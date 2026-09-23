# Save/Close Persistence

- Human: save and close succeeded; no prompt.
- `PBIDesktop` / `msmdsrv` after close: `0 / 0`.
- Project: 15 files / 3715 bytes.
- Relative to pre-open: 6 added / 9 modified / 0 deleted.
- Added files are the same Desktop platform/local/cache/layout categories observed in V1.
- `model.tmdl` retains exactly one `annotation __PBI_TimeIntelligenceEnabled = 0` and no value `1`.
- Desktop also added `annotation PBI_ProTooling = ["DevMode"]`.

The explicit off setting survived Desktop serialization. A reopen UI confirmation remains required.
