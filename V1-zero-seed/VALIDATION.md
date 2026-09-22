# V1 Zero Seed — 总体验证记录

- 状态：`In Progress — Run A/B Passed；等待 R7 跨 Run 收口与最终验收提交`
- Playbook 基线：`3ee871d618db84d55b3b2f86a198ac552864317e`
- V1 采用前草案：`22da780412f27decf17a097548d65d151c75b235`
- no-ff merge：`8c28f5e340ec41ef56e16d942fd2f9eb97767963`
- 需求冻结提交：本轮“v0.1 符合性检查及 V1 规划冻结”提交，SHA 由 Git/报告记录
- 正式 Run 起点：Run A `473ff1e1e83cbb21458186468ad853d244ded562`

本文件汇总跨 Run 事实。单个 Run 的原子执行、Human Gate、异常和证据写入其 `runs/<run-id>/VALIDATION.md`。

## 1. 规划 Gate

| 项目 | 状态 | 证据 |
| --- | --- | --- |
| 步骤 1：分支、worktree、Git 清洁检查 | Passed | 接入前 `codex/v1-zero-seed` @ `22da780`，工作树干净；Playbook 独立 worktree @ `3ee871d` |
| 步骤 2：no-ff merge 固定 Playbook | Passed | merge `8c28f5e`，双亲为 `22da780` 与 `3ee871d` |
| 步骤 3：完整阅读 README/PLAYBOOK/templates/adapter | Passed | `BASELINE.md` §3 |
| 步骤 4–6：采用前符合性与模板补齐 | Passed | `PLAYBOOK_CONFORMITY.md`、冻结 Contract 与输出骨架 |
| 步骤 7：规划冻结 checkpoint | Passed | 以包含本文件的独立 Git 提交完成；SHA 由 Git/报告记录 |
| HG-00：正式 Run 授权 | Passed | 用户确认冻结提交 `82b4489` 并明确授权 |

## 2. 正式 Run 状态

| 试验 | Run ID | 项目名/路径特征 | 状态 | 验证记录 | Checkpoint |
| --- | --- | --- | --- | --- | --- |
| A | `20260922-012919-a` | `ZeroSeedAlpha` / ASCII 短路径 | Passed | `runs/20260922-012919-a/VALIDATION.md` | Run/R1 `473ff1e`；预打开 `57b6e64`；首存 `44c2fb7`；核心往返 `9c34b5f`；final 为包含本记录的提交 |
| B | `20260922-032410-b` | `零种子 Beta` / 不同父目录、空格与 Unicode | Passed | `runs/20260922-032410-b/VALIDATION.md` | Run 起点 `21af7b2`；Run/R1 `a121769`；预打开 `6d0a594`；R3 `af23869`；首存 `5428294`；核心往返 `45a0dda`；final 为本轮后续报告的 checkpoint |

## 3. Human Gate

| ID | 状态 | 请求与目标 | Human 确认 | 证据 | 继续授权 |
| --- | --- | --- | --- | --- | --- |
| HG-00 | Passed | 确认规划冻结提交并授权创建首个正式 Run | 用户回复“确认，授权” | `runs/20260922-012919-a/logs/HUMAN_ACTIONS.md` | 是 |
| HG-01 | Passed | 打开 Run A 的精确 `.pbip`，禁止保存/另存为/创建项目 | 成功进入；`Overview` 可见；无提示；标题正确 | Human 日志、截图、首开后 manifest | 是，仅完成 R3 |
| HG-02 | Passed | 显式保存当前项目并正常关闭 Desktop | 保存成功；关闭成功；无提示 | Human 日志、首存 manifest、进程退出检查 | 是，仅完成 R4 |
| HG-03 | Passed | 从同一 `.pbip` 第一次重开，禁止保存和修改 | 稳定重开；页面/标题正确；无提示 | Human 日志、重开 manifest、MCP 日志 | 是，仅完成 R5 |
| HG-04 | Passed A/B | 执行 R-VLD-003 的额外关闭/重开 | A/B 均关闭无提示并再次成功进入；页面/标题正确；无提示/错误/修复；约用几秒 | 各 Run Human 日志、R6 evidence、最终重开 manifest | B 仅允许完成 R6 技术步骤 |
| HG-05 | Passed A/B | 对当前最终可见状态作独立签字式确认 | A/B 的项目标题与 `Overview` 正确；无弹窗、警告、错误或修复提示 | 各 Run Human 日志、R6 evidence | 是；Run B 可形成 final checkpoint |

## 4. 跨 Run 独立验收

Run A/B 均已完成 R0–R6 与适用的 HG-00–HG-05。R7 将只做跨 Run 收口、最终文档与提交，不再执行 Desktop 实验。

| 验收条款 | A | B | 独立依据 | 结论 |
| --- | --- | --- | --- | --- |
| 空目录 Trusted baseline | Passed | Passed | 递归清单、目录外记录、Git | A/B Passed |
| Codex 首开前完整生成 | Passed | Passed | Schema、不变量、manifest | A/B 生成阶段 Passed；不等于 Run B Desktop 兼容 |
| Desktop 首开/补写分类 | 首开 Passed；磁盘补写 0 | 首开 Passed；磁盘补写 0 | 真实运行、Human 观察、diff | A/B 首开均无磁盘补写 |
| 保存/关闭/重开 | 核心往返与额外最终往返均 Passed | 核心往返与额外最终往返均 Passed | Desktop、manifest、MCP 只读回读、最终 Human Gate | A/B Passed |
| 不同名称/路径重复性 | ASCII 短路径样本 Passed | Unicode+空格路径样本 Passed | 独立空目录、独立文件/标识符、不同进程、逐 Run 证据 | 两条计划样本重复验证 Passed |

## 5. 最终判定

- 功能结果：Run A/B `Passed`；等待 R7 文档收口
- Contract 符合度：Run A/B 完整符合
- 证据完整度：A/B R0–R6 技术证据完整；存在已解释的非阻塞 Schema/Product 缺口
- 持久化/重启状态：A/B 核心往返与额外最终往返均技术通过；最后一次重开磁盘零差异
- 安全与权限状态：Contract 已冻结；A/B 未访问敏感信息、未发布、MCP 仅只读
- 已知限制和不能声称的内容：R7 与最终验收提交前不能声称 V1 文档收口完成；不能声称两条样本之外的普遍兼容性、`.platform` 反事实必要性，或用规则符合性证明规则有效性
- 最终验收提交：`Not Started`
