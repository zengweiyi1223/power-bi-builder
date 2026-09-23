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

None recorded.

