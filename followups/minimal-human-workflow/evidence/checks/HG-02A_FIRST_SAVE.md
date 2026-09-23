# HG-02A first save

Result: **PASS — DESKTOP INITIALIZATION OBSERVED**

The human saved once with Desktop open. No prompt or error appeared and the
visible state remained `Baseline Total / 60`.

Read-only inspection immediately after save found:

- all 11 Codex-authored project files were rewritten or normalized;
- the ignored `Tripled Total / 180` retry was overwritten by Desktop's
  in-memory `Baseline Total / 60` state;
- semantic lineage tags were generated;
- report and semantic-model `.platform` files were generated;
- `diagramLayout.json` was generated;
- four `.pbi/` machine-local files were generated and remain Git-ignored.

Repository `.gitattributes` intentionally marks `.pbip`, `.pbir`, `.pbism`, and
`.tmdl` as `-text !eol` to preserve Desktop source bytes. Consequently,
`git diff --check` describes Desktop CRLF bytes as trailing whitespace for these
rewritten files. They are retained unchanged; JSON parsing, file manifests, and
SHA-256 checks are the applicable validations for this checkpoint.

The save therefore acts as a real Desktop initialization and ownership
boundary. No claim is made that saving alone enables external-change detection;
that requires a new post-save batch.
