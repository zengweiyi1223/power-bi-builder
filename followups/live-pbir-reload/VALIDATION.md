# Validation

Status: **PARTIAL SUCCESS — MATERIAL BOUNDARY IDENTIFIED**

## Baselines

- Playbook v0.1: `3ee871d618db84d55b3b2f86a198ac552864317e`
- V1 final baseline: `0d47e512e3b835b9d1aa8580c68c4a853a0d325d`
- Plan-freeze commit: `fc671ac2c1638d19a249eb9dcaee735211fc61d3`
- Pre-open checkpoint: `39ea434a634746ddfe898ce90b3dbd61a66fda68`
- Final acceptance commit: `8732141fa58d6314c0b17e31116f2b0db5296d71`

## Gate results

| Gate | Result | Evidence |
| --- | --- | --- |
| R0 preflight and empty baseline | Pass | `evidence/checks/R0_PREFLIGHT.md` |
| R1 generated scaffold | Pass | `evidence/checks/R1_GENERATED_SCAFFOLD.md`, `manifests/PRE_OPEN.json` |
| HG-01 first open | Pass | `logs/HUMAN_ACTIONS.md`, `manifests/POST_OPEN_NO_SAVE.json` |
| HG-02 save and keep open | Initially skipped; later diagnostic first save passed | `RECORDS.md#dev-001--skip-pre-edit-desktop-save`, `manifests/POST_FIRST_DESKTOP_SAVE.json` |
| R2 external PBIR edit | Static pass; Desktop pending | `evidence/checks/R2_EXTERNAL_PBIR_EDIT.md`, `manifests/POST_EXTERNAL_EDIT.json` |
| HG-03 apply external changes | Never-loaded visual: fail; already-loaded visual: detection and application pass | `logs/HUMAN_ACTIONS.md`, `evidence/screenshots/HG03_POST_SAVE_NO_DETECTION.png`, `evidence/screenshots/HG05_LOADED_VISUAL_CHANGE_DETECTED.png`, `evidence/screenshots/HG05_APPLY_EXTERNAL_CHANGES_SUCCESS.png` |
| R3 visual valid after reopen | Pass | `logs/HUMAN_ACTIONS.md`, `evidence/screenshots/HG04_REOPEN_VISUAL_LOADED.png` |
| HG-04 save/close | Replaced by close without save; pass | `logs/HUMAN_ACTIONS.md` |
| HG-05 final reopen | Pass | `manifests/FINAL_REOPEN_NO_SAVE.json`, `evidence/screenshots/HG06_FINAL_REOPEN_NO_SAVE.png` |
| R4 final validation | Pass | `FINAL_RESULT.md`, `manifests/FINAL_CLOSED_CHECK.json` |

## Result

Live PBIR reload succeeds for modifications to a visual already loaded by
Desktop. The same session did not detect a visual created after initial open,
even after the first Desktop save. See `FINAL_RESULT.md` for the claim boundary.
