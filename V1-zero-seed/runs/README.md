# V1 Zero Seed 正式运行目录

当前没有正式运行。规划冻结提交报告后，只有 `HG-00` 获得 Human 明确授权，才为每次尝试创建独立的 `runs/<run-id>/`，并遵循上级 `REQUIREMENTS.md`、`EXPERIMENT_PLAN.md`、`RUN_RECORD_TEMPLATE.md` 和 `VALIDATION.template.md`。

不要预放空白 PBIP/PBIR/TMDL 项目。空 `project/` 不提交占位文件；其 Trusted baseline 状态记录在 `RUN.md`、`VALIDATION.md` 和目录外证据中。

失败现场保持不可变。只有 Contract 允许、状态可信且不会覆盖证据时才在原 Run 原子步骤内重试；否则回滚或新建 attempt。
