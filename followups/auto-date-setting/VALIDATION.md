# Explicit Auto Date/Time — Validation

- Status: `Pre-open validation passed; waiting HG-AD-01`
- Baseline: `0d47e512e3b835b9d1aa8580c68c4a853a0d325d`
- Branch: `codex/auto-date-setting`
- Project: `AutoDateExplicitOff`
- Independent variable: model-level `annotation __PBI_TimeIntelligenceEnabled = 0`

## Hypothesis

Opening this externally generated PBIP project in Power BI Desktop will show Current File > Data Load > Auto date/time as unchecked without a Human changing that setting.

## Controls

- Negative control already observed: V1 projects omitted the annotation and showed the Current File option checked.
- Desktop-created control observed by Human: with the global “Auto date/time for new files” option off, a Desktop-created new file showed the Current File option unchecked.
- Treatment: this project is externally generated and explicitly includes the model-level annotation set to `0`.

## Gates

1. Prove the project root started at 0 files / 0 subdirectories.
2. Generate and statically validate the minimum PBIP/PBIR/TMDL project.
3. Commit a pre-open checkpoint while Desktop is not running.
4. Human opens the exact `.pbip` without saving and checks the Current File option.
5. Compare the project directory to the pre-open manifest.

No V1, V0, or `playbook/**` file is modified.

## Pre-open result

- Empty baseline: Passed (`0` files / `0` subdirectories).
- Generated project: Passed (`9` files / `1562` bytes).
- JSON, references, page identity, minimal TMDL, and process checks: Passed.
- Treatment annotation: `annotation __PBI_TimeIntelligenceEnabled = 0` present at model level.
- Desktop has not opened the project.
