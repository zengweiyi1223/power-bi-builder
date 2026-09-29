# 人机协作开发闭环 Playbook

状态：`v1.0 candidate`（等待自动验证与人工验收，尚未发布）

这套 Playbook 把通用开发生命周期、人机责任、可裁剪阶段、记录模板和证据闸门放在同一条流程中。它适用于实验、文档、数据、组件、应用和服务；项目可以按风险增减阶段，不能静默省略责任、验证或恢复边界。

## 一分钟理解

```text
先对齐为什么做、为谁做
→ 冻结范围和验收
→ 选择并冻结方案
→ 拆成可验证任务
→ 每完成一个增量立即验证、判定和建立回滚点
→ 完成集成验收、受控交付和必要运维
→ 形成可复核、可恢复的 HANDOFF
```

完整生命周期：

```text
Profile & Tailor → Discover & Frame → Contract → Design → Plan & Prepare
→ [Implement → Verify → Human Gate → Decide → Checkpoint] × N
→ Integrated Acceptance → Release / Delivery → Operate / Observe
→ Handoff / Close / Learn
```

## 开始一个项目

1. 阅读 [主规范](PLAYBOOK.md)，选择基础画像、风险修饰器和阶段 R/C/N/A。
2. 用 [PROJECT 模板](templates/PROJECT.template.md)建立根入口、责任和 Artifact Map。
3. 用 [REQUIREMENTS 模板](templates/REQUIREMENTS.template.md)对齐 Why、范围、验收、安全和 Human Gate。
4. 存在实质取舍时使用 [TECH_DESIGN 模板](templates/TECH_DESIGN.template.md)；实施型项目使用 [DELIVERY_PLAN 模板](templates/DELIVERY_PLAN.template.md)或把这些逻辑记录合并到已有文档。
5. 用 [VALIDATION 模板](templates/VALIDATION.template.md)作为唯一滚动状态与证据记录；每次新会话或恢复工作先核对“当前控制状态”，再进行首次修改。
6. 涉及部署或持续运行时使用 [发布与运行模板](templates/RELEASE_OPERATIONS.template.md)。
7. 结束时填写 [HANDOFF 模板](templates/HANDOFF.template.md)；重大取舍和偏差写入 [RECORDS 模板](templates/RECORDS.template.md)。

目录和文件不必照抄。先阅读 [项目结构与记录指南](PROJECT_STRUCTURE.md)，再按项目规模映射逻辑记录。

## 文档地图

| 文档 | 用途 | 普通执行者是否必读 |
| --- | --- | --- |
| [PLAYBOOK.md](PLAYBOOK.md) | 唯一生命周期、规则、责任和 Evidence Gate | 是 |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | 根目录可读性、Artifact Map 和按画像示例 | 建项时阅读 |
| [templates/](templates/) | 必需及条件式记录模板 | 按触发条件使用 |
| [Power BI adapter](adapters/power-bi.md) | Power BI 文件、Desktop、MCP、Service 浏览器插件边界 | 仅 Power BI 项目 |
| [case-studies/](case-studies/) | V0 和跨领域验证事实 | 不必读，用于溯源 |
| [reviews/v1.0-disposition.md](reviews/v1.0-disposition.md) | v0.2 到 v1.0 的逐项处置 | Maintainer Review |
| [CHANGELOG.md](CHANGELOG.md) | 版本变化和基线 | 升级时阅读 |

## 记录最小集

所有正式项目至少保留：

- `PROJECT`：入口、画像、角色、阶段裁剪和 Artifact Map；
- `REQUIREMENTS`：需求原因、范围、验收、安全和责任契约；
- `VALIDATION`：唯一滚动状态、证据、异常、Gate 和 checkpoint；
- `HANDOFF`：最终入口、结论、限制和恢复。

`TECH_DESIGN`、`DELIVERY_PLAN`、`UX_SPEC`、`UAT`、`RELEASE_PLAN`、`RUNBOOK`、`PLAYBOOK_FEEDBACK` 按触发条件启用。逻辑记录可以合并，不能丢失或重复维护权威状态。

## 人与 AI

- 人类负责目标原因、重要取舍、风险接受、外部写入、主观验收和最终授权。
- AI 可以起草、比较方案、实施、验证和整理证据，但不能自行批准 Human Gate。
- 高歧义或高风险方案可以使用多个 AI、领域专家或反方提示做独立评审；共识不等于事实证据。

## 版本与证据

- v0.1：来自 Power BI Builder V0，基线 `3ee871d618db84d55b3b2f86a198ac552864317e`。
- v0.2：吸收 Power BI V1，基线 `dff3a717d59935697e310a29caf6b29dff11ff11`。
- v1.0 candidate：吸收 `data-quality-checker@416ec65453fd280a611065c09272aa5d293a9f33` 的跨领域反馈和 Maintainer Review；正式提交号在人工验收后冻结。

只有 Playbook Maintainer 可以修改或发布 Playbook。实验项目固定所用提交，只提交 Validation、Handoff、Decision/Deviation 和 Feedback，不直接修改规范。

v1.0 发布并完成后续验证前，不封装 Codex Skill。
