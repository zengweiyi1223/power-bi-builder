# Minimal human workflow experiment

This independent follow-up determines the smallest real human-operation sequence
for a Codex-authored PBIP project containing a semantic model and a data-bound
PBIR visual.

## Fixed baselines

- Playbook v0.1: `3ee871d618db84d55b3b2f86a198ac552864317e`
- Integrated follow-up baseline: `298ff99addf2b348fbea62966144705ee3543fb3`
- Branch: `codex/minimal-human-workflow`
- Project: `project/MinimalWorkflow/MinimalWorkflow.pbip`

## Scope

- One calculated `Sales` table with three rows
- One measure: `Total Amount`
- One pre-created, data-bound `cardVisual`
- One simultaneous external batch modifying the existing TMDL measure and the
  existing PBIR card title
- Human-operation accounting separated into production-required and
  validation-only operations

No Desktop operation may begin before the plan-freeze and pre-open checkpoints.

## Current state

- Plan freeze: `03b7af978616b6bfabbe2b1605b1f405e952c357`
- Final outcome: report-only hot pass; TMDL restart pass
- Final rendered state: `Tripled Total / 180`
- Final Desktop/model processes: `0 / 0`
- See `FINAL_RESULT.md` for minimum workflows and claim limits
