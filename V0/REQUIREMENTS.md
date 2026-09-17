# Power BI Builder — V0 需求文档

## 1. 文档定位与冻结规则

- 本文档是 Power BI Builder V0 的执行与验收基线。
- 在用户未明确修改方案前，后续步骤、文件组织和成功判定均按本文档执行。
- 本次重构后冻结 V0 的功能范围、技术路线、数据契约和成功口径，不因实施中的 MCP Preview bug、PBIR 兼容问题或 Desktop 版本差异继续扩展需求。
- 实施问题记录到运行日志和 `VALIDATION.md`。只有发现本文档存在矛盾、不可实现或与锁定版本的官方格式冲突时，才提出显式勘误，经确认后以独立 Git 提交修改。

## 2. 项目目标

- 通过最小可行实验，验证 Codex 能否结合 Microsoft Power BI Modeling MCP 与 PBIP/PBIR，自动生成可由 Power BI Desktop 正常打开、展示和交互的报表。
- 验证完整链路：自然语言需求 → Codex → Modeling MCP → Power Query / Semantic Model / DAX → PBIR Report → PBIP → Power BI Desktop。
- 本阶段只验证端到端可行性，不建设完整产品。

## 3. V0 基线与种子前置条件

- 使用 Power BI Desktop 人工创建并保存的最小空白 PBIP/PBIR 工程作为种子。
- 创建种子时启用所需 PBIP/PBIR 功能，并在 Desktop 的 Current File 设置中关闭 Auto date/time。
- 种子仅包含有效工程结构、空白语义模型和唯一的空白 `Overview` 页面，不预置目标表、度量值或视觉对象。
- 种子保存到 `V0/seed/`，纳入 Git 后视为不可变；所有实验先复制到 `V0/runs/<run-id>/project/`，后续操作仅针对运行副本。
- 种子必须保留报告对语义模型的相对 `byPath` 引用。
- Auto date/time 关闭状态以人工确认 Desktop 的 Current File 设置，并核对保存后 `model.tmdl` 中 `__PBI_TimeIntelligenceEnabled = 0` 为主要证据；截图可选。模型创建、刷新和重开后，再通过 MCP 表清单、模型元数据或受支持的 DMV 查询确认未出现自动日期表，作为辅助证据。隐藏表不存在不能单独证明该设置已关闭。
- Power BI Service、浏览器报表编辑和 Fabric 发布不属于本地 PBIP 验证链路。
- 零种子、零模板创建整个 PBIP 工程壳不属于 V0。

## 4. 人工与 Codex 职责边界

### 人工负责

- 创建空白种子并设置 Desktop 当前文件选项。
- 在要求的阶段打开、保存、关闭和重开 Power BI Desktop。
- 处理 MCP 首次修改、首次查询确认，以及隐私、凭据和系统弹窗。
- 确认 Desktop 已识别模型修改并显式执行 Save；若关闭时出现保存提示，选择保存并记录提示及处理结果。
- 完成最终视觉结果的人工签字确认。

### Codex 负责

- 建立运行目录、复制种子并保护原始种子。
- 生成固定输入数据和独立计算基准。
- 调用 MCP 完成数据加载、建模、刷新、回读和 DAX 查询。
- 生成和校验运行副本中的 PBIR 文件。
- 执行客观的数值、结构、布局和交互检查，保存证据并填写 `VALIDATION.md`。
- 检查 Git 状态、保留回滚点并提交已验证阶段。

人工操作不替代自动验证；Codex 自动检查也不替代最终人工视觉确认。

## 5. 固定执行路线

1. 检查 Git、种子、环境和 MCP 能力，创建唯一 `<run-id>` 并复制种子到运行目录。
2. 人工打开运行副本的 `.pbip`，MCP 连接当前 Desktop 本地语义模型。
3. Codex 通过 MCP 创建数据加载、表、关系、属性和度量值，完成刷新、回读和首次 DAX 验证。
4. DAX 结果与独立 Python 基准对比。
5. 人工在 Desktop 中确认模型已修改，显式保存并关闭；记录关闭时是否出现保存提示。
6. 执行独立的“模型持久化闸门”：保存磁盘快照，重开仍为空白报表的 PBIP，MCP 重新连接、回读模型并执行代表性 DAX；通过后再次关闭 Desktop。
7. Codex 仅在运行副本中修改允许范围内的 PBIR 页面和视觉文件。
8. 执行项目入口、JSON Schema、引用和 PBIR 结构校验。
9. 人工重开 PBIP；Codex 验证视觉渲染、数值、布局和切片器交互，人工完成视觉签字确认。
10. 人工保存、关闭并再次打开完整项目。
11. MCP 最终重新连接，回读持久化模型并执行代表性 DAX，完成最终验收。

