# Handoff

## Outcome

The experiment proves live reload for modifications to an already-loaded PBIR
visual. It does not prove live discovery of a new visual created after Desktop
opened.

## Recommended real-project route

1. Codex generates the PBIP/PBIR/TMDL project and pre-scaffolds the known pages
   and visual files before first open.
2. Human opens the project once. A first save is needed only if Desktop or a
   connected modeling workflow has in-memory changes that must be preserved.
3. Codex modifies existing, loaded PBIR visual files.
4. Human selects **Apply external changes** and verifies the result.
5. For external-only PBIR edits, a second save is not required for persistence;
   close/reopen was used here only as acceptance evidence.
6. If Codex adds a completely new visual after open, use a close/reopen boundary
   unless a separate experiment proves live discovery for that creation route.

## Human operations observed in this diagnostic run

- Initial open
- One first save used as a diagnostic (it did not discover the new visual)
- Close/reopen to load the newly created visual
- Click **Apply external changes**
- Close/reopen without save for final persistence validation

These are experimental operations, not all mandatory production operations.
For the proven pre-scaffolded route, routine operation can be one initial open,
one **Apply external changes** click per accepted batch, and final close; save is
conditional on in-Desktop changes.

## Known limits

- Only one static textbox was tested.
- No data-bound visual, new page, model hot reload, Desktop Bridge, or MCP model
  write was tested.
- Results are specific to Desktop version `2.157.1354.0` and this local project.
- The run cannot establish behavior for every PBIR schema/object type.

## Cleanup

The final closure and Git checkpoint passed. The temporary worktree has been
removed; branch `codex/live-pbir-reload` and its commits are retained and
integrated into the repository's follow-up history.
