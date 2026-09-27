# V1 — 最少人工步骤与人机协作工作流交接

状态：**四项实验完成，V1 可交接给 Playbook v0.2 总结。**

- Playbook 固定基线：`v0.1` @ `3ee871d618db84d55b3b2f86a198ac552864317e`
- 零种子最终验收：`c9003aaf29056edac67be88e9f9cf6745816a9cd`
- 自动日期/时间最终提交：`77a188f20f85a614a7a2774ecb64fa6426411fa6`
- PBIR 热重载最终提交：`8732141fa58d6314c0b17e31116f2b0db5296d71`
- 最少人工工作流最终提交：`8a005159aa2b739ecc4a399405b2caecb3a752f6`
- V1 首次统一归档提交：`e76373310b6f2f0a4194d5a737d890966d1510a8`

本文件只汇总 V1 已有结果、证据边界和改进建议，不修改 Playbook v0.1，也不创建 Playbook v0.2。

## 1. V1 问题与结论

V1 验证的整体问题是：Codex 能否从空目录直接生成完整 Power BI Project，并把长期协作中的人工操作压缩到最低。

综合结论：

- 在已测试环境中，Codex 可以从空目录直接生成可由 Desktop 打开、保存和重开的 PBIP/PBIR/TMDL 项目，不需要人工创建空白 PBIP 种子。
- 当前文件的自动日期/时间可以通过模型级 `__PBI_TimeIntelligenceEnabled = 0` 显式关闭，并在 Desktop 保存和重开后保持。
- 已被当前 Desktop 会话加载的 PBIR 视觉文件可以在外部修改后通过 **Apply external changes** 应用；成功应用的纯外部 PBIR 修改无需额外保存。
- 本次测试的 TMDL 度量值外部修改没有随同一次 Apply 完成模型热重载，关闭并重开后才得到最终值。因此，包含 TMDL 的批次当前应使用关闭—重开作为可靠验收边界。
- MCP 没有参与 V1 的项目生成或模型修改，说明它不是生成完整项目的必要条件；V1 不据此声称已经验证 MCP 模型写入工作流。

V1 的综合结果不是“所有内容都可热重载”，而是：**完全零种子；PBIR 已加载视觉可 Apply；测试过的 TMDL 修改需要重开。**

## 2. 四项实验与证据入口

| 阶段 | 结果 | 已证明 | 主要入口 |
| --- | --- | --- | --- |
| 01 Zero Seed | Passed — 完全零种子 | 两组独立空目录、不同名称和路径均可首开、保存、关闭和稳定重开 | [Validation](experiments/01-zero-seed/results/VALIDATION.md) · [Handoff](experiments/01-zero-seed/results/HANDOFF.md) · [Feedback](experiments/01-zero-seed/results/PLAYBOOK_FEEDBACK.md) |
| 02 Auto Date Setting | Passed | 模型级 annotation 可控制当前文件选项并持久化 | [Validation](experiments/02-auto-date-setting/results/VALIDATION.md) · [Final Result](experiments/02-auto-date-setting/results/FINAL_RESULT.md) |
| 03 Live PBIR Reload | Partial success with material boundary | 已加载视觉可 Apply；会话中新增且从未加载的视觉没有被发现 | [Final Result](experiments/03-live-pbir-reload/results/FINAL_RESULT.md) · [Handoff](experiments/03-live-pbir-reload/results/HANDOFF.md) · [Feedback](experiments/03-live-pbir-reload/results/PLAYBOOK_FEEDBACK.md) |
| 04 Minimal Human Workflow | Report-only hot pass; TMDL restart pass | 数据绑定卡片可零种子生成；PBIR 标题 Apply 成功；TMDL 值在重开后生效 | [Final Result](experiments/04-minimal-human-workflow/results/FINAL_RESULT.md) · [Handoff](experiments/04-minimal-human-workflow/results/HANDOFF.md) · [Feedback](experiments/04-minimal-human-workflow/results/PLAYBOOK_FEEDBACK.md) |

实验的 `planning/` 保存冻结需求和路线；`results/` 保存结论；`project/`、`evidence/`、`logs/` 和 `manifests/` 只在需要复核具体声明时读取。零种子的 A/B 项目和证据位于各自 `runs/` 内。

## 3. 当前最少人工工作流

### 3.1 首次完整交付

技术上已经证明完整项目可以直接打开和渲染，不以 Desktop 首次保存为“可打开”的必要条件。对于长期协作，建议采用稳定基线流程：

`Codex 生成完整项目 → Human 打开验收 → 必要时处理真实刷新/凭据 Gate → 保存 → 关闭`

这里的首次保存是长期协作建议，不是零种子成立条件。它让 Desktop 写入规范化、lineage、平台和布局元数据；保存前应保留 Git checkpoint，因为 Desktop 可能用内存状态覆盖磁盘文件。

### 3.2 Codex 修改模型文件

对于包含 TMDL 的外部修改批次，当前可靠路径是：

`Desktop 关闭 → Codex 修改 TMDL（可同时修改 PBIR）→ Human 重开并验收`

文件已由 Codex 写入磁盘，纯外部修改不要求 Human 为持久化再保存。若 Human 随后在 Desktop 内继续修改，则应保存该部分内存修改。

### 3.3 Codex 修改已有视觉

完成首次初始化并让目标视觉被 Desktop 加载后：

