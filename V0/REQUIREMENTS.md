# Power BI Builder — V0 需求文档

## 1. 文档定位

- 本文档是 Power BI Builder V0 的执行与验收基线。
- 在用户未明确修改方案前，后续步骤、文件组织和成功判定均按本文档执行。
- 如需改变范围、技术路线或成功标准，先更新本文档并记录变更，再继续实施。

## 2. 项目目标

- 通过最小可行实验，验证 Codex 能否结合 Microsoft Power BI Modeling MCP 与 PBIP/PBIR，自动生成可由 Power BI Desktop 正常打开、展示和交互的报表。
- 验证完整链路：自然语言需求 → Codex → Modeling MCP → Power Query / Semantic Model / DAX → PBIR Report → PBIP → Power BI Desktop。
- 本阶段只验证端到端可行性，不建设完整产品。

## 3. V0 基线方案

- 使用 Power BI Desktop 创建并保存的最小空白 PBIP/PBIR 工程作为种子。
- 种子仅包含有效工程结构、空白语义模型和唯一的空白 `Overview` 页面，不预置目标表、度量值或视觉对象。
- 语义模型通过 Microsoft 官方 Power BI Modeling MCP 创建和修改。
- 报表页面内容与视觉对象通过公开 PBIR 文件格式生成。
- Power BI Service、浏览器报表编辑和 Fabric 发布不属于本地 PBIP 验证链路。
- 零种子、零模板创建整个 PBIP 工程壳不属于 V0。

## 4. 固定执行路线

1. 在 Power BI Desktop 中打开种子 `.pbip`。
2. Modeling MCP 连接当前 Desktop 本地语义模型。
3. 通过 MCP 创建数据加载、表、关系和度量值，完成刷新与 DAX 查询。
4. 通过 MCP 回读模型对象，保存 PBIP，然后关闭 Desktop。
5. Codex 在磁盘上修改种子中已有的 `Overview` 页面，不新建第二个页面。
6. 对生成的 PBIR 执行 JSON、Schema 和引用校验。
7. 重新打开 PBIP，验证模型、视觉对象、数据和交互。
8. 保存、关闭并再次打开，完成最终验收。

V0 不混用“直接加载离线 PBIP 模型”和“连接 Desktop 模型”两条 MCP 路线。若主路线不可用，停止并记录，不静默切换。

## 5. 输入数据契约

- 输入文件为 `V0/data/sales.csv`。
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
- 数据量保持较小，便于人工检查；维度键无空值、无重复映射、无孤儿外键。
- 数据包含至少一个筛选后销售额为零的合法场景，用于验证毛利率安全除法；退货、缺失成本等异常场景不纳入 V0。
- V0 只保证当前实验环境可刷新。实际数据路径、区域设置和解析规则必须记录，不承诺跨机器免配置迁移。

## 6. Power Query / M 与刷新

- 通过 MCP 创建必要的 Power Query/M named expression 和 Import Partition，不以手工导入替代。
- 创建 `DataFilePath` 记录当前环境中的 CSV 绝对路径，并由共享表达式 `SalesSource` 读取和显式转换字段类型。
- 三张表的数据生成方式固定为：
  - `FactSales`：从 `SalesSource` 加载销售明细。
  - `DimProduct`：从销售源选取 `ProductKey`、`Product`、`Category` 后去重。
  - `DimDate`：根据最小和最大 `SaleDate` 生成连续日期。
- 刷新后验证三张表均有数据、Schema 与预期一致，且维度键约束成立。
- 数据未成功加载和刷新时，不进入关系、DAX 或 PBIR 阶段。

## 7. 语义模型与命名契约

- 表名固定为：`FactSales`、`DimDate`、`DimProduct`。
- 建立并激活以下关系：
  - `DimDate[Date]` 1 → * `FactSales[SaleDate]`。
  - `DimProduct[ProductKey]` 1 → * `FactSales[ProductKey]`。
- 两条关系均采用从维度表到事实表的单向筛选。
- `DimDate[Date]` 必须唯一、连续且无空值；`DimProduct[ProductKey]` 必须唯一且无空值。
- 关闭 Auto date/time，并将 `DimDate` 标记为日期表。
- 表、列和度量值的精确名称是 PBIR 字段绑定契约。未经需求变更不得重命名；绑定对象缺失或改名导致断链即为失败。
- MCP 产生 `.tmdl` 文件变化属于正常结果；禁止绕过 MCP 手工修改模型后声称 MCP 链路成功。

## 8. DAX 度量值契约

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

- 毛利率在销售额为零时预期返回 `BLANK`。
- 通过 MCP List/Get 回读度量值定义，并执行总计、月份和品类层级的 DAX 查询。

## 9. 独立计算基准

- 使用独立本地脚本直接读取原始 CSV 生成基准结果，不调用 Power BI，也不复用 DAX 查询结果。
- 默认使用 `V0/scripts/calc_expected.py`，结果保存为机器可读文件并写入验收记录。
- 至少核对：
  - 5 个度量值的总计。
  - 按月份的销售额和毛利额。
  - 按品类的销售额和毛利额。
  - 一个品类筛选后的代表性结果。
- 允许误差：
  - 销量完全相等。
  - 金额绝对误差不超过 `0.01`。
  - 毛利率绝对误差不超过 `0.0001`。
  - 零分母场景应与 `BLANK` 预期一致。

## 10. PBIR 报表契约

- 修改种子中已有的唯一 `Overview` 页面，最终页面总数为 1。
- 页面包含且只要求以下 6 个标准视觉对象：
  - 3 张独立单值 Card：销售额、毛利额、毛利率。
  - 1 个 Line chart：日期 × 销售额。
  - 1 个 Clustered column chart：品类 × 销售额。
  - 1 个 Category dropdown slicer。
