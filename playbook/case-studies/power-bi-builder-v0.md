# Power BI Builder V0 — 方法溯源

本 Case Study 只回答“V0 实际发生了什么，以及为何抽象成这些规则”。未来 Power BI 项目如何执行见 [Power BI Adapter](../adapters/power-bi.md)。

## 1. 来源

- [项目入口](../../README.md)
- [V0 需求与验收契约](../../V0/REQUIREMENTS.md)
- [V0 交接](../../V0/HANDOFF.md)
- [正式 Run 验证记录](../../V0/runs/20260917-003433/VALIDATION.md)
- [教程说明](../../tutorial/README.md)

提炼基线：`78a20f0179b9deb5c3cdaa5e1fc64f502a78ec7b`。

## 2. 实际提交轨迹

| 提交 | 已核实的阶段意义 |
| --- | --- |
| `f2aa331` | 冻结 V0 执行与验收基线。 |
| `c5f43c1` | 固化不可变空白种子。 |
| `c056f30` | 创建隔离 Run，并以待执行状态初始化验证记录。 |
| `5f5dfbf` | 用独立提交修正证据口径，没有静默改变成功标准。 |
| `d3975a2`–`b429b0e` | 逐步验证环境、工具能力和正确 Run 连接。 |
| `da3aaa3` | 建立固定输入、独立计算脚本和预期结果。 |
| `0afafa5` | 记录模型回读及 DAX 与独立基准对比。 |
| `b01d551`–`b19bf6a` | 保存模型快照并通过关闭、重开、回读和查询闸门。 |
| `c0cbb92` | 生成 PBIR 并完成离线结构校验。 |
| `33bb89e`–`535a0c7` | 记录 Desktop 渲染、交互及人工视觉确认。 |
| `c7a4579` | 保留 Desktop 保存后的原始 PBIR 差异。 |
| `2db7009` | 完成最终重开、MCP 回读和功能验收。 |
| `78a20f0` | 汇总交接、教程和后续边界。 |

## 3. 关键事实

- V0 从宽泛目标逐步形成精确输入、对象、执行路线、验收、停止和范围外契约。
- 人工负责 Desktop、系统确认和视觉签字；AI 负责确定性生成、检查、回读和证据整理，两者互不替代。
- 固定输入、不可变种子、Run 副本、正式证据和 `.work` 临时文件采用不同生命周期。
- 模型持久化在 PBIR 生成前单独验证，隔离了模型层和报表层的因果关系。
- 数值基准、MCP 回读、静态 Schema、Desktop 实际运行和人工观察共同构成证据链。
- Desktop 保存后把一个 Schema 声明升级到当时无法获取的版本；项目准确报告“功能成功、精确校验待补证”，没有用兼容性检查冒充原版本验证。
- 面向操作者的教程被单独整理，不替代 VALIDATION 和机器证据。

## 4. Rule 溯源矩阵

| Rule ID | 依据 | V0 事实与抽象理由 | 适用边界 | v0.1 状态 |
| --- | --- | --- | --- | --- |
| R-FRM-001 | V0 Evidence | V0 只验证本地端到端可行性并明确非目标；可证伪问题防止范围漂移。 | 有明确实验或交付目标的项目。 | Required |
| R-CTR-001 | V0 Evidence | `f2aa331` 冻结路线和成功口径；`5f5dfbf` 证明勘误应显式提交。 | 正式 Run。 | Required |
| R-CTR-002 | V0 Evidence | REQUIREMENTS 明确人工与 Codex 职责，教程进一步压缩人工等待点。 | 存在人工、外部应用或权限操作。 | Required |
| R-SAF-001 | User Mandate + V0 Evidence | V0 处理凭据、隐私弹窗、本机路径、公开截图和修改边界；抽象为安全契约。 | 所有可能接触敏感数据或外部系统的项目。 | Required |
| R-WRK-001 | V0 Evidence | 种子、Run、副本、证据和 `.work` 隔离，避免污染原件和混淆证据。 | 有文件或持久化制品的项目。 | Required |
| R-PFL-001 | V0 Evidence | MCP 预检、版本固定、正确实例连接先于建模；缺能力时停止。 | 依赖工具、权限或环境能力。 | Required |
| R-EXV-001 | V0 Evidence | V0 每一依赖阶段通过后再继续，没有在末尾一次性验收。 | 存在依赖链的项目。 | Required |
| R-EXV-002 | V0 Evidence | 打开、保存、关闭、重开和视觉确认均由人工明确完成。 | Contract 定义的 Human Gate。 | Required |
| R-VLD-001 | V0 Evidence | Python 基准不调用 Power BI；防止 DAX 自证正确。 | 关键结论；无数值 Oracle 时使用等价独立依据。 | Required |
| R-VLD-002 | V0 Evidence | 截图、日志、哈希和人工确认各自证明不同事实；公开材料要求脱敏。 | 所有正式验收。 | Required |
| R-VLD-003 | V0 Evidence + Provisional Hypothesis | 两次保存/重开/回读发现并控制持久化风险；跨领域成本收益尚待验证。 | 有宿主重写或持久化状态时。 | Provisional |
| R-STP-001 | V0 Evidence | REQUIREMENTS 定义失败即停止，但实际也允许受控刷新和继续；需区分类型、严重度与恢复。 | 所有阶段 Gate。 | Required |
| R-GIT-001 | V0 Evidence | 需求、种子、持久化、保存前后和最终验收均有明确提交。 | 使用版本控制或等价快照的项目。 | Required |
| R-GIT-002 | Derived | V0 的阶段级提交足以回滚；每个小动作提交会增加负担。 | Git 项目。 | Guidance |
| R-VDC-001 | V0 Evidence | 最终结论同时报告功能成功和 Schema 精确校验缺口，避免二元过度声明。 | 存在部分结果或证据缺口。 | Required |
| R-HOF-001 | V0 Evidence | HANDOFF 汇总结论、入口、证据、回滚点、限制和后续边界。 | 正式交付。 | Required |
| R-GOV-001 | User Mandate | 用户固定由 Maintainer 对话维护 Playbook，实验对话只反馈。 | 本 Playbook 的版本治理。 | Required |
| R-FBK-001 | User Mandate + Provisional Hypothesis | v0.1 必须从 V1 和非 Power BI 项目获得结构化反馈；conformity 不能代替 utility。 | 参与 Playbook 验证的实验。 | Required |

## 5. 未泛化的 Power BI 实现

以下内容只进入 Adapter，不构成 Core Rule：PBIP/PBIR/TMDL、Modeling MCP、DAX、Power Query/M、Auto date/time、`byPath`、视觉对象、Desktop 原生序列化、Power BI Schema 版本和 `.pbi` 缓存。

V0 的种子策略也没有被抽象成“所有项目必须有种子”；Core 只要求可追溯的 Trusted baseline。

## 6. V0 暴露的改进点

- 最终项目名称仍包含 `Seed`；未来应在 Run 初始化 Gate 完成业务命名。
- V0 保存了足够证据，但没有保存所有原始工具输出；通用方法要求预先定义最低证据集，而不是无限留存。
- V0 的完整流程较长；v0.1 把详细依据留在本 Case Study，避免普通执行者承担溯源阅读成本。
