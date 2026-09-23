# HG-02B external-change banner after initialization restart

Result: **PASS — ACTION SURFACED**

After the project had been saved, closed, and reopened, Codex modified the same
existing TMDL measure and PBIR card title while Desktop remained open. Desktop
showed:

> This project's files were changed externally. Apply to view the latest changes.

The available action was `Apply external changes`. The pre-apply visual state
remained `Doubled Total / 120`, with no other warning or error. This proves the
external-change notification boundary is the initialization restart, not first
save alone, for this generated project and installed Desktop build.

Screenshot SHA-256:
`75A2D86AB1F5E6E0990212016F119EEF7BC70A0367D550CC964D54F563AC3264`.
