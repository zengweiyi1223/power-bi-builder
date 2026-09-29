# <项目名> — Run / Change Set <id> 验证记录

- 状态：`Not Started / In Progress / Passed / Passed with Limitations / Blocked / Failed`
- Playbook 基线：`<commit>`
- Contract 基线：`<commit/version>`
- 起点与 Rollback point：`<commit/hash/path>`

这是当前阶段状态的唯一权威记录。只写已核实事实；待执行项保持 `Not Started`，不预填成功结论。

## 1. 环境与安全边界

- 时间与时区：
- 关键工具和版本：
- 目标系统/项目身份：
- 权限及外部连接：
- 敏感信息和脱敏检查：
- 初始 Git/工作区状态：

## 2. 当前控制状态

- 最后更新时间与执行者：
- 当前 Stage：
- 当前 Task / Change Set：
- 当前允许执行：
- 当前禁止执行：
- 当前 Blocker：
- 下一 Gate / Approver：
- 最新有效证据：
- 最新 Rollback point：
- 恢复握手：`已读取 Playbook 基线、根入口、Contract 和本记录；状态一致 / 存在冲突`

新会话、恢复或执行者切换时，必须在首次修改前核对并复述本节。信息缺失、冲突或过期时先记录 `Evidence Gap` / `Governance Failure`，不得凭聊天记忆继续。

## 3. 生命周期阶段状态

| Stage | 适用性 | 状态 | 执行与验证摘要 | 证据 | DCS/DEV | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- |
| Profile & Tailor | R/C/N/A |  |  |  |  |  |

## 4. 原子增量

| Task ID | 变更 | 自动验证 | 必要人工验证 | Gate 结论 | 证据 | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- |
| T-01 |  |  |  |  |  |  |

每个增量按“变更 → 自动验证 → 必要人工验证 → Gate 判定 → checkpoint”更新。失败不得进入依赖任务。

## 5. Human Gate

| ID | 请求与目标 | 目标身份/版本 | 人工确认 | 证据 | 继续授权 |
| --- | --- | --- | --- | --- | --- |
| HG-01 |  |  |  |  |  |

仅在 Contract 声明效率或最少人工目标时填写：

| Gate/阶段 | 发出时间 | 完成时间 | Human active | Wait | Machine time | 口径 |
| --- | --- | --- | --- | --- | --- | --- |
| HG-01 |  |  |  |  |  |  |

## 6. 验收条款与独立证据

| AC ID | 生成/实现结果 | 独立依据 | 差异/容差 | 证据 | 结论 |
| --- | --- | --- | --- | --- | --- |
| AC-01 |  |  |  |  |  |

## 7. 异常、归因与恢复

| Event ID | 类型 | 严重度 | 影响 | 处理 | 恢复/新 Run | 现场证据 |
| --- | --- | --- | --- | --- | --- | --- |
| EVT-001 | Validation / Environment / Safety-Permission / Governance / Evidence Gap / Expected Negative / Warning | Blocking / Non-blocking / Informational |  |  |  |  |

## 8. 状态转换与证据压缩

相同方法下重复的无变化观察可以合并；首态、末态、首次转换、Blocking 和异常必须保留完整证据。

| 转换 | 前态 | 动作 | 后态 | 重复次数 | 证据 | 异常/残余风险 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## 9. 操作用途

| 操作 | Production 必需 | Conditional | Diagnostic | Validation-only | 说明 |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 10. 当前或最终判定

- 功能结果：
- Contract 符合度：
- 证据完整度：
- 构建/发布/运行/持久化状态：
- 安全与权限状态：
- 当前 Blocker 或下一 Gate：
- 已知限制和不能声称的内容：
- 当前/最终验收提交：
