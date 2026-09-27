# R2c Report/PBIR — Run 20260922-032410-b

验证时间：`2026-09-22T06:48:57.0921158-07:00`

## Execute

R2b 通过后，仅新增五个 Report/PBIR 文件：

- `零种子 Beta.Report/definition.pbir`
- `definition/version.json`
- `definition/report.json`
- `definition/pages/pages.json`
- `definition/pages/ee10ab53292bad27c265/page.json`

页面 ID 为 `SHA-256("20260922-032410-b|零种子 Beta|Overview")` 的前 20 个小写十六进制字符：`ee10ab53292bad27c265`。未读取、复制或改名其他 Run 页面标识符。

## 公开 Schema 与哈希

| 文件 | Schema 版本 | Schema SHA-256 | 文件 SHA-256 |
| --- | --- | --- | --- |
| `definition.pbir` | `definitionProperties/2.0.0` | `E46B78FCE6F2107A005F27ACCE1D12F7BD03714C1F0EA4B41E11B0720E478CC1` | `B53E9584497DD473EAF10F3A993591F160BCE6DDA935FF1E6441622342A4DF90` |
| `version.json` | `versionMetadata/1.0.0` | `2C77C510CB12E11F10172174422D0EFB1D4E97DA06B8D453B2ABDF81537E68B2` | `0F9F217A60981BF882D7B1963977FC72CC051078DF8512B46CAA607AFF2E5220` |
| `report.json` | `report/3.3.0` | `9F0B94A084D6C2E2CAC2F1EE0900FC7F8159AE4E2C308F108000636A6D6BB481` | `9AC7E731DC8035B5A9E34207562C54C4EE38C5D45EAF8CA6D4E88C4A2CDE087D` |
| `pages.json` | `pagesMetadata/1.1.0` | `AEE864CCFF93F1B2E072B5B3DCBD3DBB904380D1D51EA22941B3E2A87DA459F1` | `DB1F217277B612A5CF76D3D23831E3A1F7846BF4D6AB7C334EFD815E8D37F200` |
| `page.json` | `page/2.1.0` | `35C2F150882647855607CCE7ACD6B7166F7539F8614A1BF534DCED5FBA7699CC` | `650D58F8C6D6F7ED23B4FFCF30FEBCBCF00D5789EDCEBA618C029078606296DD` |

## 立即 Verify

- 五个 JSON：解析与完整公开 Draft 7 Schema 均 Passed
- PBIR：`version: 4.0`；`byPath: ../零种子 Beta.SemanticModel`
- `byPath` 解析后精确指向本 Run SemanticModel，且不越出项目根
- 页面：唯一 `Overview`；目录名、`name`、`pageOrder`、`activePageName` 一致
- 页面 ID：20 位小写十六进制，且与本 Run 独立派生值一致
- 无 visual 目录
- 项目递归文件数：`9`
- Desktop / 模型进程：`0`

R2c Gate：`Passed`。
