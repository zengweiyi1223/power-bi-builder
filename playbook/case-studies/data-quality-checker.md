# data-quality-checker — 跨领域验证案例

本案例只保存非 Power BI 验证项目的事实与方法结论。产品实现细节不自动成为 Playbook 规则。

## 1. 固定来源

- 项目：`data-quality-checker`
- Playbook 基线：`v0.2@dff3a717d59935697e310a29caf6b29dff11ff11`
- 生命周期设计包：`2319a6904cd1dba0b696e59b9376889a3179b068`
- 需求冻结：`70fb532bd31b9ffcf0794eafd41b583621ab4ed4`
- 公开 release：`a475db50b18e7a430d04e4dbede72679a8c97adb`
- 最终归档：`416ec65453fd280a611065c09272aa5d293a9f33`
- 正式反馈：`PLAYBOOK_FEEDBACK.md`、`VALIDATION.md`、`HANDOFF.md`、`RECORDS.md`

## 2. 项目边界

项目以 `PF-APP` 为基础画像，启用 `MD-UI`、`MD-DATA`、`MD-DEPLOY`、`MD-SEC`，条件启用最小 `MD-OPS`。它交付一个浏览器本地处理 CSV 的静态应用，只检查空值和完全重复行，并把检查 Core 与 CSV Adapter、UI 和部署分离。

项目明确排除了类型/日期推断、清洗修复、其他数据源、账号与云保存、AI 功能、大文件承诺和生产 SLA。

## 3. 验证结果

- 23/23 自动测试通过；Core、Adapter、真实浏览器、构建产物、网络行为和公开 HTTPS 分层验证。
- 公开站点的 7/7 文件 hash 与批准 release build 一致。
- 所有适用 Required Rules conformant；Conformity 与 Utility 分开评价。
- `PF-APP + modifiers` 足以表达项目，没有被迫增加新的基础画像。
- `Required / Conditional / Not Applicable + 理由` 保留了 UAT、发布、回滚和安全，同时排除了无关运维范围。
- 生命周期阶段与 v0.2 Evidence Gate 共用同一 Validation，没有形成冲突的双流程。
- Rolling Validation 适合当前状态与异常链；Final Handoff 适合最终入口、非结论和恢复边界。

## 4. 规则产生的实际 Utility

| 事件 | Gate 作用 | 方法结论 |
| --- | --- | --- |
| 首次真实浏览器检查发现 favicon 404 | Blocking，修复后完整重跑 | 浏览器真实运行不能被静态构建成功替代 |
| 隔离恢复时发现 SVG 行尾造成 hash 不一致 | 发布前停止、修复、重新构建和复验 | 回滚点必须验证，而不只是文字声明 |
| workflow 权限和 runner 漂移 | 分别记录为权限条件和残余风险 | 环境/平台风险不能伪装成产品功能失败 |
| 发布前没有外部写入授权 | HG-04 阻止创建远端、push 和部署 | Human Gate 有实际治理价值 |

Release、Operate 和 Close 阶段发现了实现结束后仍可能遗漏的部署、复现和恢复问题，HYP-06 获得强支持。

## 5. 对 v1.0 的支持

- 保留 v0.2 的 20 条规则；`R-VLD-003` 有充分跨领域 Utility，建议升为 Required。
- `R-VDC-002` 防止诊断与验证步骤污染生产工作流，建议在触发相关声明时升为 Required。
- `R-EXV-003` 因项目不作效率声明而 N/A，继续保持 Provisional。
- 六类画像、风险修饰器、阶段 R/C/N/A、责任模型和逻辑记录/物理文件分离获得支持。
- `TECH_DESIGN` 中的多方案比较和 HG-02 冻结有效；“多个 AI 参与”本身没有被验证，只能作为 Guidance。
- I-00～I-09 的可验证任务与 C0～C7 checkpoint 支持风险优先、最小闭环和阶段恢复。

## 6. 模板摩擦

小项目在 PROJECT、VALIDATION 和 HANDOFF 中出现少量状态重复。v1.0 因此规定：

- 动态状态只在 VALIDATION 维护；
- PROJECT 只保存稳定画像、责任、裁剪和导航；
- HANDOFF 只保存最终结论、入口、限制和恢复；
- 逻辑记录可以合并，但 Artifact Map 必须能找到对应章节。

## 7. 未泛化的项目事实

以下内容不进入通用 Core：CRLF fixture 的 JSON 载体、SVG LF、5 MiB 阈值、Vanilla TypeScript、Edge/CDP、GitHub Pages、`ubuntu-latest` 和具体 workflow/deployment ID。

本案例也没有验证：效率计量、PF-SVC 完整运维、多团队协作、高风险/监管项目、公开环境真实降级回滚、多 AI 评审增益或 Power BI 浏览器插件。