`Desktop 保持打开 → Codex 批量修改已有 PBIR → Human Apply external changes → 验收`

成功应用后无需额外保存。若运行中新增此前未被会话加载的视觉，当前安全路径仍是关闭—重开；V1 没有证明任意新视觉都能被热发现。

### 3.4 人工或工具在 Desktop 内修改

人工在 Desktop 内修改的内容必须保存。MCP 或其他建模工具如果改变 Desktop 的内存模型，也应在完成后保存；但这项 MCP 写入流程不是 V1 的直接实验结论，应与 V0 证据或后续专项验证分开评价。

## 4. Human、Codex 与 MCP 边界

- Human：负责明确授权的 Desktop Gate，包括打开、必要刷新、首次保存、关闭—重开、Apply 和最终验收。
- Codex：负责生成和修改磁盘上的 PBIP/PBIR/TMDL、静态验证、manifest、Git checkpoint 和证据记录。
- MCP：V1 零种子阶段只做过只读回读，后续三个实验没有执行 MCP mutation。V1 只证明“不依赖 MCP 也能完成生成和文件迭代”，不证明 MCP 没有价值。
- 持久化规则：磁盘外部修改已经落盘；Desktop 内部或工具写入内存的修改需要保存。

## 5. Rule conformity 与 utility

- 零种子正式 A/B Run 对 Playbook v0.1 Required Rules 的结论为 `Conformant`。三个后续实验是独立聚焦验证，不把它们表述为同一份 Contract 下的额外 Run。
- 高价值规则：空目录与来源证明、冻结 Contract、Execute–Verify、Human Gate、操作主体分离、首存/外部批次前 Git checkpoint、精确 manifest 和多维 Handoff。
- R-VLD-003 在两次零种子 Run 中均符合，但强验证完成后的额外最终往返没有产生新发现，仅增加少量重复性信心；utility 为 `Low positive marginal value`。
- 后续最有价值的诊断信息来自生命周期状态：是否首次保存并重启、目标对象是否已经加载、修改批次是 PBIR-only 还是包含 TMDL、Desktop 是否持有未保存内存状态。
- 记录每次重复的“无横幅/无动作”状态产生了明显证据量；状态转换表可能比逐次长记录更经济。

符合规则只证明执行符合性，不等同于规则具有同等实际价值。

## 6. 提交给 Playbook v0.2 的建议

以下仅为 V1 观察和建议：

1. 将外部修改路线明确拆分为 PBIR-only 与包含 TMDL 两类。
2. 把 Desktop 首次保存定义为具有覆盖风险的生命周期 Gate：保存前 Git checkpoint，保存后 manifest；需要 PBIR 热迭代时再完成关闭—重开初始化。
3. 对 PBIR 区分“已加载对象修改”和“会话中新增、尚未加载对象”。
4. 对包含 TMDL 的批次，将关闭—重开作为当前默认验证路径，不强制先做一次冗余 Apply。
5. 将 R-VLD-003 从低风险项目的无条件再次往返改为风险触发或抽样；复杂、高风险或存在未解释差异的宿主仍保留强验证。
6. 在 Human Gate 发出时开始记录 active/wait/machine 时间，避免事后估算验证成本。
7. 区分生产必需操作、诊断操作和仅为持久化证明而增加的操作，不把实验步骤全部写成生产流程。
8. 用紧凑状态转换表记录重复的无动作观察，同时保留 Blocking 事件、覆盖风险和最终验收的完整证据。
9. 将可显式写入模型的当前文件设置优先作为项目文件要求，而不是依赖机器全局偏好。
10. 将 MCP 描述为复杂模型工程的可选效率路径，而不是生成 PBIP 项目的前置条件；其写入、保存和恢复边界需要引用已有证据或单独验证。

这些建议是否进入 v0.2，应由 Playbook Maintainer 基于 V0、V1 和规则目标独立决定。

## 7. 已知限制与不能声称

- 环境集中在 Windows 和 Power BI Desktop `2.157.1354.0`；不能外推到所有版本、操作系统和语言环境。
- 零种子 A/B 是最小空项目；综合实验使用计算 `DATATABLE`、一个 measure 和一个绑定卡片，不代表复杂业务模型和真实凭据数据源。
- 只测试了少量已有 PBIR 对象和一个 TMDL measure 修改；没有证明所有视觉、页面、表、关系或模型对象具有相同行为。
- 会话中新增但从未加载的视觉没有被热发现；不能声称任意 PBIR 新对象都无需重开。
- V1 没有执行 MCP 模型 mutation，不能用本项目证明复杂 MCP 建模、实时回读和保存链已经完成验证。
- 未验证 Power BI Service、发布、跨机器迁移、长路径和所有凭据绑定场景。
- Desktop canonical 根文件与公开 Schema 的 `$schema` 差异仍是已记录的非阻塞证据缺口。

## 8. 归档与冻结说明

- `V0/**` 和 `playbook/**` 在 V1 实验与本次归档中保持不变。
- 四项实验最初在独立分支和目录执行，当前统一归档到 `V1/experiments/`；Git 历史保留原始路径和提交。
- 运行记录中的旧绝对路径反映执行当时现场，不因归档迁移而重写。
- `.work/`、`.pbi/`、自动恢复和其他机器本地缓存不是正式项目交付物；归档只保留已跟踪项目、证据和日志。
