# R5 First Reopen and Read-only MCP — Run 20260922-012919-a

验证完成时间：`2026-09-22T02:49:44.1053818-07:00`

## Human 重开观察

Human 从同一绝对路径重新打开 `ZeroSeedAlpha.pbip`，未保存、未修改、未另存为。

- 成功进入报表界面。
- `Overview` 空白页面仍可见。
- 窗口标题仍为 `ZeroSeedAlpha`。
- 没有弹窗、警告、错误或修复提示。

## 重开后磁盘稳定性

- Manifest：`manifests/POST_REOPEN_NO_SAVE.json`
- 文件数：`15`
- 总字节数：`3643`
- 相对 `POST_SAVE_CLOSED.json`：Added `0`、Modified `0`、Deleted `0`
- MCP 连接、只读回读并断开后再次比较：Added `0`、Modified `0`、Deleted `0`
- Desktop/模型进程保持运行；没有保存动作。

## Modeling MCP 只读回读

完整分离日志：`logs/MCP_ACTIONS.jsonl`。仅执行发现、连接、读取和断开；没有 Create、Update、Delete、Refresh、Import、Export、Transaction 或 Trace 操作。

- 本机实例：1 个；父窗口标题 `ZeroSeedAlpha`。
- 连接：本机 Desktop，会话无 transaction、无 trace；完成后连接数为 0。
- 数据库：1 个 Tabular 模型，compatibility level `1606`，language `1033`，状态 `Unprocessed`（空模型无数据处理）。
- 模型：`Model`；culture `en-US`；default mode `Import`；`PowerBI_V3`；`PBI_ProTooling=["DevMode"]`；运行时报告为空模型。
- 表：`0`。

MCP 结果与磁盘 TMDL 和 Human UI 观察一致：项目身份正确、模型为空、没有意外表或业务对象。

## 对 R4 差异的影响

- R5 证明 Desktop 保存后的 15 文件状态可从同一路径无提示稳定重开。
- R5 以真实产品行为缓解 `EVT-003` 对功能兼容性的担忧，但不消除公开 Schema 与 Desktop 去除 `$schema` 的规范证据缺口。
- 首开在两个 `.platform` 不存在时已成功；重开在 Desktop 已生成它们后成功。该证据不能证明删除 `.platform` 后的反事实重开，因此不把它们宣称为后续持久化必需，也不执行破坏现场的消融试验。

## 核心往返判定

- 直接首开：Passed。
- 显式保存/关闭：Passed。
- 同一路径第一次重开：Passed。
- 首开未保存磁盘差异：0。
- 重开未保存磁盘差异：0。
- 首存变化：全部归为 `CACHE_LOCAL`、`SERIALIZATION_EQUIVALENT`、`DEFAULT_ENRICHMENT` 或 `VERSION_UPGRADE`；没有已证实的 `STRUCTURAL_REQUIRED`、`SEMANTIC_CHANGE` 或 `UNKNOWN`。

Run A 当前功能候选：`完全零种子（带 Desktop 正常保存规范化）`。这不是 V1 最终结论；仍须执行 R-VLD-003 的 Playbook-only 最终往返、完成 Run B 独立重复，并保留 `.platform` 反事实未验证限制。

R5 Gate：`Passed`。可以请求 HG-04 执行额外最终往返；该额外往返只用于评价 Provisional Rule R-VLD-003 的成本和价值，不属于核心功能验收。
