# V1 Zero Seed — 总体验证记录

- 状态：`In Progress — Run A 等待 HG-01`
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
| A | `20260922-012919-a` | `ZeroSeedAlpha` / ASCII 短路径 | R2d Passed；等待 HG-01 | `runs/20260922-012919-a/VALIDATION.md` | Run/R1 `473ff1e`；预打开提交待形成 |
| B | 未创建 | `零种子 Beta` / 空格与 Unicode | Not Started |  |  |

## 3. Human Gate

| ID | 状态 | 请求与目标 | Human 确认 | 证据 | 继续授权 |
| --- | --- | --- | --- | --- | --- |
| HG-00 | Passed | 确认规划冻结提交并授权创建首个正式 Run | 用户回复“确认，授权” | `runs/20260922-012919-a/logs/HUMAN_ACTIONS.md` | 是 |
| HG-01 | Pending | 打开 Run A 的精确 `.pbip`，禁止保存/另存为/创建项目 | 等待 Human | 同上 + `manifests/PRE_OPEN.json` | 否 |

## 4. 跨 Run 独立验收

Run A 已完成首开前冻结；Desktop 项仍保持 `Not Started`。

| 验收条款 | A | B | 独立依据 | 结论 |
| --- | --- | --- | --- | --- |
| 空目录 Trusted baseline | Passed | Not Started | 递归清单、目录外记录、Git | A Passed |
| Codex 首开前完整生成 | Passed | Not Started | Schema、不变量、manifest | A Passed；不等于 Desktop 兼容 |
| Desktop 首开/补写分类 | Not Started | Not Started | 真实运行、Human 观察、diff | Not Started |
| 保存/关闭/重开 | Not Started | Not Started | Desktop、manifest、MCP 只读回读 | Not Started |
| 不同名称/路径重复性 | Not Started | Not Started | 跨 Run 对比 | Not Started |

## 5. 最终判定

- 功能结果：Run A `In Progress`；尚无业务结论
- Contract 符合度：Run A R0–R2d 符合；Desktop 阶段未评价
- 证据完整度：Run A 首开前证据完整；Desktop 证据未开始
- 持久化/重启状态：未测试
- 安全与权限状态：Contract 已冻结；运行时未测试
- 已知限制和不能声称的内容：不能声称任何零种子业务结论、Desktop 兼容性、MCP 可用性或 R-VLD-003 utility
- 最终验收提交：`Not Started`
