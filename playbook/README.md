# AI 项目闭环 Playbook

状态：`v0.1`（基于 Power BI Builder V0 提炼，等待 V1-zero-seed 验证）

本目录提供一套证据驱动、分阶段、可停止、可归因的 AI 项目闭环。它规范项目如何冻结目标、隔离运行、逐阶段执行与验证、保存证据并完成交接；具体领域操作放在 `adapters/`，历史依据放在 `case-studies/`。

## 快速入口

1. 阅读 [PLAYBOOK.md](PLAYBOOK.md)，确认核心规则和术语。
2. 复制 [需求模板](templates/REQUIREMENTS.template.md)，在正式运行前冻结需求与验收契约。
3. 用 [验证模板](templates/VALIDATION.template.md)逐阶段记录事实。
4. 用 [记录模板](templates/RECORDS.template.md)登记重大决策和偏差。
5. 完成后填写 [交接模板](templates/HANDOFF.template.md)与 [Playbook 反馈模板](templates/PLAYBOOK_FEEDBACK.template.md)。

执行流程：

```text
Frame → Contract → Prepare → Preflight
                         ↓
       [ Execute → Verify → Gate → Checkpoint ] × N
                         ↓
                    Decide → Handoff & Feedback
```

`Execute` 与 `Verify` 是阶段内循环，不是“全部完成后统一验证”。每个原子变更必须先验证，通过后才能进入下一依赖阶段。

## 规则等级

- `Required`：必须遵守；未遵守时可以继续报告项目结果，但不能声明符合本 Playbook。
- `Provisional`：必须评估并反馈；可以通过明确记录的不适用或受控偏差证明规则不合理。
- `Guidance`：建议做法，可按项目情况选择。

## 角色与维护

- **Playbook Maintainer**：唯一有权修改、升级和发布 Playbook 基线的角色。本项目当前由维护本方法论的 Codex 对话担任。
- **Experiment Owner**：负责某个实验的需求、执行、验证和反馈，不得直接修改固定版本的 `playbook/**`。
- **Human Approver**：在 Human Gate 提供授权、外部应用操作或主观验收。

Power BI V0、V1-zero-seed 和后续非 Power BI 验证均是独立实验。它们只提交结果与反馈，由 Maintainer 决定是否进入下一版本。

## 固定版本顺序

1. Power BI Builder V0 → Playbook v0.1。
2. V1-zero-seed 按 v0.1 执行并反馈。
3. Maintainer 基于 V1 反馈形成 v0.2。
4. 非 Power BI 项目按 v0.2 验证。
5. Maintainer 形成 v1.0。
6. v1.0 验证完成后再封装 Codex Skill。

在 V1 HANDOFF 返回前，v0.1 不升级。阻塞执行的明显错误只能通过单独 erratum 提交修复，并重新声明实验实际固定的基线提交号。

## V1 接入约束

V1 的提交 `22da780` 形成于 v0.1 之前，只是非规范预备草案。v0.1 发布后，V1 应通过 no-ff merge 引入 v0.1 原始提交，随后完成符合性检查并形成新的规划冻结提交；正式 Run 只能在该提交之后开始。V1 不得修改 `playbook/**`。

## 文档边界

- [PLAYBOOK.md](PLAYBOOK.md)：跨领域核心规范。
- [Power BI adapter](adapters/power-bi.md)：未来 Power BI 项目的领域映射。
- [V0 case study](case-studies/power-bi-builder-v0.md)：V0 事实、提交和规则来源。
- [CHANGELOG.md](CHANGELOG.md)：版本规则变化。

执行者无需阅读 Case Study 才能使用 Playbook。
