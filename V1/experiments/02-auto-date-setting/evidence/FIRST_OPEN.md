# First Open — Explicit Auto Date/Time Off

- Human observation: Current File > Data Load > Auto date/time was unchecked without changing the option.
- Report: opened normally and displayed `Overview`.
- Prompts: no warning, error, or repair prompt.
- Human closed the Options dialog with no setting change and kept Desktop open.
- Desktop PID: `30708`; model PID: `19868`.
- Project after open/no save: 9 files / 1562 bytes.
- Relative to pre-open: 0 added / 0 modified / 0 deleted.
- `model.tmdl` still contains exactly one model-level `annotation __PBI_TimeIntelligenceEnabled = 0`.

The primary hypothesis is supported at first open. Persistence through Desktop save and reopen remains to be tested.
