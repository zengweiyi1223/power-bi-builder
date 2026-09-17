# V0 验收记录 — 20260917-003433

状态：阶段 1–11 已通过；V0 Demo 完整成功。已知校验限制见文末。

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
| 2. Modeling MCP 连接与能力矩阵 | 已通过 | 官方 MCP 已连接 Desktop 本地模型；建模、刷新、属性修改、回读和 DAX 均在后续阶段实测通过。 |
| 3. 固定 CSV 与独立基准 | 已通过 | 固定 15 行 CSV、独立 Python 脚本和本次运行的预期结果已生成并核对。 |
| 4. M/Partition 创建和数据刷新 | 已通过 | 3 个 Import/M Partition 均为 Ready，行数为 15、5、88。 |
| 5. 模型、关系、属性与度量值回读 | 已通过 | 3 表、2 条活动单向关系、5 个度量值及关键属性均已回读。 |
| 6. DAX 与独立基准对比 | 已通过 | 总计、4 个月、4 个品类、Technology 和零分母场景均一致。 |
| 7. 模型持久化闸门 | 已通过 | 重开运行副本后，MCP 对象和属性回读及代表性 DAX 均通过；执行者已再次关闭 Desktop。 |
| 8. PBIR 生成与离线校验 | 已通过 | 唯一 Overview 页含 6 个视觉对象；项目入口、官方 JSON Schema、布局、字段绑定及交互配置均通过预检，随后在 Desktop 实际渲染。 |
| 9. Desktop 打开、渲染与交互 | 已通过 | 无错误或自动修复提示；Technology 筛选与基准一致，清除后恢复；执行者确认页面清晰可读。 |
| 10. Desktop 保存、关闭和重开 | 已通过 | 保存关闭无提示；磁盘差异无业务语义漂移；重开无错误/自动修复，六个视觉对象及未筛选 KPI 正常。 |
| 11. 最终持久化回读 | 已通过 | 新 MCP 连接回读 3 表、2 关系、3 个 Ready 分区、5 度量值及关键属性；代表性 DAX 与独立基准一致。 |

## 关键验收证据

- 固定输入与独立基准：`V0/data/sales.csv`、本运行的 `expected-results.json`。
- 保存前、保存后快照：Git 提交 `535a0c7`、`c7a4579`；`git diff 535a0c7 c7a4579 -- V0/runs/20260917-003433/project/` 可复查原始差异。
- Desktop 视觉/交互：`evidence/overview-unfiltered.png`、`evidence/overview-technology.png`，以及执行者的清除筛选和最终重开确认。
- 最终模型与查询：`logs/final-mcp-readback.json`。

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
- 能力矩阵预检时：连接、原生工具调用及只读对象回读已实测通过；M/Partition 创建、关系、度量值、日期表标记、列排序、格式、刷新和 DAX 在当时留待相应阶段验证，现均已通过。

## 固定数据与独立基准

- `V0/data/sales.csv` 为固定 UTF-8、逗号分隔测试数据，共 15 行、5 个产品、4 个品类，覆盖 2026-01 至 2026-04；`Technology` 用于交互验证，`ZeroSales` 中仅有合法的零销量行，用于检验毛利率 `BLANK`。
- CSV SHA-256：`1bec90ec71d15f74b28ae3389b44df4e34a24f8b8e960de4db28231646cb826c`。后续运行共用该文件，不随机生成或覆盖。
- `V0/scripts/calc_expected.py` 使用 Python 标准库直接读取 CSV，以 `Decimal` 汇总行级金额，验证字段、日期、产品键映射及日期-产品粒度，不调用 Power BI/DAX。输出为本运行的 `expected-results.json`。
- 独立总计：销售额 `9356.75`、销量 `74`、成本 `6344.80`、毛利额 `3011.95`、毛利率 `0.3219013011996687`。月度销售额和品类销售额分别汇总到总计；`ZeroSales` 销售额为 `0`，毛利率为 `null`，对应 DAX `BLANK`。
- 这些数值是待与 MCP DAX 查询比较的基准，尚不能证明模型或报表正确。

