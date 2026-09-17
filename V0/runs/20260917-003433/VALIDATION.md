# V0 验收记录 — 20260917-003433

状态：阶段 1 仓库与种子准备已通过；MCP 能力闸门及 Power BI Demo 尚未执行。本记录只记载已核实事实，不代表 Demo 成功。

## 环境与基线

- 运行时间：2026-09-17，America/Los_Angeles。
- Power BI Desktop：Microsoft Store 安装包 `Microsoft.MicrosoftPowerBIDesktop`，版本 `2.157.1354.0`；复制种子时 Desktop 进程已退出。
- Modeling MCP：微软官方 `@microsoft/powerbi-modeling-mcp-win32-x64` `0.5.0-beta.13`；版本化安装在本机 `%LOCALAPPDATA%/Programs/PowerBIModelingMCP/0.5.0-beta.13/`，未纳入 Git。安装包按 npm SHA-512 完整性值校验，可执行文件微软签名有效，SHA-256 为 `8B5434688C0A5CBBE94928F0099F24C91886393A888AC35DCCED349B2F5A30F7`。
- Codex MCP 注册名：`powerbi-modeling-mcp`，STDIO 启动参数 `--start --require-confirmation`；未使用跳过确认参数。当前任务的工具目录尚未动态刷新，需在下一次会话检查原生工具是否可见。
- 需求基线提交：`f2aa331`。
- 种子提交：`c5f43c15aeef5f3c564ab980ae17b8a80bcfef5f`；种子 Git tree：`c5031c40f16f95350dae0f4a11a92d5e65251342`。
- 种子 `.pbip` SHA-256：`AF67AAF1A650845C67975103E6F2079E414A9E51BB841A097DC51AD518362FD9`。
- 运行项目：`V0/runs/20260917-003433/project/`；从 Git 已追踪种子文件复制，14 个文件逐一 SHA-256 一致，未带入 `.pbi` 本机状态。

## 种子检查

- `.pbip`、语义模型 TMDL、报告 PBIR `definition/` 均存在；`definition.pbir` 使用相对 `byPath` 引用。
- 报告仅有一个名为 `Overview` 的空白页面；尚无目标表、度量值或视觉对象。
- 用户已在 Desktop 取消当前文件 Auto date/time 并保存；磁盘 `model.tmdl` 中 `__PBI_TimeIntelligenceEnabled = 0`。按需求勘误，此两项构成主要证据，无需补拍截图。
- Desktop 原生项目文件保留其原始换行符；现有 `.gitattributes` 对 Power BI 文件不做文本转换，暂不需要修改。

## 阶段状态

| 阶段 | 状态 | 记录 |
| --- | --- | --- |
| 1. Git 回滚点、种子与运行副本 | 已通过 | 种子独立提交；运行副本逐文件一致；Auto date/time 证据已核对。 |
| 2. Modeling MCP 连接与能力矩阵 | 服务端预检通过，模型能力待测 | 官方服务端已注册；只读 MCP 初始化及 `tools/list` 成功，未连接 Desktop 模型。 |
| 3. 固定 CSV 与独立基准 | 待执行 | `expected-results.json` 尚未生成，避免虚假结果。 |
| 4–11. 建模、刷新、DAX、持久化、PBIR、Desktop 验收 | 待执行 | 未启动 Demo。 |

## 待补证据

- MCP 对运行副本 Desktop 模型的实际连接，以及各必要能力的操作和回读结果。
- 后续阶段的日志、数值比对、项目与 PBIR 校验、两次持久化回读、交互截图和人工视觉确认。

## MCP 服务端预检

- 包来源：微软发布的 npm Windows x64 平台包；固定版本 `0.5.0-beta.13`，未使用浮动 `latest`。
- 只读握手：`initialize` 协议 `2025-06-18` 成功；服务端自报版本 `0.5.0.0`；`tools/list` 返回 21 个工具组。
- 与 V0 对应的已声明入口：`connection_operations`、`model_operations`、`table_operations`、`column_operations`、`named_expression_operations`、`partition_operations`、`relationship_operations`、`measure_operations`、`dax_query_operations`、`database_operations`。
- 日期表属性、`sortByColumn`、`formatString`、刷新及保存后回读等是否在当前版本和 Desktop 目标上可实际执行，仍需后续逐项验证；工具组存在不等于能力通过。
- 当前任务未连接模型、未执行 DAX、未修改语义模型或 PBIR。

## 当前结论

确认种子与运行副本准备完成，MCP 服务端预检成功；完整 MCP 能力闸门及端到端结果尚未判定。下一步在原生工具可见后打开运行副本并逐项验证，未通过则按需求文档停止并记录。