V0 不混用“直接加载离线 PBIP 模型”和“连接 Desktop 模型”两条 MCP 路线。若主路线不可用，停止并记录，不静默切换。

## 6. 输入数据契约

- 输入文件为 `V0/data/sales.csv`。
- 由 Codex 一次性、确定性生成并提交 Git；不使用随机数据，不在每次 Run 中重新生成或覆盖。
- 后续所有 Run 共用同一份输入。改变数据内容必须先获得明确需求变更并形成独立提交。
- 文件采用 UTF-8、逗号分隔、首行列名、ISO 日期 `YYYY-MM-DD` 和点号小数。
- 事实表粒度：每行表示某日期、某产品的一条销售记录。
- 精确列名与类型：
  - `SaleDate`：日期。
  - `ProductKey`：整数键。
  - `Product`：文本。
  - `Category`：文本。
  - `Quantity`：整数。
  - `UnitPrice`：定点小数，最多两位小数。
  - `UnitCost`：定点小数，最多两位小数。
- 数据量保持较小；维度键无空值、无重复映射、无孤儿外键。
- 数据必须包含品类 `Technology`，作为固定交互测试值。
- 数据必须包含至少一个筛选后销售额为零的合法场景，用于验证毛利率安全除法；退货、缺失成本等异常场景不纳入 V0。
- V0 只保证当前实验环境可刷新。实际数据路径、区域设置和解析规则必须记录，不承诺跨机器免配置迁移。

## 7. Power Query / M 与刷新

- 通过 MCP 创建必要的 Power Query/M named expression 和 Import Partition，不以手工导入替代。
- 创建 `DataFilePath` 记录当前环境中的 CSV 绝对路径，并由共享表达式 `SalesSource` 读取数据和显式转换字段类型。
- 三张表的数据生成方式固定为：
  - `FactSales`：从 `SalesSource` 加载销售明细。
  - `DimProduct`：从销售源选取 `ProductKey`、`Product`、`Category` 后去重。
  - `DimDate`：根据最小和最大 `SaleDate` 生成连续日期及规定的日期属性列。
- CSV 解析显式使用固定编码、分隔符、区域和数据类型，不依赖当前机器的隐式区域设置。
- 刷新后验证三张表均有数据、Schema 与预期一致，且维度键约束成立。
- 数据未成功加载和刷新时，不进入关系、DAX 或 PBIR 阶段。

## 8. 语义模型、日期表与命名契约

- 表名固定为：`FactSales`、`DimDate`、`DimProduct`。
- `DimDate` 最小列集固定为：
  - `Date`：日期，唯一、连续且无空值。
  - `Year`：整数。
  - `MonthNumber`：1–12 的整数。
  - `MonthName`：英文月份名称。
  - `YearMonth`：文本，格式为 `YYYY-MM`。
- `DimDate[MonthName]` 的 `sortByColumn` 必须设置为 `DimDate[MonthNumber]`。
- 将 `DimDate` 标记为日期表，并指定 `DimDate[Date]` 为日期列。
- 建立并激活以下关系：
  - `DimDate[Date]` 1 → * `FactSales[SaleDate]`。
  - `DimProduct[ProductKey]` 1 → * `FactSales[ProductKey]`。
- 两条关系均采用从维度表到事实表的单向筛选；`DimProduct[ProductKey]` 必须唯一且无空值。
- 表、列和度量值的精确名称是 PBIR 字段绑定契约。未经需求变更不得重命名；绑定对象缺失或改名导致断链即为失败。
- MCP 产生 `.tmdl` 文件变化属于正常结果；禁止绕过 MCP 手工修改模型后声称 MCP 链路成功。

## 9. DAX 度量值与格式契约

必须创建以下 5 个度量值，名称和业务定义保持不变：

