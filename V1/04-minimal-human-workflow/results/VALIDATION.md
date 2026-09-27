# Validation

Status: **FINAL — REPORT-ONLY HOT PASS; TMDL RESTART PASS**

## Baselines

- Playbook v0.1: `3ee871d618db84d55b3b2f86a198ac552864317e`
- Integrated baseline: `298ff99addf2b348fbea62966144705ee3543fb3`
- Plan freeze: `03b7af978616b6bfabbe2b1605b1f405e952c357`
- Pre-open checkpoint: `aff4f7dd069d793c0afce89583a98a2085030f67`
- Initial external-batch checkpoint: `802b32a97b7a72f17a041ba08d1553927452a693`
- Post-refresh retry checkpoint: `b57fb61c9717f4948895ae789b64f8aec8e61519`
- First-save checkpoint: `1e13a9d29dadd7d5eb926479603adbe5eee4a43e`
- Post-save external-batch checkpoint: `58a1448415b536db81f07841d1f6a6dfaa0dcab4`
- Reopened-instance live-batch checkpoint: `1f6a2ccd8c98ec768c6f401977e2c3fbbf2c068e`
- Final acceptance: `8a005159aa2b739ecc4a399405b2caecb3a752f6`

## Gates

| Gate | Result | Evidence |
| --- | --- | --- |
| R0 empty baseline and plan freeze | Pass | `manifests/EMPTY_BASELINE.json`, `evidence/checks/R0_PREFLIGHT.md` |
| R1 complete generated project | Pass (static) | `manifests/PRE_OPEN.json`, `evidence/checks/R1_COMPLETE_PROJECT.md` |
| HG-01 cold open: title 60 | Core pass; non-blocking banner deviation | `logs/HUMAN_ACTIONS.md`, `evidence/checks/HG-01_COLD_OPEN.md`, screenshot |
| R2 two-file external batch | Pass (static) | `manifests/EXTERNAL_BATCH.json`, `evidence/checks/R2_EXTERNAL_BATCH.md` |
| HG-02 one apply action | Pass: one action completed without error | `evidence/checks/HG-02B_EXTERNAL_BANNER.md`, screenshot |
| R3 combined title/value update | Partial: title `Tripled Total`; value remained `120` | `evidence/checks/HG-02C_APPLY_PARTIAL.md`, screenshot |
| HG-03 closes without save | Pass; no prompt and hashes preserved | `logs/HUMAN_ACTIONS.md`, `manifests/FINAL_CLOSED_CHECK.json` |
| HG-04 TMDL reload reopen | Pass: `Tripled Total / 180` | `evidence/checks/HG-04_TMDL_REOPEN.md`, screenshot |
| R4 final acceptance | Pass with report-only hot-reload boundary | `FINAL_RESULT.md`, `HANDOFF.md`, `manifests/FINAL_CLOSED_CHECK.json` |

## Operation result

The diagnostic run used 10 active human UI operations: one initial open, one
failed banner dismissal, one refresh, one save, three closes, two reopens, and
one external-apply action. See `FINAL_RESULT.md` for the smaller production
flows derived from the observed boundaries; failed diagnostics are not treated
as required workflow steps.
