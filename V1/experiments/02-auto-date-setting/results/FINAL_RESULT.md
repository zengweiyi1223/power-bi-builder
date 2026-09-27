# Final Result — Explicit Auto Date/Time Off

Result: `Passed`.

- Before first open, `model.tmdl` contained one model-level `annotation __PBI_TimeIntelligenceEnabled = 0`.
- First open: Current File > Data Load > Auto date/time was unchecked without Human changing it.
- Desktop save retained the annotation as `0`; no value `1` appeared.
- Reopen: the Current File checkbox remained unchecked.
- No warning, error, repair, save, close, or reopen prompt appeared.
- Final close succeeded; `PBIDesktop` and `msmdsrv` process counts were 0.
- Final project: 15 files / 3715 bytes; relative to post-save manifest: 0/0/0.

Conclusion: in Power BI Desktop `2.157.1354.0`, explicitly writing the model-level annotation automatically controls the Current File checkbox and survives Desktop save/reopen. This is stronger and more reproducible than relying on the global “new files” preference for externally generated PBIP projects.