```DAX
销售额 =
SUMX ( FactSales, FactSales[Quantity] * FactSales[UnitPrice] )

销量 =
SUM ( FactSales[Quantity] )

成本 =
SUMX ( FactSales, FactSales[Quantity] * FactSales[UnitCost] )

毛利额 =
[销售额] - [成本]

毛利率 =
DIVIDE ( [毛利额], [销售额] )
```

格式字符串固定为：

- `销售额`、`成本`、`毛利额`：`#,0.00`。
- `销量`：`#,0`。
- `毛利率`：`0.0%`。

- 毛利率在销售额为零时预期返回 `BLANK`。
- 通过 MCP List/Get 回读度量值表达式和格式字符串。
- 总计查询使用全部 5 个度量值；月度查询统一按 `DimDate[YearMonth]` 分组；品类查询按 `DimProduct[Category]` 分组。

## 10. 独立计算基准

- 使用独立本地 Python 脚本直接读取原始 CSV 生成基准结果，不调用 Power BI，也不复用 DAX 查询结果。
- 默认使用 `V0/scripts/calc_expected.py`，结果保存到运行目录的 `expected-results.json`。
- 结果中记录固定的 `interactionTestCategory`，其值为 `Technology`。
- 至少核对：
  - 5 个度量值的总计。
  - 按 `YYYY-MM` 的销售额和毛利额。
  - 按品类的销售额和毛利额。
  - `Technology` 筛选后的 5 个度量值。
- 允许误差：
  - 销量完全相等。
  - 金额绝对误差不超过 `0.01`。
  - 毛利率绝对误差不超过 `0.0001`。
  - 零分母场景应与 `BLANK` 预期一致。

## 11. PBIR 报表、布局与交互契约

- 仅修改运行副本中已有的唯一 `Overview` 页面，最终页面总数为 1。
- 页面尺寸固定为 1280 × 720、16:9。
- 页面包含且只要求以下 6 个标准视觉对象：
  - 3 张独立单值 Card：销售额、毛利额、毛利率。
  - 1 个 Line chart：日期 × 销售额。
  - 1 个 Clustered column chart：品类 × 销售额。
  - 1 个 Category dropdown slicer。
- 使用锁定 Desktop 版本的内置视觉对象，不使用 multi-row card 或自定义视觉对象。
- 6 个视觉对象必须全部位于画布内，不得重叠；标题、数据标签和轴标签不得裁切，并在 100% 缩放下可辨认。
- 不加入复杂主题、书签、钻取或移动布局。
- 品类切片器必须过滤全部 3 张 Card、趋势图和品类图；其他图表间交叉高亮不作为 V0 验收条件。
- 固定交互验证步骤：
  1. 记录未筛选状态。
  2. 在切片器中选择 `Technology`。
  3. 将 3 张 Card 数值与同品类 DAX 查询及 Python 基准比较。
  4. 验证趋势图和品类图均已受到筛选。
  5. 保存筛选前后截图及数值到 `evidence/` 和 `VALIDATION.md`。
  6. 清除筛选并确认视觉对象恢复。
- 人工最终确认页面可读性，并在 `VALIDATION.md` 中签字记录。

## 12. 环境与 MCP 能力闸门

执行前记录：

- Power BI Desktop 完整版本及 PBIP/PBIR 相关功能状态。
- Auto date/time Current File 设置的人工检查证据。
- Modeling MCP 版本、实际启动参数和连接目标。
- Codex 中可见的 MCP 工具清单。
- 输入文件路径、编码、分隔符和区域设置。

仅验证 V0 需要的 MCP 能力：

- 连接 Desktop 本地模型。
- 创建和读取表、列、M 表达式及 Partition。
- 刷新模型或 Partition。
- 创建和读取关系与度量值。
- 设置并回读日期表及日期列属性。
- 设置并回读列的 `sortByColumn`。
- 设置并回读度量值 `formatString`。
- 执行 DAX 查询。
- Desktop 保存和重开后重新连接、回读模型并执行 DAX。

Auto date/time 是种子和 Desktop 当前文件前置条件，不作为 MCP 修改能力；MCP 元数据或 DMV 检查只作为辅助验证。

任一必要 MCP 能力不可用时停止，记录为能力限制、部分成功或环境阻塞。由于空白种子中不存在 `DimDate` 和度量值，不允许用“种子侧预设”或人工补改这些对象来掩盖 MCP 属性能力缺失。BIM/TMDL 导出、Fabric 部署、计算组和 RLS 不属于能力闸门。

