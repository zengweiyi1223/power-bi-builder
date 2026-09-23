# Human actions

## HG-01 — First open

Result: **PASS**

Human confirmation:

1. Successfully entered the report view.
2. `Overview` was blank and contained no textbox.
3. Window title was `LivePbirReload`.
4. No popup, warning, error, or repair prompt appeared.

Desktop was left open. No save was requested at this gate.

## HG-02 — Pre-edit save

Result: **SKIPPED BY HUMAN DECISION**

The human requested testing the minimum-step path without an explicit save.
No Desktop edit had occurred, and Codex rechecked that the project disk state
was unchanged before applying the external file edit.

## HG-03a — Initial external-change detection

Result: **FAIL — NO DETECTION UI**

After Codex created the new visual directory and `visual.json`, the human
reported that no prompt or banner of any kind appeared in Desktop.

## HG-03b — Existing visual file modification detection

Result: **FAIL — NO DETECTION UI**

After Codex modified the text inside the existing `visual.json`, the human again
reported no prompt, banner, warning, error, or visible change of any kind.

## HG-02b — First Desktop save after failed detection

Result: **PASS**

The human saved successfully, kept Desktop open, and observed no prompt,
warning, or error. This save occurred only after both no-save detection attempts
had failed.

## HG-03c — Post-first-save external modification detection

Result: **FAIL — NO DETECTION UI**

After the first successful Desktop save, Codex modified the same existing-on-disk
visual file again. The human reported that Desktop still showed no prompt or
banner. The supplied screenshot shows the blank `Overview` page and title
`LivePbirReload` with no external-change UI.

Evidence: `evidence/screenshots/HG03_POST_SAVE_NO_DETECTION.png`

## HG-04 — Reopen loads the external visual

Result: **PASS**

After closing and reopening, the human confirmed:

1. `Overview` displayed `Live PBIR after first save succeeded`.
2. The window title remained `LivePbirReload`.
3. No warning, error, or repair prompt appeared.

Desktop remained open for the loaded-visual modification test.

Evidence: `evidence/screenshots/HG04_REOPEN_VISUAL_LOADED.png`

## HG-05a — Loaded visual external change detected

Result: **PASS — BANNER DISPLAYED**

After Codex modified the already-loaded visual file, Desktop displayed:

> This project's files were changed externally. Apply to view the latest changes.

The banner offered the `Apply external changes` button. At this evidence point,
the old text remained visible because the reload had not yet been applied.

Evidence: `evidence/screenshots/HG05_LOADED_VISUAL_CHANGE_DETECTED.png`

## HG-05b — Apply loaded visual external change

Result: **PASS**

The human selected `Apply external changes`. Desktop applied the change
directly and displayed `Live PBIR loaded-visual hot reload succeeded` on
`Overview`. The title remained `LivePbirReload`, and the supplied screenshot
shows no warning, error, or repair prompt.

Evidence: `evidence/screenshots/HG05_APPLY_EXTERNAL_CHANGES_SUCCESS.png`

## HG-06 — Close without save and final reopen

Result: **PASS**

The human closed Desktop without saving and received no prompt. After reopening:

1. `Live PBIR loaded-visual hot reload succeeded` remained visible.
2. `Overview` and the `LivePbirReload` title remained correct.
3. No warning, error, or repair prompt appeared.

Desktop was kept open pending final evidence completion and checkpointing.

Evidence: `evidence/screenshots/HG06_FINAL_REOPEN_NO_SAVE.png`

## HG-07 — Final closure

Result: **PASS**

The human closed Desktop and reported no prompt. Codex subsequently verified
`PBIDesktop=0` and `msmdsrv=0`.
