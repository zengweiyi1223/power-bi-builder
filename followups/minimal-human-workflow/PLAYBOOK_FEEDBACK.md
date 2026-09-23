# Playbook feedback

This file records observations and suggestions only. It does not modify
Playbook v0.1.

## Observations

1. Lifecycle state mattered more than file existence. External edits were not
   detected before first save, nor immediately after first save in the same
   Desktop process. Detection began after save plus close—reopen.
2. `Apply external changes` had different utility by layer: the existing PBIR
   visual reloaded, while the TMDL measure remained at its prior in-memory
   definition until restart.
3. Desktop first save was materially destructive to ignored external edits: it
   restored in-memory content and added lineage/platform metadata.
4. A calculated-table test fixture introduced a persistent manual-refresh
   banner that obscured the external-change gate until refreshed.

## Impact

A generic instruction to “keep Desktop open and apply external changes” is not
sufficient for minimum-operation planning. It must state:

- whether Desktop has completed an initialization save and restart;
- whether the batch is PBIR-only or includes TMDL;
- whether the target object already exists and is loaded;
- whether Desktop has stale or unsaved in-memory state;
- whether refresh prompts originate from the test fixture or the real source.

## Suggestions for a future Playbook revision

- Split external-edit guidance into PBIR-only and TMDL-containing paths.
- Treat first Desktop save as an overwrite-risk Human Gate with a preceding Git
  checkpoint and a post-save file manifest.
- Make save-plus-restart an explicit initialization state transition for PBIR
  live reload until broader evidence shows it can be omitted.
- For a TMDL-containing batch, recommend close—reopen as the default verified
  acceptance path; do not require a redundant apply click first.
- Label fixture-driven refresh gates separately from production data-source
  gates so diagnostic setup does not inflate the claimed human workflow.

## Rule conformity versus utility

- Conformity: Execute—Verify steps, Human Gates, separate actor logs, blocking
  attribution, Git checkpoints, and frozen-scope checks were followed.
- Utility: the checkpoints immediately before first save and external batches
  were high value because Desktop overwrote valid on-disk edits without a
  prompt. Separate actor logs made the overwrite and reload boundaries clear.
- Cost: recording every failed notification state produced substantial evidence
  volume. A future template could keep the same safety while using a compact
  state-transition table for repeated no-action observations.