V0 保留首次模型修改和首次查询的人工确认。执行前以已安装版本的实际帮助信息确认安全参数，不硬编码可能随版本变化的跳过确认参数。

## 13. 项目完整性、PBIR 修改范围与校验

### 项目入口完整性

- 根 `*.pbip` 必须通过 JSON 及其公开 Schema 校验，并继续指向正确的 Report 目录。
- 根 `*.pbip` 不属于 Codex 修改范围；生成前后保留哈希或 diff，任何非预期变化均停止并调查。
- `definition.pbir` 不属于 Codex 修改范围；必须保持原有 `byPath` 及文件内容不变。

### PBIR 允许修改范围

Codex 仅可修改运行副本 `<Report>/definition/` 内为 Overview 页面和 6 个视觉对象所必需的文件：

- `definition/pages/pages.json`，仅在确有必要时。
- `definition/pages/<Overview>/page.json`。
- `definition/pages/<Overview>/visuals/*/visual.json`。
- `definition/report.json`，仅当公开 Schema 和目标页面生成确有需要时。

不修改：

- `definition.pbir`、`.platform`、`version.json`、`reportExtensions.json`。
- `mobileState.json`、`semanticModelDiagramLayout.json`。
- bookmarks、`mobile.json`、`StaticResources/` 及其他 V0 无关文件。

### 校验顺序

1. 根 `*.pbip` 和所有目标 JSON 的语法校验。
2. 按文件声明的公开 JSON Schema 校验。
3. 页面、视觉对象、对象名称及跨文件引用检查。
4. 表、列、度量值和视觉绑定检查。
5. `definition.pbir` 的 `byPath` 和不变性检查。
6. Power BI Desktop 打开验证。

- Schema 校验通过不等同于 Desktop 验收通过。
- PBIR 修改前、Desktop 首次加载后和最终保存后分别保留快照与原始 diff。
- 保存后以下语义必须不变：页面数与名称、6 个视觉对象及类型、字段绑定、位置和尺寸、切片器字段与效果、报表到模型的 `byPath` 引用。
- 序列化顺序、内部生成引用或默认属性的规范化只记录，不因字节差异直接判失败。
- 若 Desktop 对生成的 PBIR 报告自动修复或非阻塞修复警告，不能判定为完整成功。

## 14. 阶段验证与停止规则

每个阶段通过后再进入下一阶段：

1. Git 回滚点、种子、运行副本和环境检查。
2. MCP 连接与能力矩阵。
3. 固定 CSV、独立基准脚本及预期结果准备。
4. M/Partition 创建和数据刷新。
5. 模型、关系、属性和度量值回读。
6. DAX 与独立基准对比。
7. **模型持久化闸门**：人工保存并关闭 → 保存磁盘快照 → 重开 PBIP → MCP 回读 3 表、2 关系、5 度量值、M/Partition 及属性 → 执行代表性 DAX → 再次关闭。
8. PBIR 生成、项目入口和 Schema 校验。
9. Desktop 打开、视觉渲染、布局和固定交互验证。
10. Desktop 保存、关闭和重开验证。
11. **最终持久化回读**：MCP 重新连接 → 回读模型契约 → 执行代表性 DAX → 记录最终状态。

模型持久化闸门适用快照和“失败即停止”规则；未通过时不得进入 PBIR 阶段。所有阶段失败时立即停止后续依赖步骤，保留现场和日志，不在同一运行目录中用复杂替代方案覆盖失败结果。

Git 用于执行治理、版本记录和回滚，不属于 Power BI Builder 的技术成功判定。若无法建立安全回滚点，记录为执行治理阻塞并暂停修改，不将其误报为 Power BI 技术失败。

## 15. 成功判定

### 完整成功

以下条件全部满足：

- 种子前置、Auto date/time、环境和必要 MCP 能力检查通过。
- Modeling MCP 实际完成 M/Partition、模型、关系、日期表属性、列排序属性和度量值创建或修改。
- CSV 刷新成功，3 张表、2 条关系、日期表列和 5 个度量值符合命名、表达式及格式契约。
- MCP 回读和 DAX 查询成功，结果与独立基准一致。
- PBIR 自动生成规定的唯一页面和 6 个视觉对象，并通过项目入口、Schema 与引用校验。
- PBIR 前模型持久化闸门通过。
- Desktop 无 PBIP/PBIR 修复性错误或自动修复警告地打开项目。
- 数据、布局和固定切片器交互验证通过，人工完成最终视觉确认。
- 保存、关闭并重新打开后，最终 MCP 回读及代表性 DAX 均通过。

