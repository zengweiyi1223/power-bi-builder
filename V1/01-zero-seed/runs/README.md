# V1 Zero Seed 正式运行目录

状态：**两次正式运行均已完成并通过。**

- [20260922-012919-a](20260922-012919-a/)：`ZeroSeedAlpha`，ASCII 名称与短路径。
- [20260922-032410-b](20260922-032410-b/)：`零种子 Beta`，不同父目录、空格与 Unicode。

两次运行均遵循 [REQUIREMENTS](../planning/REQUIREMENTS.md)、[EXPERIMENT_PLAN](../planning/EXPERIMENT_PLAN.md) 和 [templates/](../templates/) 中冻结的记录模板。每个 Run 均独立保存 `RUN.md`、`VALIDATION.md`、项目、manifest、日志和截图证据。

不要预放空白 PBIP/PBIR/TMDL 项目。空 `project/` 不提交占位文件；其 Trusted baseline 状态记录在 `RUN.md`、`VALIDATION.md` 和目录外证据中。

原执行规则要求失败现场保持不可变；只有 Contract 允许、状态可信且不会覆盖证据时才在原 Run 原子步骤内重试，否则回滚或新建 attempt。该段保留用于解释 A/B Run 的证据边界。
