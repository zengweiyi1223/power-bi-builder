# Requirements and acceptance contract

## Objective

Determine whether Power BI Desktop can remain open while Codex adds a PBIR
visual, and whether a human can apply that external change without closing and
reopening Desktop between the blank-project and visual-authoring stages.

## Required success criteria

1. The treatment project begins as an empty directory and is generated without
   copying a seed project.
2. The generated PBIP opens normally on a blank page named `Overview`.
3. The human saves the open project before Codex edits PBIR and keeps Desktop
   open.
4. Codex adds exactly one static textbox through a new PBIR `visual.json`; no
   model or data-source change is part of the treatment.
5. Desktop detects the external change and offers **Apply external changes**.
6. Applying the change shows the expected textbox on `Overview` without a
   warning, repair dialog, or error.
7. Saving, closing, and reopening preserves the textbox without warning,
   repair, or error.
8. Human actions, Codex file actions, and MCP actions are logged separately.

## Expected visual

- Type: static textbox
- Text: `Live PBIR reload succeeded`
- Page: `Overview`
- No semantic-model binding

## Non-goals

- Model editing while Desktop is open
- Data refresh or data-source connectivity
- Desktop Bridge automation
- General workflow or Playbook modification
- Proving that every PBIR object type supports live reload

## Outcome classes

- **Pass:** criteria 1-8 all hold.
- **Partial:** the visual is valid after close/reopen but live detection or live
  application fails. This does not prove a one-open workflow.
- **Fail:** Desktop rejects, repairs, omits, or cannot persist the visual.

