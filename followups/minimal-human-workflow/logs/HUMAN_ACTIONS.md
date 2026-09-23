# Human actions

## H-001 — HG-01 cold open

- Recorded at: `2026-09-23T00:22:05.6900174-07:00`
- Action: opened `project/MinimalWorkflow/MinimalWorkflow.pbip`
- Production operation count: open `1`, save `0`, refresh `0`, apply external
  changes `0`, close `0`, reopen `0`
- Observed page: `Overview`
- Observed card title: `Baseline Total`
- Observed card value: `60`
- Observed window title: `MinimalWorkflow`
- Popup/error/repair dialog: none
- Banner: `需要手动刷新一个或多个计算表。`
- Banner action offered: `立即刷新`
- Banner action taken: no
- End state: Desktop remains open; no save or report edit was performed
- Evidence: `evidence/screenshots/HG-01-cold-open.png`

## H-002 — HG-02 notification observation

- Recorded at: `2026-09-23T00:30:36.3975331-07:00`
- Observation: after the committed two-file external batch, Desktop still showed
  only `需要手动刷新一个或多个计算表。`
- Expected external-change banner: not visible
- Human action taken: none
- Production operation count remains: open `1`, save `0`, refresh `0`, apply
  external changes `0`, dismiss banner `0`, close `0`, reopen `0`
- End state: Desktop remains open

## H-003 — Dismiss calculated-table banner

- Recorded at: `2026-09-23T00:35:17.0438513-07:00`
- Action: selected the close icon on the calculated-table refresh banner once
- Result: the same `需要手动刷新一个或多个计算表。` banner reappeared
- External-change banner: still not visible
- Refresh/save/close action: none
- Production operation count: open `1`, dismiss banner `1`, save `0`, refresh
  `0`, apply external changes `0`, close `0`, reopen `0`
- End state: Desktop remains open

## H-004 — Refresh calculated table once

- Recorded at: `2026-09-23T00:39:38.2352221-07:00`
- Action: selected `立即刷新` once
- Refresh completion indicator: none observed, so completion cannot be claimed
  directly
- Observable result: calculated-table banner disappeared
- External-change banner: did not appear
- Card remained: `Baseline Total`, value `60`
- Error or other prompt: none
- Save/close action: none
- Observed-run operation count: open `1`, dismiss banner `1`, refresh `1`, save
  `0`, apply external changes `0`, close `0`, reopen `0`
- End state: Desktop remains open

## H-005 — Post-refresh no-save retry observation

- Recorded at: `2026-09-23T00:44:06.6108145-07:00`
- Human action taken: none
- Waited after retry batch: several seconds
- External-change banner: did not appear
- Card remained: `Baseline Total`, value `60`
- Other prompt/error: none
- Desktop save state: no save performed in this experiment
- End state: Desktop remains open

## H-006 — First save in current Desktop session

- Recorded at: `2026-09-23T00:46:40.8727023-07:00`
- Action: saved once
- Result: save completed
- Prompt/error: none
- Visible state after save: `Baseline Total`, value `60`
- Desktop state: remains open
- Observed-run operation count: open `1`, dismiss banner `1`, refresh `1`, save
  `1`, apply external changes `0`, close `0`, reopen `0`
- Disk result: Desktop rewrote all 11 authored project files, restored its
  in-memory baseline over the ignored retry, added 3 trackable initialization
  files, and added 4 ignored `.pbi/` local-cache files

## H-007 — Post-save external detection observation

- Recorded at: `2026-09-23T00:56:05.1563304-07:00`
- Human action taken: none
- Waited after post-save batch: several seconds
- External-change banner: did not appear
- Visible state: `Baseline Total`, value `60`
- Other warning/error: none
- Disk target remained committed as: `Doubled Total`, value `120`
- End state: Desktop remains open

## H-008 — Initialization close

- Recorded at: `2026-09-23T00:59:15.5126211-07:00`
- Action: closed Power BI Desktop without an additional save
- Prompt/error: none
- Process verification: `PBIDesktop=0`, `msmdsrv=0`
- Disk verification: committed `Doubled Total / 120` batch hashes unchanged
- Observed-run operation count: open `1`, dismiss banner `1`, refresh `1`, save
  `1`, close `1`, apply external changes `0`, reopen `0`

## H-009 — Initialization reopen

- Recorded at: `2026-09-23T01:02:01.2683679-07:00`
- Action: reopened the same `MinimalWorkflow.pbip`
- Page: `Overview`
- Card: `Doubled Total`, value `120`
- Calculated-table refresh banner: none
- Warning/error/repair prompt: none
- End state: Desktop remains open
- Observed-run operation count: open `1`, dismiss banner `1`, refresh `1`, save
  `1`, close `1`, reopen `1`, apply external changes `0`

## H-010 — Reopened-instance external-change notification

- Recorded at: `2026-09-23T01:07:13.5870202-07:00`
- Human action taken: none
- Banner text: `This project's files were changed externally. Apply to view the latest changes.`
- Action offered: `Apply external changes`
- Visible pre-apply state: `Doubled Total`, value `120`
- Other warning/error: none
- End state: Desktop remains open; external change not yet applied
- Evidence: `evidence/screenshots/HG-02-external-change-banner.png`
