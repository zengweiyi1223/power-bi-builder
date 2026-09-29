# <项目名> — 实施与交付计划

- 状态：`Draft / Ready / In Progress / Complete`
- Contract：`<commit/version>`
- Design：`<commit/version or N/A>`
- 当前滚动状态：[VALIDATION](<path>)

本计划描述任务依赖和完成定义；实际通过状态只在 VALIDATION 维护。

## 1. 排序依据

1. 先消除权限、环境、不可逆操作等阻塞；
2. 尽早验证高代价或高不确定性假设；
3. 建立最小端到端闭环；
4. 再从低耦合增量扩展到复杂集成。

- 本项目与默认排序不同的地方及理由：

## 2. 可验证增量

| Task ID | 产物/目标 | 依赖 | Owner / Executor | 完成定义 | 验证与证据 | 风险/停止条件 | Checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T-01 |  |  |  |  |  |  |  |

任务必须小到能够独立判定；若一个任务失败后无法确定原因或安全恢复，应继续拆分。

## 3. Gate 与人工等待点

| Gate | 触发任务 | Approver | 需要确认的内容 | 未批准时 |
| --- | --- | --- | --- | --- |
| HG-01 |  |  |  | 不进入依赖任务 |

## 4. Preflight 与准备

- 环境、版本和工具能力：
- 目标身份、账号和权限：
- 输入、baseline、工作副本和临时目录：
- Oracle、fixture、量表和证据位置：
- 初始 rollback point：
- 外部依赖、费用和可用性：

## 5. 变更控制

- 允许不改 Contract 的计划调整：
- 必须记录 Decision 的调整：
- 必须回到 Contract / Design 的调整：
- Blocking 后原地重试、回滚或新 Run 的判断：
