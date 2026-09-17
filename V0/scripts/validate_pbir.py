"""Validate the V0 PBIP/PBIR files before opening them in Desktop."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import urlopen

from jsonschema import Draft7Validator, RefResolver


PBIP_SCHEMA = "https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/main/item-schemas/common/pbip-1.0.json"
PAGE_ID = "8fb40e89e07700078d07"
VISUAL_TYPES = Counter({"cardVisual": 3, "lineChart": 1, "clusteredColumnChart": 1, "slicer": 1})
SEED = Path(__file__).resolve().parents[1] / "seed"
SCHEMA_CACHE = {}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def fetch_schema(url):
    if url not in SCHEMA_CACHE:
        require(urlparse(url).hostname in {"developer.microsoft.com", "raw.githubusercontent.com"}, f"Unexpected schema host: {url}")
        # Microsoft's visualConfiguration schema advertises a dot-named $id,
        # while the published file uses a hyphen. Keep this alias narrow.
        published_url = url.replace("/schema.embedded.json", "/schema-embedded.json")
        with urlopen(published_url, timeout=30) as response:
            SCHEMA_CACHE[url] = json.load(response)
    return SCHEMA_CACHE[url]


def check_schema(path, data, url):
    schema = fetch_schema(url)
    resolver = RefResolver(base_uri=url, referrer=schema, handlers={"https": fetch_schema, "http": fetch_schema})
    errors = sorted(Draft7Validator(schema, resolver=resolver).iter_errors(data), key=lambda e: list(map(str, e.path)))
    require(not errors, f"{path}: JSON Schema error: {errors[0].message if errors else ''}")


def binding(visual, role):
    projections = visual["visual"]["query"]["queryState"][role]["projections"]
    require(len(projections) == 1, f"{visual['name']}: {role} must have one projection")
    p = projections[0]
    kind, item = next(iter(p["field"].items()))
    entity = item["Expression"]["SourceRef"]["Entity"]
    prop = item["Property"]
    require(p["queryRef"] == f"{entity}.{prop}", f"{visual['name']}: queryRef mismatch")
    require(p["nativeQueryRef"] == prop, f"{visual['name']}: nativeQueryRef mismatch")
    return kind, entity, prop


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    args = parser.parse_args()
    project = args.project.resolve()
    pbip = project / "PowerBIBuilderV0Seed.pbip"
    report = project / "PowerBIBuilderV0Seed.Report"
    model = project / "PowerBIBuilderV0Seed.SemanticModel"
    page_dir = report / "definition" / "pages" / PAGE_ID
    files = [pbip, report / "definition" / "report.json", report / "definition" / "version.json",
             report / "definition" / "pages" / "pages.json", page_dir / "page.json"]
    require(all(path.is_file() for path in files), "Required PBIP/PBIR file is missing")
    require(pbip.read_bytes() == (SEED / pbip.name).read_bytes(), ".pbip root changed from seed")
    require((report / "definition.pbir").read_bytes() == (SEED / report.name / "definition.pbir").read_bytes(),
            "definition.pbir changed from seed")

    root = load_json(pbip)
    check_schema(pbip, root, PBIP_SCHEMA)
    require(root["artifacts"][0]["report"]["path"] == report.name, ".pbip report path mismatch")
    definition = load_json(report / "definition.pbir")
    require(definition["datasetReference"]["byPath"]["path"] == "../" + model.name,
            "definition.pbir byPath mismatch")
    require(model.is_dir(), "Semantic model directory missing")

    for path in files[1:]:
        data = load_json(path)
        check_schema(path, data, data["$schema"])
    metadata = load_json(report / "definition" / "pages" / "pages.json")
    page = load_json(page_dir / "page.json")
    require(metadata["pageOrder"] == [PAGE_ID] and metadata["activePageName"] == PAGE_ID, "Expected exactly one Overview page")
    require(page["name"] == PAGE_ID and page["displayName"] == "Overview", "Overview page identity changed")
    require((page["width"], page["height"]) == (1280, 720), "Page must be 1280×720")

    visual_paths = sorted(page_dir.glob("visuals/*/visual.json"))
    require(len(visual_paths) == 6, "Expected exactly six visual.json files")
    visuals = [load_json(path) for path in visual_paths]
    for path, visual in zip(visual_paths, visuals):
        check_schema(path, visual, visual["$schema"])
        require(path.parent.name == visual["name"] and re.fullmatch(r"[0-9a-f]{20}", visual["name"]),
                f"{path}: visual name/folder mismatch")
    require(len({v["name"] for v in visuals}) == 6, "Visual names must be unique")
    require(Counter(v["visual"]["visualType"] for v in visuals) == VISUAL_TYPES, "Visual type count mismatch")

    for index, a in enumerate(visuals):
        p = a["position"]
        require(p["x"] >= 0 and p["y"] >= 0 and p["x"] + p["width"] <= 1280
                and p["y"] + p["height"] <= 720, f"{a['name']}: outside page")
        for b in visuals[index + 1:]:
            q = b["position"]
            overlap = p["x"] < q["x"] + q["width"] and q["x"] < p["x"] + p["width"] and p["y"] < q["y"] + q["height"] and q["y"] < p["y"] + p["height"]
            require(not overlap, f"Visual overlap: {a['name']} / {b['name']}")

    cards = [v for v in visuals if v["visual"]["visualType"] == "cardVisual"]
    require({binding(v, "Data") for v in cards} ==
            {("Measure", "FactSales", name) for name in ("销售额", "毛利额", "毛利率")},
            "Card bindings mismatch")
    line = next(v for v in visuals if v["visual"]["visualType"] == "lineChart")
    column = next(v for v in visuals if v["visual"]["visualType"] == "clusteredColumnChart")
    slicer = next(v for v in visuals if v["visual"]["visualType"] == "slicer")
    require(binding(line, "Category") == ("Column", "DimDate", "YearMonth")
            and binding(line, "Y") == ("Measure", "FactSales", "销售额"), "Line binding mismatch")
    require(binding(column, "Category") == ("Column", "DimProduct", "Category")
            and binding(column, "Y") == ("Measure", "FactSales", "销售额"), "Column binding mismatch")
    require(binding(slicer, "Values") == ("Column", "DimProduct", "Category"), "Slicer binding mismatch")
    require(slicer["visual"]["objects"]["data"][0]["properties"]["mode"]["expr"]["Literal"]["Value"] == "'Dropdown'",
            "Slicer must use Dropdown mode")
    expected_interactions = {(slicer["name"], v["name"], "DataFilter") for v in visuals if v is not slicer}
    actual_interactions = {(item["source"], item["target"], item["type"]) for item in page["visualInteractions"]}
    require(actual_interactions == expected_interactions, "Slicer interactions mismatch")

    tables_dir = model / "definition" / "tables"
    for table in ("FactSales", "DimDate", "DimProduct"):
        require((tables_dir / f"{table}.tmdl").is_file(), f"Missing model table {table}")
    fact = (tables_dir / "FactSales.tmdl").read_text(encoding="utf-8")
    dim_date = (tables_dir / "DimDate.tmdl").read_text(encoding="utf-8")
    dim_product = (tables_dir / "DimProduct.tmdl").read_text(encoding="utf-8")
    for measure in ("销售额", "销量", "成本", "毛利额", "毛利率"):
        require(f"measure {measure} =" in fact, f"Missing model measure {measure}")
    require("column YearMonth" in dim_date and "column Category" in dim_product,
            "Missing bound model column")
    print(f"PBIR preflight passed: 1 Overview page, 6 visuals, 5 explicit slicer filters; {len(SCHEMA_CACHE)} official schemas fetched.")


if __name__ == "__main__":
    main()
