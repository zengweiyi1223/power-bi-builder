# Power BI Adapter

本文件把 Playbook v1.0 映射到未来 Power BI 项目。它不替代项目自己的 Contract，也不把 V0/V1 的单版本观察、当前工具说明或未执行路线冒充为普遍规律。

## 1. Trusted baseline 与项目生成

- Trusted baseline 可以是已验证 PBIP/PBIR 种子，也可以是有来源证据的空目录；由实验问题决定，核心方法不预设种子必要。
- 当前 V1 证据证明最小项目可以从空目录生成并直接打开，但不证明所有复杂模型、版本和数据源均无需模板。
- 种子存在时保持不可变，复制完整项目到唯一 `runs/<run-id>/project/` 后操作。
- `.pbip`、Report、SemanticModel 的名称和相对引用必须一致；正式项目使用业务名称，不沿用 `Seed`。
- `.pbi` 本机设置、缓存和自动恢复文件属于机器状态，不作为正式项目源文件。

## 2. Contract 应冻结的 Power BI 边界

- Desktop、PBIP/PBIR/TMDL、可选 Modeling MCP、Power BI Service 和浏览器插件的实际版本与适用范围。
- 数据源、编码、区域、类型、凭据和刷新边界。
- 表、列、关系、度量值、格式和字段绑定名称。
- 页面、视觉对象、布局和交互要求。
- 外部修改批次属于 PBIR-only、TMDL-only 还是混合批次。
- 目标对象在当前 Desktop 会话中是否已存在并加载。
- Desktop 是否可能持有未保存的内存修改。
- 打开、首次保存、关闭—重开、Apply external changes 和视觉确认的 Human Gate。
- Service、发布/分享、跨机器迁移、网关、浏览器插件和 MCP mutation 是否属于范围。

## 3. Desktop 生命周期状态

| 状态 | 已验证含义 | 默认风险控制 |
| --- | --- | --- |
| Generated / never opened | 磁盘项目由 Codex 生成；最小 V1 项目可直接首开 | 首开前静态验证与 Git checkpoint |
| First opened / never saved | Desktop 已加载项目，但外部变更监听不一定可用 | 不假设热重载；避免让 Desktop 覆盖外部修改 |
| First save pending | Desktop 可能规范化文件、写入 lineage/platform 元数据并以内存覆盖磁盘 | 保存前 checkpoint；保存作为 Human Gate；保存后 manifest/diff |
| Saved but same process | V1 中首次保存本身没有让外部变更检测生效 | 不把保存等同于完成初始化 |
| Saved and reopened | V1 中已加载 PBIR 文件修改可触发 Apply | 仅对已测试对象和版本成立 |
| Unsaved Desktop edits | 内存与磁盘可能分叉 | 先决定保存、放弃或关闭；不得盲目外部覆盖 |
| Desktop closed | 磁盘是外部文件修改的可靠边界 | 适合 TMDL 或混合批次，修改后重开验收 |

这些状态是路线选择信息，不是要求每个项目逐项经历所有状态。

## 4. 路线选择

### 4.1 首次完整交付

```text
Codex 生成完整项目 → 静态验证/checkpoint → Human 打开 → 必要刷新或凭据 Gate → 验收
```

项目能首开不等于必须首存。若后续需要 PBIR 热迭代，可把首次保存、关闭和重开作为一次初始化路线；保存前必须 checkpoint，保存后检查 manifest 和业务语义。

### 4.2 PBIR-only：已存在且已加载对象

在已完成所需初始化、Desktop 没有未保存编辑时：

```text
Codex 批量修改已有 PBIR → Human Apply external changes → 验收
```

V1 中成功 Apply 的纯外部 PBIR 修改已经存在磁盘，关闭后无需为了持久化额外保存。若 Human 随后在 Desktop 内编辑，则仍需保存内存修改。

### 4.3 PBIR：会话中新建、尚未加载对象

V1 的一个新视觉在当前会话中未被发现，首次保存也未使其进入监控。安全路线是关闭—重开，让 Desktop 从磁盘加载新对象后再迭代。该观察不能外推到所有页面和对象类型。

### 4.4 包含 TMDL 的批次

当前已验证的默认路线：

```text
Desktop 关闭 → Codex 修改 TMDL（可同时修改 PBIR）→ checkpoint → Human 重开 → 模型与报表共同验收
```

V1 的一个 measure 修改没有随 Apply 热加载，但重开后生效。因此不能声称所有 TMDL 都必须重开；在没有更强对象级证据前，重开是保守的已验证边界。混合批次先 Apply PBIR 对达到最终组合状态是冗余操作。

### 4.5 Desktop 或 MCP 内存修改

人工或工具在 Desktop 内存模型中产生的修改必须保存后才算磁盘持久化。MCP mutation 的具体连接、保存和恢复流程应引用 V0 或另行验证，不能由 V1 的无 MCP 文件工作流推导。

## 5. 首次保存是覆盖风险 Human Gate

首次保存不是零种子项目“能够打开”的前置条件，但可能是宿主所有权和规范化边界：

