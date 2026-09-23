# Experiment plan

## Fixed protocol

Playbook v0.1 at `3ee871d618db84d55b3b2f86a198ac552864317e` is
the execution protocol. Findings are recorded here; `playbook/**` is not edited.

## Independent variable

While Desktop holds the generated PBIP open in a clean saved state, Codex adds
one PBIR visual file under the active page's `visuals/` directory.

## Execute-Verify sequence

1. **R0 preflight:** verify branch/worktree, frozen scopes, no Desktop/model
   process, and record the empty project baseline.
2. **R1 scaffold:** Codex generates a minimal PBIP/PBIR/TMDL project and checks
   JSON/TMDL references plus a pre-open manifest. Commit a rollback checkpoint.
3. **HG-01 first open:** human opens the exact `.pbip`; confirms title,
   `Overview`, and no prompt/error.
4. **HG-02 clean save, keep open:** human saves, confirms success, and leaves
   Desktop open. Codex captures the post-save disk state before editing.
5. **R2 external PBIR edit:** Codex creates one textbox `visual.json`, validates
   syntax, identifiers, references, and the exact diff. Desktop remains open.
6. **HG-03 live detection/application:** human confirms the **Apply external
   changes** banner appears, clicks it, and reports the complete text of any
   dialog. If an overwrite warning appears, stop and do not accept it.
7. **R3 live visual verification:** human confirms the expected textbox is
   visible on `Overview` and no warning/repair/error occurred.
8. **HG-04 persistence save/close:** human saves and closes; reports any prompt.
9. **HG-05 final reopen:** human reopens once and confirms title, page, textbox,
   and absence of warnings/errors; then closes.
10. **R4 final validation:** Codex captures final manifests, diffs, logs, result,
    limitations, and commits the final checkpoint.

## Human boundary

Only the human opens Desktop, presses Save, selects **Apply external changes**,
visually evaluates the report, and closes Desktop. Codex performs repository and
project-file operations only. MCP actions, if any, are separately logged and are
not substituted for human confirmation.

## Stop rules

- **Blocking:** wrong branch/worktree; dirty unknown changes; Desktop/model
  process present before R1; generated project fails static checks; overwrite
  warning after external editing; blocking schema/open error; visual missing
  after reload; repair required. Stop all dependent steps.
- **Non-blocking:** UI layout reset, filter reset, or additional Desktop-local
  metadata files, provided they do not change the expected project semantics.
  Record before continuing.
- If a failure can be corrected without erasing evidence, preserve the failed
  state and use a new checkpoint. Do not silently rewrite the run record.

## Evidence requirements

- Empty, pre-open, post-save/pre-edit, post-external-edit, post-apply,
  post-save/closed, and final-reopen manifests as applicable
- Human action log with exact confirmations
- Codex file-action JSONL log
- MCP action JSONL log, including explicit `none` entries
- Static JSON parsing and reference checks after each file batch
- Git checkpoint before first open and at final acceptance

## Safety basis

Microsoft documents that Desktop detects external PBIP changes and offers
**Apply external changes**, but also warns that Desktop and external tools can
overwrite each other. Desktop must therefore be saved before the external edit.
Reload is whole-report/model rather than per-visual, and some project files do
not support external editing.

References:

- https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-external-editing
- https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report

