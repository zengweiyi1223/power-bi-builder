# Final result

Status: **PARTIAL SUCCESS — PBIR HOT RELOAD WORKS; TMDL REQUIRES RESTART**

## Proven

1. From a recorded empty directory, Codex generated a complete PBIP/PBIR/TMDL
   project containing calculated data, a measure, and a bound card. Desktop
   opened it directly and rendered `Baseline Total / 60` without a seed, repair,
   error, or manual visual/model construction.
2. The first open showed `需要手动刷新一个或多个计算表。`. One `立即刷新`
   action cleared this calculated-table-specific banner.
3. Before the first Desktop save, external changes to the already-loaded TMDL
   and PBIR files were not detected. First save alone also did not enable
   detection in that same process.
4. First save is a material initialization boundary: Desktop rewrote all 11
   authored files, restored its in-memory state, added lineage tags, generated
   two `.platform` files and `diagramLayout.json`, and created four ignored
   `.pbi/` local files.
5. After first save plus close—reopen, a fresh external batch produced the
   documented `Apply external changes` action.
6. One apply action changed the existing PBIR card title from `Doubled Total` to
   `Tripled Total`, but the measure value remained `120` instead of `180`.
7. Closing without save and reopening loaded the same PBIR title and the TMDL
   measure value `180`, with no banner, warning, error, or repair prompt.
8. Final close succeeded with `PBIDesktop=0` and `msmdsrv=0`.

## Outcome classification

The fixed acceptance contract classifies this as **Report-only hot pass**:

- cold zero-seed project generation: pass;
- existing PBIR visual hot reload: pass after Desktop initialization restart;
- existing TMDL measure hot reload through the same apply action: fail;
- TMDL reload after close—reopen: pass.

## Minimum proven human workflows

### Complete project authored before first open

`Codex generate -> Human open -> optional source/fixture refresh -> verify -> close`

No human-created seed or Desktop save is required merely for the project to
open and render. In this run the refresh was required to clear a calculated
table banner; it is not evidence that every real data source requires the same
action.

### PBIR-only iterative changes to existing loaded visuals

Initialize once:

`Open -> source/fixture refresh if required -> Save -> Close -> Reopen`

Then for each accepted PBIR-only batch:

`Codex edit existing PBIR -> Human Apply external changes`

No additional save was required for the external PBIR edit.

### Any batch containing TMDL changes

`Codex edit TMDL (and optional PBIR) -> Human Close -> Reopen -> verify`

The close—reopen loads both model and report files. Clicking `Apply external
changes` first is optional for PBIR preview but is redundant for reaching the
combined final model+report state.

## Operation accounting

The diagnostic run used 10 active human UI operations:

- initial open: `1`;
- failed banner dismissal: `1`;
- calculated-table refresh: `1`;
- first save: `1`;
- closes: `3`;
- reopens: `2`;
- apply external changes: `1`.

The failed dismissal and repeated no-save/save-only detection attempts are not
recommended workflow steps. Passive observations are not counted.

## Claim limits

- The data fixture was a calculated `DATATABLE`, not a credentialed source.
- Only one bound card, one measure, and changes to existing files were tested.
- New table/page/visual discovery while Desktop is open was not tested here.
- The result is specific to Desktop version `2.157.1354.0` and this project.
- The run does not prove that every TMDL change requires the same boundary, but
  it proves this measure edit did on the installed build.
- No MCP operation was performed; model behavior came only from file edits and
  explicit human Desktop gates.

## Git checkpoints

- Integrated baseline: `298ff99addf2b348fbea62966144705ee3543fb3`
- Plan freeze: `03b7af978616b6bfabbe2b1605b1f405e952c357`
- Pre-open: `aff4f7dd069d793c0afce89583a98a2085030f67`
- First-save initialization: `1e13a9d29dadd7d5eb926479603adbe5eee4a43e`
- Reopened-instance live batch: `1f6a2ccd8c98ec768c6f401977e2c3fbbf2c068e`
- Report-only apply evidence: `205120a49b47350510cb26b6f402c03188bd73e4`
- TMDL restart evidence: `db1a531a0b7e887fe0747d450892c95cd5c6fce3`
- Final acceptance: `8a005159aa2b739ecc4a399405b2caecb3a752f6`
