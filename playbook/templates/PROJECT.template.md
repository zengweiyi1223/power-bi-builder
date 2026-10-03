# <项目名> — 项目入口与裁剪

- 状态：`Draft / Active / Complete / Archived`
- Playbook：`v1.0.1@<commit>`
- 项目基线或当前稳定版本：`<commit/version>`
- 当前滚动状态：[VALIDATION](<path>)
- 执行恢复入口：[VALIDATION 当前控制状态](<path-to-current-control-state>)
- 最终交付或最近稳定状态：[HANDOFF](<path>)
- AI 指令入口：`<AGENTS.md / equivalent / N/A + reason>`

## 1. 项目摘要

- 一句话目标：
- 目标用户/使用者：
- 主要交付：
- 当前阶段：
- 明确非目标：

本节只给稳定摘要；详细 Why、范围和验收以 REQUIREMENTS 为准，动态状态以 VALIDATION 为准。

## 2. 项目画像与风险修饰器

| 项目 | 选择 | 理由 |
| --- | --- | --- |
| 基础画像 | PF-EXP / PF-DOC / PF-DAT / PF-CMP / PF-APP / PF-SVC |  |
| 启用修饰器 | MD-UI / MD-DATA / MD-EXT / MD-DEPLOY / MD-OPS / MD-SEC / MD-MULTI / MD-HIGH |  |
| 未启用或条件式修饰器 |  |  |

## 3. 生命周期裁剪

| Stage | 适用性 | 触发或 N/A 理由 | Owner / Approver | 权威记录 | Exit Gate |
| --- | --- | --- | --- | --- | --- |
| Profile & Tailor | Required |  |  | 本文件 |  |
| Discover & Frame | Required |  |  | REQUIREMENTS |  |
| Contract | Required |  |  | REQUIREMENTS |  |
| Design | Required / Conditional / N/A |  |  | TECH_DESIGN / Decision |  |
| Plan & Prepare | Required / Conditional |  |  | DELIVERY_PLAN / TECH_DESIGN |  |
| Implement & Verify | Required |  |  | VALIDATION |  |
| Integrated Acceptance | Required |  |  | VALIDATION / UAT |  |
| Release / Delivery | Required |  |  | RELEASE / HANDOFF |  |
| Operate / Observe | Required / Conditional / N/A |  |  | RUNBOOK / VALIDATION |  |
| Handoff / Close / Learn | Required |  |  | HANDOFF |  |

## 4. 人机责任

| 角色 | 可识别主体 | Owner / Executor / Reviewer / Approver | 权限与禁止事项 |
| --- | --- | --- | --- |
| Project Owner |  |  |  |
| AI |  | AI Draft / AI Execute / AI Recommend |  |
| Human |  | Human Review / Human Approve / Human Execute |  |
| Automation |  |  | 输出不能自行批准 Gate |

## 5. Artifact Map

| 逻辑记录/资产 | 实际路径或系统 | 权威内容 | 生命周期 |
| --- | --- | --- | --- |
| PROJECT |  | 画像、角色、阶段裁剪、导航 | 稳定入口 |
| AI 指令入口 |  | 阅读顺序、权限边界和已验证命令 | 条件式稳定入口 |
| REQUIREMENTS |  | Why、范围、验收、安全、Gate | 冻结版本 |
| TECH_DESIGN |  | 方案、接口、风险与验证设计 | 条件式冻结版本 |
| DELIVERY_PLAN |  | 任务、依赖、完成定义和 checkpoint | 实施前及受控更新 |
| VALIDATION |  | 唯一滚动状态、证据和异常 | 滚动更新 |
| HANDOFF |  | 最终结论、入口、限制和恢复 | 里程碑形成 |
| 实现/内容 |  |  |  |
| 测试/Oracle |  |  |  |
| Evidence |  |  |  |
| 临时/可重建内容 |  | 不作为唯一证据 |  |

## 6. 协调模式

- 默认模式：`Human Relay / Automatic Orchestration`
- 选择理由与成本边界：
- 最小转移包位置：`<通常为 VALIDATION 当前控制状态或 HANDOFF 摘要>`

## 7. 根目录导航

```text
<只列真实使用的目录与用途；不要为了模板预建空目录>
```

物理文件可以合并，但 Artifact Map 必须指出对应章节。动态阶段状态不要在本文件和 VALIDATION 中重复维护。
