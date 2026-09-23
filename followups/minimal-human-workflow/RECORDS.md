# Decision and deviation records

## D-001 — Calculated in-model data

- Classification: operational clarification
- Decision: use a three-row calculated `Sales` table rather than an external
  data source.
- Reason: exercise a real data-bound measure and visual without credentials,
  network, privacy prompts, or a manual refresh gate.

## D-002 — Existing-file batch only

- Classification: risk correction based on observed evidence
- Decision: create the table file and visual file before first open, then modify
  those same files while Desktop remains open.
- Reason: the prior experiment did not detect a visual created after open but
  did detect modifications to an already-loaded visual.

## D-003 — One batch, one apply

- Classification: minimum-operation test
- Decision: change the measure and card title before the human applies once.
- Reason: directly test whether the practical workflow can use one acceptance
  gate for a coherent model+report batch.

## Deviations

## DV-001 — Calculated-table manual-refresh banner

- Classification: non-blocking operational deviation
- Gate: `HG-01`
- Observation: cold open rendered `Baseline Total` and `60`, but Desktop showed
  `需要手动刷新一个或多个计算表。` with the action `立即刷新`.
- Action taken: none; Desktop remains open and the banner was not selected.
- Impact: the strict no-warning cold-open criterion is not met, although the
  generated model and bound visual loaded successfully. The production human
  action count remains one open and zero refresh/save actions at this point.
- Experiment handling: continue the fixed one-batch test. Do not redesign the
  model merely to erase the observation.
- Suggested follow-up interpretation: a calculated-table fixture is useful for
  credential-free testing but may add an avoidable refresh banner; a real
  source-backed project requires its own refresh/credential accounting.

## DV-002 — External-change notification not surfaced

- Classification: blocking at the original `HG-02` path; recoverable diagnostic
- Gate: `HG-02`
- Observation: after the exact two-file batch was written and committed while
  Desktop remained open, the only visible banner was still the calculated-table
  manual-refresh banner. No external-change action was available.
- File verification: both external edits remained present with their expected
  SHA-256 values; Desktop and model-server processes remained running.
- Impact: the planned one-click external apply cannot yet be executed. Dependent
  title/value verification is stopped.
- Recovery boundary: dismiss only the existing calculated-table banner by its
  close icon. Do not select `立即刷新`, save, restart, or edit the report. Count
  the dismissal as an additional human UI action and observe whether the queued
  external-change banner becomes available.
- Recovery observation: one dismissal was performed, but the same banner
  immediately reappeared and the external-change action remained unavailable.
  Dismissal is therefore not a viable workflow step.
- Next diagnostic: select `立即刷新` once. This is an explicitly counted human
  refresh action and tests whether satisfying the calculated-table requirement
  releases the queued external-change notification.
- Refresh observation: selecting `立即刷新` removed the calculated-table banner
  without an error, but no external-change banner appeared and the rendered
  state remained `Baseline Total / 60`. Thus refresh did not retroactively
  surface or apply the already-written external batch.

## D-004 — Post-refresh no-save retry batch

- Classification: controlled retry after state transition
- Decision: while Desktop remains open and unsaved, change the same two loaded
  files again to a new distinguishable state: `Tripled Total` and `180`.
- Reason: determine whether completion of the initial calculated-table refresh
  enables subsequent file-change detection without conflating the result with a
  first save.
- Boundary: no new object file, save, restart, UI edit, or MCP operation.
- Result: fail. After several seconds, no external-change banner appeared; the
  rendered state remained `Baseline Total / 60` with no error.

## D-005 — First-save diagnostic

- Classification: risk-controlled prerequisite test
- Decision: perform one human save while Desktop remains open, then inspect all
  project-file changes before writing another external batch.
- Reason: both pre-refresh and post-refresh external edits were ignored while
  the project had never been saved in the current Desktop session. Prior
  evidence suggested that first save may initialize Desktop's project-file
  monitoring state.
- Risk: Desktop may overwrite the externally authored retry state with its
  current in-memory `Baseline Total / 60` state.
- Control: retry state is committed at
  `b57fb61c9717f4948895ae789b64f8aec8e61519`; no recovery copy or hidden seed is
  required. Inspect before making any subsequent file edit.
- Result: save completed without a prompt. Desktop rewrote all 11 original
  project files, restored `Baseline Total / 60`, generated lineage tags, added
  two `.platform` files and `diagramLayout.json`, and generated four ignored
  `.pbi/` local files. This confirms first save is an initialization/ownership
  boundary rather than a no-op.
- Next test: preserve this exact Desktop-authored state as a Git checkpoint,
  then change only the existing measure and visual title once more.
- Preservation note: repository attributes deliberately keep Power BI source
  bytes without text/EOL normalization. Desktop CRLF output is committed as
  generated even though generic `git diff --check` labels it as whitespace.

## DV-003 — Post-save external batch still not detected

- Classification: blocking at the live-apply path
- Observation: after the first-save initialization checkpoint, a fresh
  two-file batch targeting `Doubled Total / 120` produced no external-change
  banner. Desktop remained on `Baseline Total / 60` without an error.
- Impact: first save alone does not make live external apply available in this
  session. The original one-open workflow has failed.
- State safety: the disk target is committed at
  `58a1448415b536db81f07841d1f6a6dfaa0dcab4`; Desktop must close without another
  save so it does not overwrite that target.
- Next diagnostic: close and reopen the same PBIP once, verify it loads the
  committed target, then write one new batch while the reopened instance runs.
- Close result: Desktop closed without a save prompt; both Desktop and model
  server exited, and the committed `Doubled Total / 120` file hashes remained
  unchanged.
- Reopen result: the same project loaded `Overview`, `Doubled Total`, and `120`
  with no calculated-table banner, warning, error, or repair prompt. This proves
  the Desktop-initialized project can consume the externally committed state on
  restart.

## D-006 — Reopened-instance live batch

- Classification: controlled retry after initialization restart
- Decision: while the cleanly reopened Desktop instance remains open, modify
  only the same existing measure and card title to `Tripled Total / 180`.
- Reason: isolate whether the close—reopen boundary, rather than first save
  alone, enables Desktop's external-change workflow.
- Boundary: no new object, save, refresh, UI edit, or MCP operation.
