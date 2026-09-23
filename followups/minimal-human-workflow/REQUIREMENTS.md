# Requirements and acceptance contract

## Objective

Produce observed evidence for the minimum real human workflow, rather than an
assumed workflow, when Codex authors both a semantic model and a data-bound PBIR
visual from an empty directory.

## Baseline model and report

- Table: `Sales`
- Rows: `A=10`, `B=20`, `C=30`
- Measure: `Total Amount = SUM('Sales'[Amount])`
- Expected baseline value: `60`
- Page: `Overview`
- Visual: pre-created `cardVisual` bound to `Sales.Total Amount`
- Baseline title: `Baseline Total`
- Auto date/time: explicitly off at model level

## External batch

While Desktop remains open and has no human edits:

1. Modify the existing measure to `SUM('Sales'[Amount]) * 2`.
2. Modify the existing card title to `Doubled Total`.
3. Make no new table, page, visual directory, or object file.

Expected applied state: title `Doubled Total`, card value `120`.

## Required success criteria

1. Project starts from a recorded empty directory without a copied seed.
2. First open succeeds without save, repair, warning, or error.
3. First open shows `Baseline Total` and value `60`.
4. Desktop remains open while Codex applies the TMDL+PBIR file batch.
5. Exactly one actionable external-change gate appears for the batch.
6. One human `Apply external changes` action updates both title and value.
7. No pre-batch or post-apply save is required.
8. Production close succeeds without prompt.
9. One validation-only reopen proves persistence without repair or error.
10. Human, Codex file, and MCP actions are logged separately.

## Outcome classes

- **Full pass:** all success criteria hold.
- **Cold-only pass:** initial model/report works, but one-batch hot reload fails.
- **Report-only hot pass:** PBIR title updates but TMDL value remains `60`.
- **Model-only hot pass:** value updates but PBIR title remains unchanged.
- **Fail:** initial project is invalid, data-bound visual errors, or persisted
  state cannot reopen cleanly.

## Claim boundary

The run tests modification of already-loaded files. It does not claim that new
table or visual files created after open are detected.

