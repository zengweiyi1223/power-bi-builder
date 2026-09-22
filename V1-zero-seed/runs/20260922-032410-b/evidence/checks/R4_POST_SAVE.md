# R4 First Save and Close — Run 20260922-032410-b

验证完成时间：`2026-09-22T07:48:51.6375213-07:00`

## Human 与进程

- Human 确认保存成功、Desktop 正常关闭，无任何提示或错误。
- `PBIDesktop` / `msmdsrv`：`0`。
- 未另存为、未修改报表内容、未接受修复。

## 磁盘结果

- Manifest：`manifests/POST_SAVE_CLOSED.json`
- 文件数：`15`
- 总字节数：`3647`
- 相对 pre-open/首开未保存：Added `6`、Modified `9`、Deleted `0`
- Unicode 项目名、父目录空格、PBIP→Report 与 PBIR→SemanticModel 引用均保留。

## 新增文件分类

| 文件 | 分类 | 说明 |
| --- | --- | --- |
| Report `.pbi/localSettings.json` | `CACHE_LOCAL` | 本地缓存；Git ignored；manifest 保留哈希 |
| SemanticModel `.pbi/editorSettings.json` | `CACHE_LOCAL` | 本地编辑器缓存；Git ignored |
| SemanticModel `.pbi/localSettings.json` | `CACHE_LOCAL` | 本地缓存；Git ignored |
| Report `.platform` | `DEFAULT_ENRICHMENT` | `Report` / `零种子 Beta` 身份与新 logicalId |
| SemanticModel `.platform` | `DEFAULT_ENRICHMENT` | `SemanticModel` / `零种子 Beta` 身份与新 logicalId |
| `diagramLayout.json` | `DEFAULT_ENRICHMENT` | 空模型图布局；无表节点 |

两个 `.platform` 均通过微软 `platformProperties/2.0.0` 完整 Schema；Schema SHA-256 为 `8D12DAA644F6E8F44E4CCC6788E29A40A2A2ECAD1A96BE91E77330ED7C8A4453`。

## 改写文件分类

| 文件 | 观察 | 分类 |
| --- | --- | --- |
| 根 `.pbip` | 移除 `$schema`；增加空 `settings`；CRLF/EOF 规范化 | `SERIALIZATION_EQUIVALENT` + `DEFAULT_ENRICHMENT` |
| `definition.pbir` | 移除 `$schema`；路径与 4.0 保持；CRLF/EOF | `SERIALIZATION_EQUIVALENT` |
| `page.json` / `pages.json` / `version.json` | 内容不变，仅行尾/EOF | `SERIALIZATION_EQUIVALENT` |
| `report.json` | 增加 `settings.useEnhancedTooltips: false` | `DEFAULT_ENRICHMENT` |
| `definition.pbism` | 移除 `$schema`；4.0→4.2；增加空 `settings` | `VERSION_UPGRADE` + `DEFAULT_ENRICHMENT` |
| `database.tmdl` | 去除显示名；1600→1606 | `SERIALIZATION_EQUIVALENT` + `VERSION_UPGRADE` |
| `model.tmdl` | 保留 `powerBI_V3`；增加 `PBI_ProTooling=["DevMode"]` | `DEFAULT_ENRICHMENT` |

## 静态与 Schema 复验

- 15 个磁盘文件与 manifest 路径、字节和 SHA-256 完全一致。
- 全部 JSON 可解析；6 个仍声明 Schema 的文件直接通过完整 Schema。
- 根 `.pbip`、`definition.pbir`、`definition.pbism` 因 Desktop 移除 `$schema`，直接验证均只在 required `$schema` 处失败；在内存恢复各自原 URL 后其余结构完整通过。
- TMDL canonical 子集：`compatibilityLevel: 1606`、`culture: en-US`、`powerBI_V3`、`PBI_ProTooling` 全部通过。
- 无未解释结构/语义变化；允许进入首次重开。

## 事件与跨 Run 观察

- `EVT-B005`：首次 R4 校验脚本未归一化 CRLF 且错误分支分词错误；项目未变，修正后全量重跑通过。
- `EVT-B006`：三个根文件的公开 Schema/Product 缺口，Non-blocking。
- `EVT-B007`：Desktop 首次显式保存的预期规范化，Informational。
- 与 Run A 相同的文件类别发生相同方向的变化；Run B 的 `.platform` 显示名和 logicalId 为独立值。

R4 Gate：`Passed with known evidence gap`。
