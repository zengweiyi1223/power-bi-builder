"""Compute a reproducible, Power BI-independent baseline from V0 sales.csv."""

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path


COLUMNS = (
    "SaleDate", "ProductKey", "Product", "Category", "Quantity", "UnitPrice", "UnitCost"
)
INTERACTION_CATEGORY = "Technology"
ZERO_SALES_CATEGORY = "ZeroSales"
CENT = Decimal("0.01")


def read_rows(path):
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    if text.startswith("\ufeff"):
        raise ValueError("CSV must be UTF-8 without BOM")
    reader = csv.DictReader(text.splitlines(), delimiter=",")
    if tuple(reader.fieldnames or ()) != COLUMNS:
        raise ValueError(f"CSV columns must be exactly {COLUMNS}")

    rows = []
    products = {}
    date_products = set()
    for line_number, source in enumerate(reader, start=2):
        if None in source or any(value is None or value == "" for value in source.values()):
            raise ValueError(f"Missing or extra field on line {line_number}")
        try:
            sale_date = date.fromisoformat(source["SaleDate"])
            if sale_date.isoformat() != source["SaleDate"]:
                raise ValueError("date must use YYYY-MM-DD")
            product_key = int(source["ProductKey"])
            quantity = int(source["Quantity"])
            price = Decimal(source["UnitPrice"])
            cost = Decimal(source["UnitCost"])
        except (ValueError, InvalidOperation) as error:
            raise ValueError(f"Invalid typed value on line {line_number}: {error}") from error
        if product_key <= 0 or quantity < 0 or price < 0 or cost < 0:
            raise ValueError(f"Negative value or nonpositive key on line {line_number}")
        if price != price.quantize(CENT) or cost != cost.quantize(CENT):
            raise ValueError(f"Money has more than two decimals on line {line_number}")
        if not source["Product"].strip() or not source["Category"].strip():
            raise ValueError(f"Empty dimension attribute on line {line_number}")
        product_identity = (source["Product"], source["Category"])
        if product_key in products and products[product_key] != product_identity:
            raise ValueError(f"ProductKey {product_key} has conflicting attributes")
        products[product_key] = product_identity
        grain = (sale_date, product_key)
        if grain in date_products:
            raise ValueError(f"Duplicate date-product grain on line {line_number}")
        date_products.add(grain)
        rows.append((sale_date, source["Category"], quantity, price, cost))

    if not rows:
        raise ValueError("CSV contains no sales rows")
    categories = {row[1] for row in rows}
    if INTERACTION_CATEGORY not in categories or ZERO_SALES_CATEGORY not in categories:
        raise ValueError("Required test categories are missing")
    return rows, len(products), hashlib.sha256(raw).hexdigest()


def metrics(rows):
    quantity = sum((row[2] for row in rows), 0)
    sales = sum((Decimal(row[2]) * row[3] for row in rows), Decimal(0))
    cost = sum((Decimal(row[2]) * row[4] for row in rows), Decimal(0))
    profit = sales - cost
    return {
        "销售额": float(sales.quantize(CENT)),
        "销量": quantity,
        "成本": float(cost.quantize(CENT)),
        "毛利额": float(profit.quantize(CENT)),
        "毛利率": float(profit / sales) if sales else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).resolve().parents[1] / "data" / "sales.csv")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    rows, product_count, source_hash = read_rows(args.input)
    months = defaultdict(list)
    categories = defaultdict(list)
    for row in rows:
        months[row[0].strftime("%Y-%m")].append(row)
        categories[row[1]].append(row)
    if metrics(categories[ZERO_SALES_CATEGORY])["销售额"] != 0:
        raise ValueError("ZeroSales category must have zero sales")

    result = {
        "source": "V0/data/sales.csv",
        "sourceSha256": source_hash,
        "rowCount": len(rows),
        "productCount": product_count,
        "interactionTestCategory": INTERACTION_CATEGORY,
        "zeroSalesTestCategory": ZERO_SALES_CATEGORY,
        "tolerances": {"quantity": 0, "amount": 0.01, "ratio": 0.0001},
        "totals": metrics(rows),
        "byMonth": {
            month: {key: value for key, value in metrics(group).items() if key in ("销售额", "毛利额")}
            for month, group in sorted(months.items())
        },
        "byCategory": {
            category: {key: value for key, value in metrics(group).items() if key in ("销售额", "毛利额")}
            for category, group in sorted(categories.items())
        },
        "interactionTestMetrics": metrics(categories[INTERACTION_CATEGORY]),
        "zeroSalesTestMetrics": metrics(categories[ZERO_SALES_CATEGORY]),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
