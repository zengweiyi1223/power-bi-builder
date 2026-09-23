# Validation

Status: **POST-SAVE LIVE DETECTION FAILED; INITIALIZATION RESTART REQUIRED**

## Baselines

- Playbook v0.1: `3ee871d618db84d55b3b2f86a198ac552864317e`
- Integrated baseline: `298ff99addf2b348fbea62966144705ee3543fb3`
- Plan freeze: `03b7af978616b6bfabbe2b1605b1f405e952c357`
- Pre-open checkpoint: this commit (exact SHA reported after creation)
- External-batch checkpoint: this commit (exact SHA reported after creation)
- Post-refresh retry checkpoint: this commit (exact SHA reported after creation)
- First-save checkpoint: this commit (exact SHA reported after creation)
- Post-save external-batch checkpoint: this commit (exact SHA reported after creation)
- Final acceptance: pending

## Gates

| Gate | Result | Evidence |
| --- | --- | --- |
| R0 empty baseline and plan freeze | Pass | `manifests/EMPTY_BASELINE.json`, `evidence/checks/R0_PREFLIGHT.md` |
| R1 complete generated project | Pass (static) | `manifests/PRE_OPEN.json`, `evidence/checks/R1_COMPLETE_PROJECT.md` |
| HG-01 cold open: title 60 | Core pass; non-blocking banner deviation | `logs/HUMAN_ACTIONS.md`, `evidence/checks/HG-01_COLD_OPEN.md`, screenshot |
| R2 two-file external batch | Pass (static) | `manifests/EXTERNAL_BATCH.json`, `evidence/checks/R2_EXTERNAL_BATCH.md` |
| HG-02 one apply action | Blocked: action not surfaced | `logs/HUMAN_ACTIONS.md`, `RECORDS.md` DV-002 |
| R3 title 120 | Pending | human log/screenshot |
| HG-03 production close without save | Pending | human log/process check |
| HG-04 validation-only reopen | Pending | human log/screenshot |
| R4 final acceptance | Pending | final result/handoff |

## Operation result

No operation count is claimed until observed.
