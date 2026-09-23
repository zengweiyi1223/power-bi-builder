# Handoff

## Outcome

Zero-seed direct generation works for a real bound card and model. The minimum
ongoing workflow depends on the file layer being changed:

| Change type | Minimum proven acceptance action |
| --- | --- |
| Complete project before first open | Open and verify; refresh only if prompted |
| Existing PBIR visual after initialization | `Apply external changes` once |
| Any tested TMDL measure change | Close and reopen |
| Combined TMDL + PBIR batch | Close and reopen; prior apply is redundant |

## Recommended real-project route

1. Codex generates the complete PBIP/PBIR/TMDL project and pre-scaffolds known
   pages and visuals before first open.
2. Human opens and validates the generated project. Handle only genuine source
   credential/refresh gates; do not assume this experiment's calculated-table
   banner applies to every project.
3. If future PBIR-only live iteration is desired, perform one initialization
   save, close, and reopen. Thereafter batch existing PBIR changes and accept
   them with one `Apply external changes` action.
4. When a batch changes TMDL, skip the apply-only expectation. Close without
   saving Desktop's stale in-memory state, reopen, and validate both model and
   report together.
5. Keep Git checkpoints before first open, before Desktop save, before each
   external batch, and before restart. Desktop first save can overwrite ignored
   external changes and materially normalize the project.

## What is not required

- No human-created blank PBIP seed.
- No human model, measure, binding, or visual construction.
- No save after a successfully applied external-only PBIR change.
- No separate apply click before restarting for a combined TMDL+PBIR batch.

## Evidence locations

- Human operations: `logs/HUMAN_ACTIONS.md`
- Codex file operations: `logs/CODEX_FILE_ACTIONS.jsonl`
- MCP operations: `logs/MCP_ACTIONS.jsonl`
- Exact manifests: `manifests/`
- Screenshots and checks: `evidence/`
- Decisions and deviations: `RECORDS.md`
- Full conclusion and claim limits: `FINAL_RESULT.md`

## Cleanup

Final closure passed and the branch is self-contained. Keep the worktree until
the result is accepted or integrated. It can then be removed while retaining
branch `codex/minimal-human-workflow` and its commits.
