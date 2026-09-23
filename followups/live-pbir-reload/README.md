# Live PBIR reload experiment

This is an independent follow-up to V1-zero-seed. It tests whether Codex can add
PBIR report content while Power BI Desktop keeps the PBIP project open, followed
by a human-triggered **Apply external changes** reload.

The experiment does not modify `V0/`, `V1-zero-seed/`, or `playbook/`.

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

Plan and safety boundaries are frozen at `fc671ac`. The zero-seed scaffold has
passed static validation and awaits its pre-open checkpoint and HG-01.
