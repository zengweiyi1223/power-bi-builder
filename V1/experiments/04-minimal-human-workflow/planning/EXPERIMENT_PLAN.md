# Experiment plan

## Fixed protocol

Playbook v0.1 at `3ee871d618db84d55b3b2f86a198ac552864317e` is
fixed. This experiment records observations and does not modify `playbook/**`.

## Why this test is necessary

Microsoft's current external-editing documentation says Desktop can detect and
reload external PBIP changes, including whole report/model reloads. The semantic
model folder documentation also states that externally changed TMDL files may
require a Desktop restart. This experiment resolves that ambiguity for the
installed Desktop build by observing a combined existing-file TMDL+PBIR batch.

References:

- https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-external-editing
- https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset
- https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview

## Execute-Verify sequence

1. **R0:** verify branch/worktree, empty project directory, frozen scopes, and
   no Desktop/model process. Freeze this plan in Git.
2. **R1:** generate the complete PBIP/PBIR/TMDL project with calculated data,
   measure, and pre-created bound card. Validate references, JSON, identifiers,
   and TMDL structure. Commit the pre-open checkpoint.
3. **HG-01 cold open:** human opens exact `.pbip` once and confirms title,
   `Overview`, card title `Baseline Total`, value `60`, and no prompt/error.
   Human does not save and leaves Desktop open.
4. **R2 batch edit:** Codex modifies only the existing `Sales.tmdl` measure and
   existing card `visual.json` title. Verify the exact two-file semantic diff.
5. **HG-02 apply:** human confirms one external-change banner and selects
   `Apply external changes` once. If an overwrite warning appears, stop.
6. **R3 applied verification:** human confirms title `Doubled Total`, value
   `120`, correct page/title, and no warning/error/repair.
7. **HG-03 production close:** human closes without saving; report any prompt.
8. **HG-04 validation-only reopen:** human reopens once, confirms persisted
   title/value and no error, then closes.
9. **R4:** finalize manifests, evidence, operation counts, claim limits, Git
   checkpoint, and cleanup recommendation.

## Atomicity and failure attribution

- Initial open validates cold generation independently from hot reload.
- The hot batch intentionally changes one existing TMDL file and one existing
  PBIR visual file. No new object file is created after open.
- The visible PBIR title change proves report reload; the measure result changing
  from `60` to `120` proves semantic-model metadata reload.
- If only one visible result changes, record a partial result without attempting
  a restart that would mask the failed component.

## Safety boundaries

- No copied V0 or follow-up project is used as a seed.
- `V0/`, `V1-zero-seed/`, `playbook/`, and prior `followups/` are read-only.
- No Desktop UI edits occur before external changes.
- No MCP connection is required; every MCP log entry is explicit.
- Git rollback points precede the first open and the external batch.

