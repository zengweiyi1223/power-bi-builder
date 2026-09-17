# V0 验收记录 — 20260917-003433

状态：阶段 1–3 已通过；MCP 建模、刷新与 Power BI Demo 验收尚未执行。本记录只记载已核实事实，不代表 Demo 成功。

## 环境与基线

- 运行时间：2026-09-17，America/Los_Angeles。
- Power BI Desktop：Microsoft Store 安装包 `Microsoft.MicrosoftPowerBIDesktop`，版本 `2.157.1354.0`；复制种子时 Desktop 进程已退出。
- Modeling MCP：微软官方 `@microsoft/powerbi-modeling-mcp-win32-x64` `0.5.0-beta.13`；版本化安装在本机 `%LOCALAPPDATA%/Programs/PowerBIModelingMCP/0.5.0-beta.13/`，未纳入 Git。安装包按 npm SHA-512 完整性值校验，可执行文件微软签名有效，SHA-256 为 `8B5434688C0A5CBBE94928F0099F24C91886393A888AC35DCCED349B2F5A30F7`。
- Codex MCP 注册名：`powerbi-modeling-mcp`，STDIO 启动参数 `--start --require-confirmation`；未使用跳过确认参数。重启 Codex 后，当前任务已能原生调用该服务端工具。
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
| 2. Modeling MCP 连接与能力矩阵 | 可用性预检通过 | 原生工具可见；已连接运行副本并回读空白模型。实际写入、刷新及 DAX 在对应阶段验证，失败即停。 |
| 3. 固定 CSV 与独立基准 | 已通过 | 固定 15 行 CSV、独立 Python 脚本和本次运行的预期结果已生成并核对。 |
| 4–11. 建模、刷新、DAX、持久化、PBIR、Desktop 验收 | 待执行 | 未启动 Demo。 |

## 待补证据

- 各必要 MCP 写入、刷新及 DAX 能力的实际操作和回读结果。
- 后续阶段的日志、数值比对、项目与 PBIR 校验、两次持久化回读、交互截图和人工视觉确认。

## MCP 服务端预检

- 包来源：微软发布的 npm Windows x64 平台包；固定版本 `0.5.0-beta.13`，未使用浮动 `latest`。
- 只读握手：`initialize` 协议 `2025-06-18` 成功；服务端自报版本 `0.5.0.0`；`tools/list` 返回 21 个工具组。
- 与 V0 对应的已声明入口：`connection_operations`、`model_operations`、`table_operations`、`column_operations`、`named_expression_operations`、`partition_operations`、`relationship_operations`、`measure_operations`、`dax_query_operations`、`database_operations`。
- 重启后上述原生 MCP 工具已在当前 Codex 任务中出现，`Help` 调用成功；静态接口包含 `MarkAsDateTable`、列 `sortByColumn`、度量值 `formatString`、刷新、关系及 DAX 操作。
- `ListLocalInstances` 返回 0 个实例；检查时 Desktop 保持关闭，未建立模型连接。
- 日期表属性、`sortByColumn`、`formatString`、刷新及保存后回读等是否在当前版本和 Desktop 目标上可实际执行，仍需后续逐项验证；工具组存在不等于能力通过。
- 本次预检未执行 DAX、未修改语义模型或 PBIR。

## Desktop 运行副本只读连接

- 用户打开的 Desktop 进程启动参数指向 `V0/runs/20260917-003433/project/PowerBIBuilderV0Seed.pbip`，不是 `V0/seed/` 原件。
- MCP 发现本地实例 `localhost:51759`，成功建立连接 `PBIDesktop-PowerBIBuilderV0Seed-51759`。
- MCP `Get` 回读模型 `Model`，注释 `__PBI_TimeIntelligenceEnabled = 0`；表、关系、度量值、Named Expression、Partition 的 `List` 结果均为 0。
- Desktop 打开后，Git 检查未发现种子或运行副本已追踪文件的变更。
- 能力矩阵判定：连接、原生工具调用及只读对象回读已实测通过；M/Partition 创建、关系、度量值、日期表标记、列排序、格式、刷新和 DAX 已在当前工具接口中声明，实际操作留待后续相应阶段验收。

## 固定数据与独立基准

- `V0/data/sales.csv` 为固定 UTF-8、逗号分隔测试数据，共 15 行、5 个产品、4 个品类，覆盖 2026-01 至 2026-04；`Technology` 用于交互验证，`ZeroSales` 中仅有合法的零销量行，用于检验毛利率 `BLANK`。
- CSV SHA-256：`1bec90ec71d15f74b28ae3389b44df4e34a24f8b8e960de4db28231646cb826c`。后续运行共用该文件，不随机生成或覆盖。
- `V0/scripts/calc_expected.py` 使用 Python 标准库直接读取 CSV，以 `Decimal` 汇总行级金额，验证字段、日期、产品键映射及日期-产品粒度，不调用 Power BI/DAX。输出为本运行的 `expected-results.json`。
- 独立总计：销售额 `9356.75`、销量 `74`、成本 `6344.80`、毛利额 `3011.95`、毛利率 `0.3219013011996687`。月度销售额和品类销售额分别汇总到总计；`ZeroSales` 销售额为 `0`，毛利率为 `null`，对应 DAX `BLANK`。
- 这些数值是待与 MCP DAX 查询比较的基准，尚不能证明模型或报表正确。

## 当前结论

确认种子与运行副本准备完成，MCP 连接及可用性预检通过，固定 CSV 与独立基准已生成；写入、刷新、DAX 和端到端结果尚未判定。下一步逐项验证 MCP 实际操作；任一必要能力失败即停。
