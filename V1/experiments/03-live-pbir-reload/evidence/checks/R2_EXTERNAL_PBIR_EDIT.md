# R2 external PBIR edit

Result: **STATIC PASS; DESKTOP APPLICATION PENDING**

- Desktop remained open (`PBIDesktop=1`, `msmdsrv=1`).
- Explicit pre-edit save: `no`, by controlled deviation `DEV-001`.
- Project diff from pre-open baseline: one added `visual.json`, zero modified,
  zero removed files.
- Visual type: `textbox`
- Text: `Live PBIR reload succeeded`
- Visual name matches its folder name.
- Position is within the `1280 x 720` page canvas.
- JSON parsing: pass
- SHA-256: `573174FB51A8B65517C9AB93BCEE7E8F7D6D3CF394B1541B4006F9B25733F290`

This check does not claim that Desktop detected, accepted, or rendered the file.
Those claims require HG-03 and R3 human evidence.