- 使用当前锁定 Desktop 版本的内置视觉对象，不使用 multi-row card 或自定义视觉对象。
- 页面保持基础、清晰、可读，不加入复杂主题、书签、钻取或移动布局。
- 品类切片器必须过滤全部 3 张 Card、趋势图和品类图；其他图表间交叉高亮不作为 V0 验收条件。

## 11. 环境与 MCP 能力闸门

执行前记录：

- Power BI Desktop 完整版本。
- PBIP/PBIR 相关预览功能及 Auto date/time 状态。
- Modeling MCP 版本、实际启动参数和连接目标。
- Codex 中可见的 MCP 工具清单。
- 输入文件路径、编码、分隔符和区域设置。

仅验证 V0 需要的 MCP 能力：

- 连接 Desktop 本地模型。
- 创建和读取表、列、M 表达式及 Partition。
- 刷新模型或 Partition。
- 创建和读取关系与度量值。
- 执行 DAX 查询。
- 保存后重新连接并回读模型。

任一必要能力不可用时停止，记录为环境阻塞或部分链路，不用直接编辑 TMDL 掩盖失败。BIM/TMDL 导出、Fabric 部署、计算组和 RLS 不属于能力闸门。

V0 保留首次模型修改和首次查询的人工确认。执行前以已安装版本的实际帮助信息确认安全参数，不硬编码可能随版本变化的跳过确认参数。

## 12. PBIR 校验与保存差异

PBIR 生成后的校验顺序：

1. JSON 语法校验。
2. 按每个文件声明的公开 JSON Schema 校验。
3. 页面、视觉对象、对象名称及跨文件引用检查。
4. 表、列和度量值绑定检查。
5. Power BI Desktop 打开验证。

- Schema 校验通过不等同于 Desktop 验收通过。
- Desktop 保存前后分别保留 PBIR 快照和原始 diff。
- 保存后以下语义必须不变：页面数与名称、6 个视觉对象及类型、字段绑定、位置和尺寸、切片器字段与效果、报表到模型的 `byPath` 引用。
- 序列化顺序、内部生成引用或默认属性的规范化只记录，不因字节差异直接判失败。
- 若 Desktop 对生成的 PBIR 报告自动修复或非阻塞修复警告，不能判定为完整成功。

## 13. 阶段验证与停止规则

按以下顺序执行，每个阶段通过后再进入下一阶段：

1. Git、种子和环境检查。
2. MCP 连接与能力矩阵。
3. M/Partition 创建和数据刷新。
4. 模型、关系、度量值回读。
5. DAX 与独立基准对比。
6. PBIR 生成和 Schema 校验。
7. Desktop 打开、渲染和交互验证。
8. Desktop 保存、关闭和重开验证。

失败时立即停止后续依赖步骤，保留现场和日志，不在同一运行目录中用复杂替代方案覆盖失败结果。

## 14. 成功判定

### 完整成功

以下条件全部满足：

- Modeling MCP 实际完成 M/Partition、模型、关系和度量值创建或修改。
- CSV 刷新成功，3 张表、2 条关系和 5 个度量值符合契约。
- MCP 回读和 DAX 查询成功，结果与独立基准一致。
- PBIR 自动生成规定的唯一页面和 6 个视觉对象，并通过 Schema 与引用校验。
- Desktop 无 PBIP/PBIR 修复性错误或自动修复警告地打开项目。
- 数据、布局和切片器交互正确。
- 保存、关闭并重新打开后语义和显示保持正确。

### 部分成功

- 模型与 DAX 链路成功，但 PBIR 或 Desktop 验证失败；或
- Desktop 能打开，但对自动生成内容执行了非阻塞自动修复。

### 失败或环境阻塞

- 必要 MCP 能力不可用；或
- 数据不能刷新、模型对象不正确、DAX 基准不一致；或
- Desktop 因生成内容发生阻塞错误而无法打开。

隐私级别、遥测或首次功能介绍等非工程提示可人工处理并记录，不单独判定为失败；数据源路径或凭据导致不能刷新则判定失败。

## 15. 文件组织与验收产物

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
- `.work/` 仅保存可删除的中间文件，并由 Git 忽略。
- 记录种子 Git 提交或哈希、运行标识和关键工具版本。
- `VALIDATION.md` 至少包含：环境指纹、MCP 能力矩阵、对象回读、DAX 基准对比、PBIR 校验、保存前后差异、Desktop 打开与交互证据、最终分级及已知限制。
- 验证通过的关键阶段应形成 Git 提交，保证可比较和可回滚。

## 16. V0 范围外

- Power BI Service 发布、共享、权限、网关和刷新计划。
- 跨机器无配置迁移和数据源凭据自动处理。
- RLS、增量刷新、计算组、复杂时间智能和性能优化。
- 多页面、移动布局、复杂主题、书签、钻取和自定义视觉对象。
- 完整异常数据测试，包括退货、缺失成本、重复维度键和孤儿外键。
- 产品化 UI、多租户、审计、部署流水线和长期兼容性。

## 17. 已知风险与执行纪律

- Modeling MCP、PBIP 和 PBIR 仍可能存在预览期行为或版本变化，必须固定并记录版本。
- Modeling MCP 只负责语义模型，不负责报表页面和视觉对象。
- PBIR JSON Schema 只能证明结构合规，最终结果必须由 Desktop 打开和交互验证。
- 本地 CSV 路径影响刷新可移植性，但不扩大 V0 为跨机器部署实验。
- 保留种子、运行副本、日志和 Git 历史；遇到失败优先回滚或新建运行目录，不在未知状态上反复覆盖修改。
