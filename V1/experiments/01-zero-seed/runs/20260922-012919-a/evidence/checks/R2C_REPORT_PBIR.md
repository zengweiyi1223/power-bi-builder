# R2c Report/PBIR — Run 20260922-012919-a

验证时间：`2026-09-22T01:57:15.8967363-07:00`

## Execute

R2b 复验通过后，仅新增 Report/PBIR 的五个必需/确定性文件：

- `ZeroSeedAlpha.Report/definition.pbir`
- `definition/version.json`
- `definition/report.json`
- `definition/pages/pages.json`
- `definition/pages/78c91ddf6ab57cf694f0/page.json`

页面 ID 由 `SHA-256("20260922-012919-a|ZeroSeedAlpha|Overview")` 的前 20 个小写十六进制字符独立生成；未读取或复制既有页面标识符。

## 公开依据

- Report folder / PBIR：Microsoft Learn `https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report`
- PBIR Schema 发布记录：Microsoft `json-schemas` `https://github.com/microsoft/json-schemas/tree/main/fabric/item/report`
- Schema 获取时间：`2026-09-22T01:52:33.6733194-07:00`

| 文件 | Schema | Schema SHA-256 |
| --- | --- | --- |
| `definition.pbir` | `definitionProperties/2.0.0` | `E46B78FCE6F2107A005F27ACCE1D12F7BD03714C1F0EA4B41E11B0720E478CC1` |
| `version.json` | `versionMetadata/1.0.0` | `2C77C510CB12E11F10172174422D0EFB1D4E97DA06B8D453B2ABDF81537E68B2` |
| `report.json` | `report/3.3.0` | `9F0B94A084D6C2E2CAC2F1EE0900FC7F8159AE4E2C308F108000636A6D6BB481` |
| `pages.json` | `pagesMetadata/1.1.0` | `AEE864CCFF93F1B2E072B5B3DCBD3DBB904380D1D51EA22941B3E2A87DA459F1` |
| `page.json` | `page/2.1.0` | `35C2F150882647855607CCE7ACD6B7166F7539F8614A1BF534DCED5FBA7699CC` |

`report.json` 使用 Schema 允许的最小 `themeCollection: {}`；未从项目模板复制 Desktop 特定主题或资源。Desktop 是否接受、初始化或补写该最小合法形态属于后续产品验证观察，不能由 Schema 验证预先声称。

## 立即 Verify

- 五个 JSON 文件均可解析并分别通过完整下载 Schema 的离线 Draft 7 验证。
- `definition.pbir` 版本为 `4.0`；`byPath` 使用正斜杠相对路径，解析后精确指向本 Run 的 `ZeroSeedAlpha.SemanticModel`，且未越出项目根。
- 唯一页面名和文件夹 ID 均为 `78c91ddf6ab57cf694f0`；显示名为 `Overview`。
- `pages.json` 的 `pageOrder` 和 `activePageName` 都精确引用该唯一页面。
- 页面 ID 符合 20 位小写十六进制约束；无 visual 文件夹。
- R2c 后项目恰有 9 个文件，全部位于精确项目根；`git diff --check` 通过。

## 项目文件哈希

- `definition.pbir`：`10F2D09523A92CEDEEB2A2A74D619983284BD75B387D599B32FB3C72DA97BC68`
- `version.json`：`0F9F217A60981BF882D7B1963977FC72CC051078DF8512B46CAA607AFF2E5220`
- `report.json`：`9AC7E731DC8035B5A9E34207562C54C4EE38C5D45EAF8CA6D4E88C4A2CDE087D`
- `pages.json`：`816DDDFEEC5741B844FD92317A83F7B56EE01541CC07781F84017376BF873A06`
- `page.json`：`570C3ECB47E917AAA0225170E354A54E77951CF6AD6D3A67B542324889BB6B96`

R2c Gate：`Passed`。
