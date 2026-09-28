# 非 Power BI 验证项目选择

- 状态：`Selected; contract not yet frozen`
- 项目代号：`data-quality-checker`
- 正式 Playbook：`v0.2@dff3a717d59935697e310a29caf6b29dff11ff11`
- 生命周期设计基线：`4f4e7348cb75541c5451bb3133b5816a6c53ed77`

本文只冻结验证项目的选择和边界。具体需求、技术路线、验收样本、角色和计时口径由新项目在 `STG-00` 至 `STG-04` 中形成并提交；不得为了提高方法符合度预填成功结论。

## 1. 项目目标

构建一个浏览器本地运行的 CSV 数据质量检查器，同时验证：

1. 一个小型非 Power BI 项目能否完整执行候选生命周期；
2. 检查能力能否作为独立 Core 被其他界面、CLI 或服务复用；
3. 静态 Web UI 能否在不上传用户数据的前提下公开分享；
4. 生命周期外壳、角色模型、记录策略和 v0.2 Evidence Gate Kernel 是否协调。

本项目首先是方法验证项目，不以功能数量、商业化或处理所有 CSV 变体为目标。

## 2. 产品边界

### 必须完成

- 导入一个 CSV 文件；
- 在浏览器本地解析和检查，不将文件内容发送到服务器；
- 检查空值和完全重复行；
- 显示总行数、问题数和问题位置；
- 返回结构化 `QualityReport`；
- 使用固定样本和预期结果完成自动测试；
- 构建静态站点并通过公开 HTTPS 地址分享；
- 完成交付、回滚、HANDOFF 和 Playbook 反馈。

### 明确不做

- 类型、日期和业务口径推断；
- 自定义规则编辑器；
- 数据修改、清洗或自动修复；
- Excel、数据库和 API 输入；
- 登录、权限、云端保存和多人协作；
- 生成式 AI 建议；
- 超大文件、流式处理和性能承诺；
- 付费服务、正式 npm 发布和生产 SLA。

## 3. 可扩展架构边界

```text
CSV File
→ CSV Adapter
→ Normalized Table
→ Quality Core
   ├─ Missing-value Rule
   └─ Exact-duplicate Rule
→ QualityReport
→ Static Web UI
```

必须保持：

- `Quality Core` 不依赖 DOM、页面状态、静态托管平台或网络请求；
- CSV 解析属于 Adapter，不写进检查规则；
- UI 只负责输入、调用和展示；
- Core 通过明确类型和函数入口返回结构化结果；
- 单元测试能够绕过 UI，直接调用 Core 处理标准化数据。

后续可以增加规则、输入 Adapter、CLI、服务或包发布，但这些都不进入本轮范围。

## 4. 项目画像与修饰器

- 基础画像：`PF-APP`。
- 领域特征：表格数据质量检查。
- 启用修饰器：`MD-UI`、`MD-DATA`、`MD-DEPLOY`、`MD-SEC`。
- 条件式修饰器：`MD-OPS`，只验证最小可用性检查和版本回滚，不建立值守或 SLA。
- 不启用：`MD-EXT`、`MD-MULTI`、`MD-HIGH`。

选择 `PF-APP` 而不是 `PF-DAT`，是因为主要交付物是供人直接使用和分享的交互应用；数据分析能力作为领域特征和 Adapter/Core 边界处理。实验必须反馈这种表达是否自然。

## 5. 阶段裁剪

| Stage | 状态 | 本项目重点 |
| --- | --- | --- |
| STG-00 Profile & Tailor | Required | 核对画像、修饰器、角色和文件映射 |
| STG-01 Discover & Frame | Required | 明确用户、场景、价值和非目标 |
| STG-02 Contract | Required | 冻结范围、验收、安全、停止条件和结论分级 |
| STG-03 Design | Required | UI 流程、Core API、Adapter、测试和部署设计 |
| STG-04 Plan & Prepare | Required | 建立独立仓库、阶段计划、工具验证和回滚点 |
| STG-05 Implement & Verify | Required | 按原子增量执行 v0.2 Evidence Gate Kernel |
| STG-06 Integrated Acceptance | Required | 固定样本、直接 Core 测试和真实浏览器 UAT |
| STG-07 Release / Delivery | Required | GitHub Pages 发布、HTTPS 访问和回滚验证 |
| STG-08 Operate / Observe | Conditional | 最小可用性复核；不做持续值守 |
| STG-09 Handoff / Close / Learn | Required | 交付、恢复、复盘和 HYP-01 至 HYP-07 反馈 |

## 6. Human Gate

| Gate | 人工确认内容 | 未确认时 |
| --- | --- | --- |
| HG-01 Contract Freeze | 用户、范围、验收和明确不做 | 不进入技术设计和实现 |
| HG-02 Design Freeze | UI 流程、Core 边界、技术路线和实施计划 | 不进入正式实现 |
| HG-03 UAT | 实际上传、结果理解、隐私说明和使用体验 | 不发布正式版本 |
| HG-04 Publish | 公开 URL、仓库可见性、部署目标和残余风险 | 不执行外部发布 |

## 7. 独立验收方向

- 固定 CSV fixture 与预期空值、重复项和问题位置；
- Core 单元测试不经过 UI 或 CSV Adapter；
- Adapter 解析结果与固定标准化表格比较；
- 浏览器端到端检查上传、展示和错误状态；
- 构建产物重新加载检查；
- 浏览器网络记录证明文件内容未被上传；
- 发布 URL、HTTPS、对应提交和回滚版本可以核验。

具体样本、容差和命令必须在项目 Contract 中冻结，本文件不预填结果。

## 8. 部署边界

- 首选 GitHub Pages；技术设计阶段仍须核对构建路径和仓库可见性；
- 网站按公开 URL 设计，不提供指定人员访问控制；
- 仓库不得包含真实敏感 CSV、凭据或用户上传内容；
- 部署属于外部写入，必须通过 `HG-04`；
- 自定义域名、统计脚本、广告和外部分析服务不在本轮范围。

## 9. 记录映射

新项目至少保留：

- `PROJECT`：画像、修饰器、阶段和角色；
- `REQUIREMENTS`：需求与验收契约；
- `TECH_DESIGN`：Core、Adapter、UI、测试和部署边界；
- `VALIDATION`：阶段状态、证据、异常和最终判定；
- `HANDOFF`：使用、复核、限制、恢复和交付入口；
- `PLAYBOOK_FEEDBACK`：v0.2 Rules 与 HYP-01 至 HYP-07 的 conformity/utility。

逻辑记录可以按项目规模合并，但内容必须可定位。实验项目不得修改 `playbook/**`。

## 10. 停止条件

出现以下情况时停止并回到 Contract 或 Maintainer，而不是扩大实现：

- 需要后端、账号、数据库或付费服务才能完成核心验收；
- CSV 边界问题迫使项目进入编码、日期或大文件专项工程；
- Core 与 UI 无法在当前路线中解耦；
- 无法建立固定 fixture 或独立验收依据；
- 发布需要超出既定权限、安全或隐私边界；
- 新增功能主要为了展示，而不服务于方法验证。

## 11. 下一动作

在独立项目和新实验对话中完成 `STG-00` 至 `STG-04`，形成项目 Contract 与执行计划；经 HG-01、HG-02 后才进入实现。创建项目前由 Maintainer 提供固定基线和启动提示词。