## MCP 建模、刷新和数值验证

- 连接目标始终是运行副本的 Desktop 本地模型 `localhost:51759`；未连接离线 PBIP，也未直接编辑 TMDL。
- MCP 创建 `DataFilePath` Power Query 参数，值为当前环境的 `E:\AIWorkspace\01_Projects\power-bi-builder\V0\data\sales.csv`；共享 M 表达式 `SalesSource` 显式指定 UTF-8、逗号分隔、7 列、`en-US` 类型转换。两者经 MCP `Get` 回读。
- MCP 创建 `FactSales`（`SalesSource`）、`DimProduct`（源表投影去重）及 `DimDate`（源数据日期最小至最大值的连续日期，并派生 `Year`、`MonthNumber`、英文 `MonthName`、`YearMonth`）。每表有一个 Import/M Partition。刷新接口的单次调用实际只处理首个表，故对另外两表逐表刷新；最终三者均为 `Ready`。
- DAX 行数检查：`FactSales=15`、`DimProduct=5`、`DimDate=88`；维度唯一键数分别为 5 和 88，事实键未发现孤儿值。三表包含 MCP/引擎自动生成的隐藏 `RowNumber-*` 内部列，不作为业务 Schema。
- MCP 回读两条活动、多对一、单向关系：`FactSales[SaleDate] → DimDate[Date]` 和 `FactSales[ProductKey] → DimProduct[ProductKey]`。`DimDate` 的 `dataCategory=Time`；`MonthName.sortByColumn=MonthNumber`。五个度量值的精确名称、表达式和格式字符串均与需求契约一致。
- 建立关系后首次月度 DAX 提示关系需要重新计算；通过 MCP 对三个 Partition 执行标准 `Calculate` 后查询成功。此过程未修改 CSV、需求或模型定义，也未绕过 MCP。
- DAX 对比独立基准：总计销售额 `9356.75`、销量 `74`、成本 `6344.80`、毛利额 `3011.95`、毛利率 `0.3219013011996687`；4 个月和 4 个品类的销售额/毛利额逐项一致；`Technology` 五项结果一致；`ZeroSales` 毛利率为 `null`，即 DAX `BLANK`。金额、销量、比率均在规定容差内。
- 以上仅证明当前 Desktop 运行中模型；尚未验证磁盘持久化。

## 模型持久化闸门：重开前磁盘检查

- 执行者在运行副本的 Desktop 点击“保存”并关闭；关闭时没有再次出现保存提示。检查时未发现 `PBIDesktop` 或 `msmdsrv` 进程。
- 磁盘 TMDL 出现 `expressions.tmdl`、`relationships.tmdl` 及 `tables/` 下 3 张表；直接核对了 2 条关系、5 个度量值、M 表达式、日期表标记和月份排序属性。磁盘文件存在是保存证据，但尚不代替重开后的模型执行验证。
- 根 `.pbip` SHA-256 仍为 `AF67AAF1A650845C67975103E6F2079E414A9E51BB841A097DC51AD518362FD9`，与种子一致；`definition.pbir` 未发生 Git 变更。运行目录总大小约 148 KB，未触及制品体积阈值。
- Desktop 原生 TMDL/JSON 保留原始 CRLF；`git diff --check` 因 CRLF 对新增行报尾空格，不据此转换 Power BI 文件。重开前原样 Git 快照提交为 `b01d551938f7f9f4926a437fa8eab5002949228e`，可用于后续结构 diff 和回滚。

## 模型持久化闸门：重开后 MCP 回读

