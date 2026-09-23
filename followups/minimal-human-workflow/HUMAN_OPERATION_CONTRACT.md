# Human operation contract

## Production target

| Operation | Target count |
| --- | ---: |
| Open Desktop project | 1 |
| Save | 0 |
| Apply external changes | 1 |
| Close | 1 |
| Reopen | 0 |

Target production sequence:

`Open -> verify baseline -> Apply external changes -> verify final -> Close`

The human performs no modeling, file editing, visual creation, field binding, or
format authoring.

## Validation-only operations

After the production close, the experiment allows one reopen and one final close
solely to prove persistence. These two actions must be reported separately and
must not be counted as production requirements.

## Stop behavior

- On any warning that unsaved Desktop work will be overwritten, do not confirm.
- On any error or repair prompt, capture complete text and buttons and stop.
- Do not save unless the experiment explicitly changes the contract after
  preserving the failed state and recording a deviation.

