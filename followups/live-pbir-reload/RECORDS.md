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

None recorded yet.