- 用户重新打开运行副本；Desktop 进程启动参数明确指向 `V0/runs/20260917-003433/project/PowerBIBuilderV0Seed.pbip`，不是种子。新引擎 PID `23532`，端口 `localhost:54545`；MCP 新连接 `PBIDesktop-PowerBIBuilderV0Seed-54545`。
- MCP 回读 3 张表、3 个 `Ready` Import/M Partition、2 条活动单向多对一关系、5 个精确命名的度量值，以及 `DataFilePath`、`SalesSource` 两个 M 表达式。五个度量值的表达式和格式字符串均未漂移。
- `DimDate.dataCategory=Time`、`DimDate[Date]` 唯一、`DimDate[MonthName].sortByColumn=MonthNumber` 在重开后保持不变。
- 重开后代表性 DAX 成功：三表行数 `15/5/88`；总计销售额 `9356.75`、销量 `74`、成本 `6344.80`、毛利额 `3011.95`、毛利率 `0.3219013011996687`；`Technology` 销售额 `7690`，`2026-04` 销售额 `0`。均与独立基准一致。
- 因此模型已通过磁盘定义和重开运行验证；执行者随后再次关闭 Desktop，才开始 PBIR 编辑。

## PBIR 生成与离线预检

- 执行者再次关闭 Desktop；进程检查未发现 `PBIDesktop` 或 `msmdsrv`。模型持久化闸门至此完成，随后才开始 PBIR 编辑。
- 仅修改运行副本唯一 `Overview` 的 `page.json`（1280 × 720）并新增 6 个 `visual.json`：3 个独立 `cardVisual`（销售额、毛利额、毛利率）、1 个 `lineChart`（`DimDate[YearMonth]` × 销售额）、1 个 `clusteredColumnChart`（品类 × 销售额）、1 个品类 `Dropdown` slicer。页面显式配置 slicer 对其他 5 个对象的 `DataFilter` 交互。
- `V0/scripts/validate_pbir.py` 对根 `.pbip`、PBIR JSON 使用微软公开 Schema 验证，并检查项目路径、`definition.pbir` 不变性、唯一页面、6 个类型与字段绑定、画布边界、对象不重叠及 5 条交互。脚本从微软公开地址读取 10 份 Schema，全部通过；`jsonschema==4.26.0` 临时安装在被忽略的 `V0/.work/`，未纳入正式产物。
- 微软公开的 `visualConfiguration/2.3.0/schema-embedded.json` 内 `$id` 使用未实际发布的 `schema.embedded.json`；验证脚本只为这一已核实地址做别名映射，不跳过任何 Schema 规则。
- `.pbip` 及 `definition.pbir` 内容与种子逐字节一致；未编辑 `report.json`、`pages.json`、`version.json`、主题或其他外围文件。尚未用 Desktop 实际打开生成后的 PBIR，不能判定视觉或交互验收通过。

## Desktop 首次打开与未筛选页面

- 执行者打开生成后的运行副本，报告没有阻塞错误或自动修复提示；尚未执行保存。
- 未筛选页面截图保存为 `evidence/overview-unfiltered.png`（406442 字节，SHA-256 `B75F59806E922F632EC0D6EA64E61B70B857C3A38C85362DCA94B1B40BAB2BE4`）。截图显示唯一 Overview 页、3 张独立 KPI、月度线图、品类柱状图及品类下拉切片器，位置互不重叠，标题与轴标签未见裁切。
- 3 张 KPI 依次显示约 `9.36 千`、`3.01 千`、`32.2%`，与精确 DAX 基准 `9356.75`、`3011.95`、`32.1901%` 的默认显示缩写/四舍五入一致。此项不替代后续筛选交互验证。

## Technology 切片器交互

- 执行者在品类下拉框选择 `Technology`，未保存项目；截图保存为 `evidence/overview-technology.png`（108377 字节，SHA-256 `FD32E50CDA2CF2518EC84B54A2C8F8E2DB0901BA3751A85E4ADCDEB30ADA6646`）。
- 3 张卡片分别显示约 `7.69 千`、`2.31 千`、`30.1%`，对应 Python 与 DAX 的精确基准 `7690.00`、`2314.00`、`30.0910%`；显示差异仅为默认缩写/四舍五入。
- 趋势图只显示 Technology 的 2026-01 至 2026-03 月度值（`2600`、`1297`、`3793`），品类柱状图仅剩 Technology；切片器对卡片和两张图的过滤已观察到。
- 执行者确认页面文字和图表在其屏幕上清晰可读；随后清除品类切片器，3 张卡片恢复约 `9.36 千`、`3.01 千`、`32.2%`，品类图恢复四类。此时尚未保存项目。阶段 9 的视觉与固定交互验收通过。

