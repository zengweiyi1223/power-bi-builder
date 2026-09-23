# R2 two-file external batch

Result: **PASS — STATIC BATCH CHECKS**

- Captured: `2026-09-23T00:25:25.6193956-07:00`
- Desktop remained open: `yes`
- `PBIDesktop` process count: `1`
- `msmdsrv` process count: `1`
- Existing project files modified: `2`
- New table/page/visual/object files: `0`
- Human save requested: `no`
- MCP connected: `no`

The exact project diff is:

1. Existing `Sales.tmdl`: `Total Amount` now evaluates
   `SUM('Sales'[Amount]) * 2`.
2. Existing card `visual.json`: title literal changed from `Baseline Total` to
   `Doubled Total`.

The visual JSON parsed and both intended values were asserted. No other project
file differs from pre-open checkpoint `aff4f7dd069d793c0afce89583a98a2085030f67`.
The next Human Gate determines whether one Desktop external-change action
applies both changes.
