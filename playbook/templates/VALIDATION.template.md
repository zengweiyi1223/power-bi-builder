# <项目名> — Run <run-id> 验证记录

- 状态：`Not Started / In Progress / Passed / Passed with Limitations / Blocked / Failed`
- Playbook 基线：`<commit>`
- 需求基线：`<commit>`
- Run 起点：`<commit/hash/path>`

本记录只写已核实事实；待执行项保持 `Not Started`，不预填成功结论。

## 1. 环境与安全边界

- 时间与时区：
- 关键工具和版本：
- 目标系统/项目身份：
- 权限及外部连接：
- 敏感信息和脱敏检查：
- 初始 Git 状态与 Rollback point：

## 2. 阶段状态

| 阶段 | 状态 | 执行与验证摘要 | 证据 | DCS/DEV | Checkpoint |
| --- | --- | --- | --- | --- | --- |
| 1 | Not Started |  |  |  |  |

每个阶段按“原子变更 → 自动验证 → 必要人工验证 → Gate 判定 → checkpoint”更新。

## 3. Human Gate

| ID | 请求与目标 | 人工确认 | 时间 | 证据 | 继续授权 |
| --- | --- | --- | --- | --- | --- |
| HG-01 |  |  |  |  |  |

## 4. 独立验收

| 验收条款 | 生成路径结果 | 独立依据 | 差异/容差 | 结论 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 5. 异常与恢复

| 事件 | 类型 | 严重度 | 影响 | 处理 | 是否保留现场 |
| --- | --- | --- | --- | --- | --- |
|  |  | Blocking / Non-blocking / Informational |  | 重试 / 回滚 / 新 Run / 记录后继续 |  |

## 6. 最终判定

- 功能结果：
- Contract 符合度：
- 证据完整度：
- 持久化/重启状态：
- 安全与权限状态：
- 已知限制和不能声称的内容：
- 最终验收提交：
