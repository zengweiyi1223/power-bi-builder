# HG-02C one apply result

Result: **REPORT-ONLY HOT PASS**

The human selected `Apply external changes` exactly once. Desktop then showed:

- card title: `Tripled Total` — report/PBIR change applied;
- card value: `120` — semantic-model/TMDL change did not apply;
- external-change banner: cleared;
- calculated-table banner: absent;
- warning, error, overwrite, or repair prompt: none.

The expected value was `180` because the committed measure is
`SUM('Sales'[Amount]) * 3`. The retained value `120` proves the running semantic
model still used the prior `* 2` definition. This is not a full combined hot
reload; it exactly matches the predefined `Report-only hot pass` outcome.

Screenshot SHA-256:
`ACBD9FA2127C124461DA87DADE5E75022619A5E9663DA23B831F4ACA977CF15C`.
