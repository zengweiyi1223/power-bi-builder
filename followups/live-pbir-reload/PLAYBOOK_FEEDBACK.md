# Playbook feedback

This file records observations only. It does not modify Playbook v0.1.

## Observation

External-edit behavior differed between a visual created after Desktop opened
and a visual already loaded in the session. The former was not detected; the
latter produced the documented banner and reloaded successfully.

## Impact

A generic “edit PBIR while Desktop is open” instruction is underspecified. The
object's load state materially affects whether the user receives an actionable
reload gate. Requiring a save before every external edit did not solve the
never-loaded-object case in this run.

## Suggestion

Future Playbook revisions could distinguish:

- external modification of files already loaded by Desktop;
- creation of new PBIR object files after Desktop is open;
- whether Desktop has unsaved in-memory edits;
- whether persistence verification is production work or validation-only work.

For minimal human interaction, consider pre-scaffolding known visual files
before first open, then batching edits and using one **Apply external changes**
gate per accepted batch.

