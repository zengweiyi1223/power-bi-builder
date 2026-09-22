# Power BI Builder — V1 Zero Seed

状态：**仅完成规划，尚未启动 Power BI Desktop 或正式实验。**

## 核心问题

验证 Codex 能否从一个经证明为空的目录，直接生成可被 Power BI Desktop 打开、保存、关闭并重新打开的 PBIP/PBIR/TMDL 项目，从而判断人工创建空白 PBIP 种子是否仍然必要。

本实验只改变“项目壳的来源”。V0 的需求、种子和正式运行产物保持冻结，不作为 V1 项目模板。

## 三种结论

| 结论 | 定义 |
| --- | --- |
| 完全零种子 | Codex 在 Desktop 首次启动前生成完整项目；至少两组不同名称和路径的项目均可无修复地打开、保存和重开，且不依赖 Desktop 补齐必需工程结构。 |
| Desktop 首次补写 | 无需人工创建或另存为空白项目，Codex 生成物可以进入 Desktop，但 Desktop 首开或首次保存必须补齐、升级或修复必需结构后才能稳定重开。 |
| 仍需人工种子 | 至少一个可归因于项目结构的重复实验无法直接打开或稳定重开，只有人工先创建有效 PBIP/PBIR 工程壳才能继续。 |

环境故障、操作失误、MCP 不可用和路径权限问题不会直接被判为“仍需人工种子”；必须先按实验计划完成归因。

## 文档地图

- [BASELINE.md](BASELINE.md)：当前 Git 基线、V0 历史对照和污染边界。
- [REQUIREMENTS.md](REQUIREMENTS.md)：范围、约束、验收标准和最终分级规则。
- [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md)：双路径实验矩阵、阶段闸门、差异分析和失败归因。
- [RUN_RECORD_TEMPLATE.md](RUN_RECORD_TEMPLATE.md)：每次正式运行的目录与分离式操作记录模板。
- [runs/README.md](runs/README.md)：正式运行目录规则；当前不创建任何项目壳。

## 执行闸门

本目录中的文档不授权启动 Desktop。开始正式实验前应先确认规划，然后为每个试验创建新的 `runs/<run-id>/`。任何试验的 `project/` 必须从空目录开始，且在首次 Desktop 打开前完成文件清单、SHA-256 清单和 Git 快照。