1. 保存前确认正确项目身份、Desktop 内存状态和磁盘目标。
2. 建立 Git checkpoint，确保外部磁盘修改可恢复。
3. Human 明确执行保存，不由 AI 推测完成。
4. 保存后生成 manifest/diff，区分等价序列化、默认元数据、平台信息、业务语义和未解释变化。
5. 若保存覆盖了计划中的外部修改，停止后续依赖步骤并从 checkpoint 恢复或重新生成。

## 6. 项目级设置优先记录在项目中

当 Power BI 提供可写入模型或项目文件的当前文件设置时，优先显式写入并验证，而不是依赖机器全局偏好。V1 只直接验证了模型级 `__PBI_TimeIntelligenceEnabled = 0` 在目标 Desktop 版本上控制 Auto date/time，并经过保存、关闭和重开保持；其他设置必须分别验证。

## 7. 工具路线选择

不要把“Power BI 插件”当成覆盖所有 Power BI 对象的统一能力。先按工作对象选路线：

| 工作对象 | 适用路线 | 能力边界 | 证据状态 |
| --- | --- | --- | --- |
| 本地文件、PBIP、PBIR、TMDL | 文件、代码、Schema 和版本控制工具 | 生成、修改和静态验证磁盘项目；不能单独证明 Desktop 或 Service 已接受 | V0/V1 observed |
| Power BI Desktop 内存模型与本地产品回读 | Desktop 人工操作；可选 Modeling MCP | 本地会话、模型对象、DAX 与保存边界；必须区分内存和磁盘状态 | V0/V1 部分 observed |
| Power BI Service 报告、视觉对象、dashboard、workspace、app 和分享 | Power BI 浏览器插件，在受支持的本地浏览器运行环境中执行 | 面向浏览器 Service；不编辑本地 PBIX/PBIR，不等同于 API 或 Desktop 自动化 | 当前工具说明；V0/V1 未验证 |
| REST API、后台集成、网关或本地应用自动控制 | 对应 API、CLI 或专用工具 | 必须单独核实认证、权限、幂等、费用和回滚 | 本 Playbook 未验证 |

使用 Power BI 浏览器插件时：

1. 先确认这是 Power BI Service，而不是 Desktop 或 Report Server。
2. 在读取或修改前核对可见账号、tenant、workspace、对象类型和权限；拒绝访问不等于空结果。
3. 区分 report、page、visual、dashboard/tile、semantic model 和 Power BI app；浏览器可见内容不代表底层 SQL、DAX 或完整数据均可访问。
4. 编辑、保存、分享、发布 app、改变权限和创建公开链接是不同动作。共享写入、覆盖和公开暴露必须分别获得 Human Gate。
5. 保存或发布后重开精确对象并验证版本、内容、筛选和可见状态；不要因结果不明确而重复创建。
6. `Publish to web` 会形成公开暴露，不能作为普通组织内分享使用。

以上是能力路由和安全边界，不是 V0/V1 的实验成功结论。首次正式使用时必须建立独立 Validation 和反馈。

## 8. Modeling MCP 定位

- MCP 不是生成完整 PBIP/PBIR/TMDL 项目的必要前置条件；V1 的项目生成和文件修改未依赖 MCP mutation。
- MCP 仍可作为复杂、多轮模型工程的效率路径，用于内存模型修改、对象回读和 DAX 验收。
- 一旦 MCP 改变 Desktop 内存状态，应按 Desktop 内存修改处理：保存、关闭—重开或其他持久化验证由 Contract 明确。
- “本项目没使用 MCP”不能推导为“MCP 没有价值”或“MCP mutation 已验证失败”。

## 9. 独立验收与证据

- 数值结果优先从原始输入独立计算，不复用 DAX 输出。
- MCP List/Get、DAX、Partition 状态或等价回读用于系统语义验证。
- PBIP/PBIR JSON、Schema、引用、字段绑定、manifest 和布局用于静态检查。
- Desktop 打开、交互、Apply、保存和重开用于真实运行验证。
- 截图用于视觉和交互观察，不替代精确数值日志。
- 重复无变化观察可以使用状态转换表压缩；首次转换、覆盖事件、Blocking 和最终状态保留完整证据。
- Desktop canonical 输出与公开 Schema 不一致时，分别保留直接校验、兼容性/辅助校验和产品运行证据；不得把辅助校验冒充精确 conformance。

## 10. Human Gate 与操作计量

常见 Gate 包括首开、真实刷新/凭据、首次保存、关闭—重开、Apply 和最终视觉确认。每次确认应记录目标项目身份和禁止动作。

只有在项目声称最少人工或效率改进时，才需要在 Gate 发出时记录 Human active、wait 和 machine time。实验中的失败诊断、重复观察和持久化证明必须与推荐生产步骤分开统计。

## 11. 停止与归因

- 数据未刷新时不得进入依赖其结果的模型、DAX 或报表验收。
- 高风险首次保存前没有 checkpoint 时暂停，而不是冒险继续。
- PBIR Apply 成功不证明 TMDL 已重载；必须分别验证模型和报表结果。
- Schema 通过不代表 Desktop 通过；Desktop 自动修复也不能冒充完整成功。
- MCP 能力缺失、环境阻塞、实现错误、宿主覆盖、对象未加载、证据缺口和治理阻塞应分别归因。
