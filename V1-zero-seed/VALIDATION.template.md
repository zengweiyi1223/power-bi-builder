# V1 Zero Seed — Run <run-id> 验证记录

- 状态：`Not Started / In Progress / Passed / Passed with Limitations / Blocked / Failed`
- Playbook 基线：`3ee871d618db84d55b3b2f86a198ac552864317e`
- 需求冻结提交：`<commit>`
- Run 起点：`<commit/hash/path>`
- 项目名与绝对路径：`<name/path>`

本记录只写已核实事实；待执行项保持 `Not Started`，不预填成功结论。

## 1. 环境与安全边界

- 时间与时区：
- Desktop / MCP / OS / 文件系统版本：
- 目标项目身份：
- 权限与外部连接：
- 敏感信息和脱敏检查：
- 初始 Git 状态与 rollback point：
- Trusted baseline 空目录证据：
- 来源及禁止来源确认：

## 2. Execute–Verify 阶段

| 阶段 | 状态 | 原子 Execute | 立即 Verify | Gate 判定 | 证据 | DCS/DEV | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R0 Run/Preflight | Not Started |  |  |  |  |  |  |
| R1 空目录 | Not Started |  |  |  |  |  |  |
| R2a PBIP 入口 | Not Started |  |  |  |  |  |  |
| R2b SemanticModel | Not Started |  |  |  |  |  |  |
| R2c Report/PBIR | Not Started |  |  |  |  |  |  |
| R2d 预打开冻结 | Not Started |  |  |  |  |  |  |
| R3 首开 | Not Started |  |  |  |  |  |  |
| R4 首存 | Not Started |  |  |  |  |  |  |
| R5 第一次重开 | Not Started |  |  |  |  |  |  |
| R6 最终往返 | Not Started |  |  |  |  |  |  |

## 3. Human Gate

| ID | 请求、目标与预期 | Human 实际确认 | 时间 | 证据 | 继续授权 |
| --- | --- | --- | --- | --- | --- |
| HG-00 |  |  |  |  |  |
| HG-01 |  |  |  |  |  |
| HG-02 |  |  |  |  |  |
| HG-03 |  |  |  |  |  |
| HG-04 |  |  |  |  |  |
| HG-05 |  |  |  |  |  |

## 4. 独立验收映射

| Contract 条款 | 生成路径结果 | 独立依据 | 证明等级 | 差异/容差 | 结论 |
| --- | --- | --- | --- | --- | --- |
| 空目录 |  | 递归清单与目录外记录 | 精确 / 辅助 / 人工观察 |  |  |
| 项目入口和引用 |  | Schema、不变量、路径解析 |  |  |  |
| Desktop 首开 |  | 真实运行、Human 观察、磁盘 diff |  |  |  |
| 首存持久化 |  | manifest、Git diff、离线复验 |  |  |  |
| 重开稳定性 |  | Desktop、MCP 只读回读、最终 manifest |  |  |  |

## 5. Desktop 保存前后差异

| 路径 | 阶段 | 差异摘要 | 分类 | 结构/语义影响 | 证据 |
| --- | --- | --- | --- | --- | --- |

## 6. 异常与恢复

| 事件 ID | Playbook 类型 | 严重度 | V1 主因 | 影响 | 处理 | 保留现场 | 证据 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Blocking / Non-blocking / Informational |  |  | 重试 / 回滚 / 新 Run / 继续 / 停止 |  |  |

## 7. R-VLD-003 成本与价值

| 指标 | Core roundtrip | Playbook-only final roundtrip |
| --- | ---: | ---: |
| Desktop 启动次数 |  |  |
| Human 主动分钟 |  |  |
| 等待分钟 |  |  |
| 机器检查分钟 |  |  |
| 新增证据文件/字节 |  |  |
| 唯一发现 |  |  |

- 省略 final roundtrip 的反事实风险：
- Utility：`Helpful / Neutral / Burdensome / Harmful`
- 建议：`Keep / Change / Retire / Move`
- 说明：Conformity 与 Utility 分开评价。

## 8. Run 最终判定

- 功能结果：
- Contract 符合度：
- 证据完整度：
- 持久化/重启状态：
- 安全与权限状态：
- 已知限制和不能声称的内容：
- Run 最终 checkpoint：
