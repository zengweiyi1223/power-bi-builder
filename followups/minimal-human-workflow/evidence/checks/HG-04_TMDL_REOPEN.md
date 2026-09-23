# HG-04 TMDL reload by reopen

Result: **PASS**

After one external apply produced the report-only state `Tripled Total / 120`,
the human closed Desktop without saving and reopened the same PBIP. The reopened
project showed:

- page: `Overview`;
- card title: `Tripled Total`;
- card value: `180`;
- calculated-table or external-change banner: none;
- warning, error, or repair prompt: none.

This proves the committed TMDL expression was valid and loaded on restart. The
contrast with the immediately preceding one-apply screenshot attributes the
value transition specifically to semantic-model reload during reopen.

Screenshot SHA-256:
`38A7448DBBE566EF13F45AB2E5F6426E5D4F3558E09B36662B836FEB5A9338B9`.
