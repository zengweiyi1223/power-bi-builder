# Live PBIR reload experiment

This experiment was executed as an independent follow-up to V1-zero-seed and is
now archived as V1 stage 3. It tests whether Codex can add
PBIR report content while Power BI Desktop keeps the PBIP project open, followed
by a human-triggered **Apply external changes** reload.

During execution, the experiment did not modify `V0/`, `V1-zero-seed/`, or `playbook/`.

## Fixed baselines

- Playbook v0.1: `3ee871d618db84d55b3b2f86a198ac552864317e`
- V1 final baseline: `0d47e512e3b835b9d1aa8580c68c4a853a0d325d`
- Branch: `codex/live-pbir-reload`
- Project under test: `project/LivePbirReload/LivePbirReload.pbip`

## Scope

The treatment is one static textbox added to the existing `Overview` page. It
has no model fields and no data source, so the result isolates PBIR external
editing and Desktop reload behavior.

## State

Execution, final Desktop closure, and the final Git checkpoint are complete.
The final experiment commit is `8732141fa58d6314c0b17e31116f2b0db5296d71`.
See [Final result](results/FINAL_RESULT.md) and [Handoff](results/HANDOFF.md). Planning documents are under [planning/](planning/); validation, records and Playbook feedback are under [results/](results/).
