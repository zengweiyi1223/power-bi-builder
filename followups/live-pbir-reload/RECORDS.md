# Decision and deviation records

## D-001 — Static textbox treatment

- Type: operational clarification
- Decision: add one static textbox with no query or model binding.
- Reason: isolate PBIR detection/reload from semantic-model and data behavior.

## D-002 — Save before external edit

- Type: risk correction
- Decision: require an explicit human save while Desktop remains open before
  Codex changes PBIR.
- Reason: Microsoft warns that Desktop and external tools can overwrite each
  other's changes and recommends saving before external editing.

## D-003 — One final reopen remains in this validation

- Type: operational clarification
- Decision: retain a final close/reopen only as persistence evidence.
- Reason: the experiment tests whether the *intermediate* close/reopen can be
  removed. Omitting final persistence validation would conflate two claims.

## Deviations

## DEV-001 — Skip pre-edit Desktop save

- Requested by: human
- Classification: operational deviation / minimum-step treatment
- Observation before treatment: Desktop had received no human edits; opening
  caused no disk changes (`added=0`, `modified=0`, `removed=0`); the pre-open
  Git checkpoint remained available.
- Change: HG-02's explicit save was skipped. Desktop remained open while Codex
  wrote the visual.
- Risk: Desktop may still regard in-memory initialization as unsaved and display
  an overwrite warning when applying the external change.
- Stop boundary: if an overwrite warning appears, do not confirm it; record the
  full text and stop.
- Value: directly tests the minimum-human-step route requested for generated
  PBIP projects.

## DEV-002 — Same-run existing-file write retry

- Trigger: creating the new visual directory/file produced no external-change
  prompt in Desktop.
- Classification: blocking detection failure followed by a bounded diagnostic
  retry.
- Decision: keep the same visual and modify only its text in the existing
  `visual.json`; do not add another object and do not save/close Desktop.
- Purpose: distinguish an unobserved new-directory/create event from a general
  failure to detect external PBIR file modifications.
- Interpretation: success on retry would prove existing-file modification can
  trigger reload, but it would not erase the initial create-event failure.

## DEV-003 — First-save initialization probe

- Trigger: both the visual-create event and a subsequent existing-file modify
  event produced no Desktop detection UI before any Desktop save.
- Decision: human performed the first Desktop save while keeping Desktop open;
  Codex then modified the same visual file again.
- Observation after save: Desktop supplemented/rewrote project metadata but
  preserved the external visual file byte-for-byte.
- Purpose: test whether the first Desktop save initializes external-change
  monitoring for an independently generated PBIP.
- Result: it did not. The post-save external modification also produced no
  detection UI, and the page remained blank.

## DEV-004 — Load-before-modify diagnostic

- Trigger: a visual created after initial open remained undetected before and
  after the first Desktop save.
- Decision: close and reopen once so Desktop loads the visual from disk, then
  modify that already-loaded `visual.json` while Desktop remains open.
- Purpose: distinguish “new, never-loaded object is not monitored” from “this
  Desktop build does not support external PBIR reload at all.”
- Cost: one extra close/reopen, retained only as diagnostic evidence.
