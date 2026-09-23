# HG-01 cold open

Result: **CORE PASS WITH NON-BLOCKING DEVIATION**

The human opened the exact pre-open checkpoint project once and did not save.

| Check | Observed |
| --- | --- |
| Report interface opened | Pass |
| Page is `Overview` | Pass |
| Card title is `Baseline Total` | Pass |
| Card value is `60` | Pass |
| Window title is `MinimalWorkflow` | Pass |
| Popup, error, or repair dialog | None |
| Project files rewritten by Desktop | No |
| Informational/action banner | `需要手动刷新一个或多个计算表。` |
| Banner button | `立即刷新` |
| Banner button selected | No |

The calculated table and bound measure already rendered the expected value
`60`, so the banner did not block the experiment. It does violate the strict
criterion that first open have no warning or prompt. The experiment continues
without selecting `立即刷新`; whether one external-change apply can refresh the
model and update the report remains the next atomic test.

Screenshot SHA-256:
`DB345DC2927DD728830D768C2937AB5C865594B967978C4794C80E889EAB3C13`.