### 部分成功

- 模型与 DAX 主链路成功，但某项必要属性能力、PBIR 或 Desktop 验证失败；或
- Desktop 能打开，但对自动生成内容执行了非阻塞自动修复；或
- 初始建模成功，但任一持久化回读未通过。

### 失败或环境阻塞

- 必要 MCP 连接、数据加载或核心建模能力不可用；或
- 数据不能刷新、模型对象不正确、DAX 基准不一致；或
- Desktop 因生成内容发生阻塞错误而无法打开。

隐私级别、遥测或首次功能介绍等非工程提示可人工处理并记录，不单独判定为失败；数据源路径或凭据导致不能刷新则判定失败。

## 16. 文件组织与验收产物

V0 的全部文件统一存放在本目录：

```text
V0/
├─ REQUIREMENTS.md
├─ .work/
├─ data/
├─ seed/
├─ scripts/
└─ runs/
   └─ <run-id>/
      ├─ project/
      ├─ logs/
      ├─ evidence/
      ├─ expected-results.json
      └─ VALIDATION.md
```

- `data/` 保存固定输入数据，`scripts/` 保存基准计算和验证脚本。
- `seed/` 保留不可变种子；每次实验复制到独立 `runs/<run-id>/` 后操作。
- `.work/` 是可重建临时目录，由脚本在使用前创建并由 Git 忽略；其中内容不得作为正式验收证据。
- 记录种子 Git 提交或哈希、运行标识和关键工具版本。
- `VALIDATION.md` 至少包含：人工操作记录、环境指纹、MCP 能力矩阵、Auto date/time 证据、对象回读、DAX 基准对比、两次持久化回读、项目及 PBIR 校验、保存前后差异、Desktop 打开与交互证据、人工视觉确认、最终分级及已知限制。
- 正式运行产物默认纳入 Git，包括 `VALIDATION.md`、JSON、CSV、TMDL、PBIR、必要文本日志和关键截图；不得忽略整个 `runs/`。
- 不提交录屏、Power BI 缓存、本机设置、自动恢复文件或无关原始转储，也不得为满足体积限制而静默删除必要证据。
- 单个提交文件不得超过 10 MB；单次运行目录建议不超过 50 MB。超限时暂停提交，在 `VALIDATION.md` 记录文件、大小和用途，再决定压缩、Git LFS 或外部制品存储方案。
- 外部保存的正式制品必须记录路径、文件大小和 SHA-256。
- 首次生成 PBIP 种子后，检查锁定 Desktop 版本的实际编码、换行符和保存重写行为，再以独立提交更新 `.gitattributes`；此前不转换 Power BI JSON、TMDL 或 PBIR。
- 验证通过的关键阶段应形成 Git 提交，保证可比较和可回滚。

## 17. V0 范围外

- Power BI Service 发布、共享、权限、网关和刷新计划。
- 跨机器无配置迁移和数据源凭据自动处理。
- RLS、增量刷新、计算组、复杂时间智能和性能优化。
- 多页面、移动布局、复杂主题、书签、钻取和自定义视觉对象。
- 完整异常数据测试，包括退货、缺失成本、重复维度键和孤儿外键。
- 零种子创建 PBIP 工程、产品化 UI、多租户、审计、部署流水线和长期兼容性。

## 18. 已知风险与执行纪律

- Modeling MCP、PBIP 和 PBIR 仍可能存在预览期行为或版本变化，必须固定并记录版本。
- Modeling MCP 只负责语义模型，不负责报表页面和视觉对象。
- PBIR JSON Schema 只能证明结构合规，最终结果必须由 Desktop 打开、交互及最终 MCP 回读共同验证。
- 本地 CSV 路径影响刷新可移植性，但不扩大 V0 为跨机器部署实验。
- 保留种子、运行副本、日志、快照和 Git 历史；遇到失败优先回滚或新建运行目录，不在未知状态上反复覆盖修改。
