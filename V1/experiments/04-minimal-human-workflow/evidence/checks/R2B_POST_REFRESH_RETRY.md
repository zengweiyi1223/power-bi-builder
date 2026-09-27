# R2B post-refresh no-save retry

Result: **STATIC PASS; DESKTOP DETECTION PENDING**

- Captured: `2026-09-23T00:41:02.1842217-07:00`
- Desktop remained open: `yes`
- First save performed: `no`
- Existing project files modified: `2`
- New object files: `0`
- Retry title: `Tripled Total`
- Retry measure: `SUM('Sales'[Amount]) * 3`
- Expected value after apply: `180`

This retry occurred only after the human selected `立即刷新` and the persistent
calculated-table banner disappeared. The new state is deliberately distinct
from both the in-memory baseline (`Baseline Total / 60`) and the missed first
batch (`Doubled Total / 120`).