## Desktop 保存后磁盘差异（重开前）

- 执行者在清除切片器后点击 Desktop“保存”并关闭；关闭时未出现额外保存、错误或自动修复提示。进程检查未发现 `PBIDesktop` 或 `msmdsrv`。
- 保存前 PBIR 快照为提交 `535a0c7`，与首次加载前的 `c0cbb92` 相比 PBIR 文件未变；保存后快照为 `c7a4579`。仅有 Overview 的 `page.json` 和 6 个 `visual.json` 被 Desktop 写回。根 `.pbip`、`definition.pbir`、模型、`pages.json` 及外围文件未变。原始差异可由两次快照的 Git diff 复查。
- 解析后比较：页面 JSON 和 5 个非切片器视觉对象均完全等价，仅序列化格式、换行符和文件末尾状态变化；切片器增加空的 `visual.objects.general[0].properties`，其 `$schema` 由 `visualContainer/2.9.0` 更新为 Desktop 写出的 `2.12.0`。切片器的品类字段、下拉模式、位置与尺寸未变，未保存 `Technology` 筛选。
- 保存后的根 `.pbip`、项目路径、`byPath`、唯一 Overview、6 个视觉对象与类型、字段绑定、布局和 5 条显式筛选交互均通过离线检查。当前微软公开的 `visualContainer/2.12.0/schema.json` 地址返回 HTTP 404，因此**无法声称按 2.12.0 原版本完成 Schema 校验**；仅对内存副本使用公开的 2.9.0 Schema 作兼容性校验（通过），磁盘上的 Desktop 产物未被改写。随后 Desktop 重开实际验收通过；兼容性校验不被冒充为精确 2.12.0 校验。

## 最终重开与 MCP 持久化回读

- 执行者重新打开运行副本，确认无错误或自动修复提示；唯一 Overview 仍显示 6 个视觉对象，未筛选的 3 张卡片约为 `9.36 千`、`3.01 千`、`32.2%`。重开后 Git 工作区保持清洁，未发现额外磁盘重写。
- Desktop 启动参数指向本运行目录 `.pbip`；新本地模型实例为 `localhost:51177`，MCP 连接名 `PBIDesktop-PowerBIBuilderV0Seed-51177`。
- MCP 回读 `FactSales`、`DimProduct`、`DimDate` 三表；三个 Import/M 分区均为 `Ready`，`DataFilePath` 和 `SalesSource` 两个 M 命名表达式仍在。两条关系均为活动、单向、多对一；五个度量值名称、表达式和格式字符串均未漂移。
- `DimDate.dataCategory=Time`、`DimDate[MonthName].sortByColumn=MonthNumber` 保持不变。
- 代表性 DAX 返回三表行数 `15/5/88`，销售额 `9356.75`、销量 `74`、成本 `6344.8`、毛利额 `3011.95`、毛利率 `0.3219013011996687`；Technology 销售额 `7690`、毛利额 `2314`；ZeroSales 毛利率为 `BLANK`。均与独立 Python 基准一致。结构化结果见 `logs/final-mcp-readback.json`。

## 当前结论

**完整成功。** 自然语言需求 → 官方 Modeling MCP → Power Query/语义模型/DAX → Codex 生成 PBIR → PBIP → Desktop 打开、交互、保存重开 → 最终 MCP 回读的 V0 链路已跑通。唯一已知校验限制是 Desktop 保存后将切片器 `$schema` 更新到 2.12.0，而对应公开 Schema 地址暂不可访问；生成时的公开 2.9.0 Schema 校验、保存后的结构/语义对比和 Desktop 实际重开均通过。V0 未验证跨机器迁移或 Power BI Service 发布。
