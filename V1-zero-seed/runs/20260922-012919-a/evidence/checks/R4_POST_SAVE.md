# R4 First Save and Close — Run 20260922-012919-a

验证完成时间：`2026-09-22T02:38:29.8352144-07:00`

## Human 观察与进程退出

- Human 确认显式保存成功。
- Human 确认正常关闭 Desktop。
- 没有弹窗、警告或错误。
- 复核时 `PBIDesktop` 与 `msmdsrv` 进程数均为 `0`。
- 未执行另存为、改名、修复或手工文件编辑。

## 首存 manifest

- 文件：`manifests/POST_SAVE_CLOSED.json`
- SHA-256：`DA9A669E19529BE7FC580961E53836173E7E20F44456A966715CE5A4DDF525CE`
- 文件数：`15`（首开前/首开未保存均为 `9`）
- 总字节数：`3643`
- 相对 `PRE_OPEN.json`：Added `6`、Modified `9`、Deleted `0`
- 相对 `POST_OPEN_NO_SAVE.json`：Added `6`、Modified `9`、Deleted `0`

首开未保存阶段差异为 0，因此以下全部变化可精确归于 Human 显式保存和 Desktop 关闭阶段。

## 新增文件分类

| 路径 | 内容摘要 | 分类 | 项目必需性 |
| --- | --- | --- | --- |
| `ZeroSeedAlpha.Report/.pbi/localSettings.json` | 本地版本与安全绑定签名 | `CACHE_LOCAL` | 否；被仓库 `.gitignore` 排除 |
| `ZeroSeedAlpha.SemanticModel/.pbi/editorSettings.json` | 本地编辑器默认选项 | `CACHE_LOCAL` | 否；被仓库 `.gitignore` 排除 |
| `ZeroSeedAlpha.SemanticModel/.pbi/localSettings.json` | 本地版本、用户同意和安全绑定签名 | `CACHE_LOCAL` | 否；被仓库 `.gitignore` 排除 |
| `ZeroSeedAlpha.Report/.platform` | Report 类型、显示名、逻辑 ID | `DEFAULT_ENRICHMENT` | 首开不需要；后续持久化必要性待 R5 |
| `ZeroSeedAlpha.SemanticModel/.platform` | SemanticModel 类型、显示名、逻辑 ID | `DEFAULT_ENRICHMENT` | 首开不需要；后续持久化必要性待 R5 |
| `ZeroSeedAlpha.SemanticModel/diagramLayout.json` | 空模型的默认“所有表”图布局 | `DEFAULT_ENRICHMENT` | 否；公开文档列为可选 Desktop 管理元数据 |

两个 `.platform` 均通过微软公开 `platformProperties/2.0.0` Draft 7 Schema；Schema 获取时间 `2026-09-22T02:35:31.3748099-07:00`，SHA-256 `8D12DAA644F6E8F44E4CCC6788E29A40A2A2ECAD1A96BE91E77330ED7C8A4453`。

## 改写文件分类

| 路径 | 原始差异摘要 | 分类 | 结构/语义解释 |
| --- | --- | --- | --- |
| `ZeroSeedAlpha.pbip` | 移除 `$schema`；增加空 `settings`；LF 改 CRLF、移除末尾换行 | `SERIALIZATION_EQUIVALENT` + `DEFAULT_ENRICHMENT` | Report 引用不变 |
| `ZeroSeedAlpha.Report/definition.pbir` | 移除 `$schema`；CRLF/末尾换行规范化 | `SERIALIZATION_EQUIVALENT` | `version` 与 `byPath` 不变 |
| `.../page.json` | 仅 CRLF/末尾换行规范化 | `SERIALIZATION_EQUIVALENT` | 页面 ID、名称、尺寸不变 |
| `.../pages.json` | 仅 CRLF/末尾换行规范化 | `SERIALIZATION_EQUIVALENT` | 页面顺序和活动页面不变 |
| `.../report.json` | 增加 `settings.useEnhancedTooltips: false`；换行规范化 | `DEFAULT_ENRICHMENT` | 无视觉、过滤或绑定变化 |
| `.../version.json` | 仅 CRLF/末尾换行规范化 | `SERIALIZATION_EQUIVALENT` | 仍为 `2.0.0` |
| `.../definition.pbism` | `4.0` 升至 `4.2`；增加空 `settings`；移除 `$schema` | `VERSION_UPGRADE` + `DEFAULT_ENRICHMENT` | TMDL 模式保持不变 |
| `.../database.tmdl` | 去除数据库显示名；兼容级别 `1600` 升至 `1606`；Desktop 换行 | `VERSION_UPGRADE` + `SERIALIZATION_EQUIVALENT` | 空数据库仍可解析；无表或数据语义 |
| `.../model.tmdl` | 增加 `PBI_ProTooling = ["DevMode"]`；Desktop 换行 | `DEFAULT_ENRICHMENT` | culture 与 `powerBI_V3` 不变 |

没有文件被归为 `SEMANTIC_CHANGE`、`STRUCTURAL_REQUIRED` 或 `UNKNOWN`。两个 `.platform` 的后续必要性明确延迟到重开证据，不提前声称。

## 独立复验

- 所有 13 个 JSON 文件均可解析；两份 TMDL 可按 Desktop 保存后的合法最小形态解析。
- PBIP Report 引用、PBIR `byPath`、唯一 `Overview` 页面、页面顺序和活动页面均保持不变。
- `diagramLayout.json` 为 `1.1.0`、一个空节点图；无业务模型对象。
- 两个 `.platform` 完整 Schema 验证通过。
- 保留 `$schema` 的四个原始 PBIR 文件直接通过公开 Schema。
- Desktop 从根 `.pbip`、`definition.pbir`、`definition.pbism` 移除了公开 Schema 要求的 `$schema`，故直接 Schema 验证只在这三个文件失败；把各自原始 Schema URL 仅在内存中补回后，其余结构完整通过。记录为 `EVT-003`，不改写 Desktop 现场。
- Desktop 使用 CRLF 且在 TMDL 末尾保留空行；标准 `git diff --check` 会将其报告为 whitespace，使用只在检查时声明 `cr-at-eol,-blank-at-eof` 的 Desktop 格式感知检查通过。项目文件保持 Desktop 原样。

## 判定

- R4 功能 Gate：`Passed with known non-blocking evidence gap`。
- 当前候选：Codex 项目无需人工建壳即可首开和首存；Desktop 在显式保存时进行了默认补充、版本升级和序列化规范化。
- 尚不能判定“完全零种子”或“Desktop 首次补写”，因为两个 `.platform` 对稳定重开的必要性和实际重开结果仍待 R5。

可以请求 HG-03；在 Human 明确执行前禁止重开或连接 MCP。
