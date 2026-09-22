# V1 Zero Seed — 运行记录模板

复制本模板内容到每个 `runs/<run-id>/RUN.md`；不要复制任何项目工程文件。

## 运行身份

- Run ID：
- Attempt：
- 试验组：A / B / 补充组
- 项目名：
- 项目绝对路径：
- Git 基线提交：
- 生成规则版本或提交：
- 开始时间与时区：
- 执行者：

## 环境

- Power BI Desktop 完整版本：
- PBIP/PBIR 功能状态：
- Modeling MCP 包版本和服务端自报版本：
- Codex 版本/模型（可记录时）：
- Windows 版本：
- 文件系统与路径特征：
- Desktop/MSAS 进程预检：

## 来源声明

- 使用的 V1 文档：
- 使用的微软公开文档/Schema（URL、获取时间、SHA-256 如可得）：
- 使用的非工程输入或验证脚本：
- `V0/seed/**` 未读取/未复制确认：是 / 否
- `V0/runs/**/project/**` 未作为实现参考确认：是 / 否
- 任何来源例外：

## 空目录证明

- 创建时间：
- 检查命令：
- 文件数：
- 子目录数：
- 证据位置：

## 阶段状态

| 阶段 | 状态 | Git/清单证据 | 备注 |
| --- | --- | --- | --- |
| P0 环境与治理预检 | 未开始 | | |
| P1 空目录证明 | 未开始 | | |
| P2 Codex 生成与离线预检 | 未开始 | | |
| P3 Desktop 首次打开 | 未开始 | | |
| P4 首次保存与关闭 | 未开始 | | |
| P5 重开与只读回读 | 未开始 | | |
| P6 重复性与分级 | 未开始 | | |

## 分离式操作日志

### 人工操作：`logs/HUMAN_ACTIONS.md`

| 时间 | 执行者 | UI 动作 | 目标 | 可见提示/结果 | 证据 |
| --- | --- | --- | --- | --- | --- |

只记录真实的人工作业；不要把 Codex 建议写成已执行动作。

### MCP 操作：`logs/MCP_ACTIONS.jsonl`

每行一个 JSON 对象，建议字段：

```json
{"timestamp":"","tool":"","operation":"","target":"","inputSummary":{},"confirmation":"","result":"","evidence":""}
```

### Codex 文件操作：`logs/CODEX_FILE_ACTIONS.jsonl`

每行一个 JSON 对象，建议字段：

```json
{"timestamp":"","operation":"create|modify|delete|hash","path":"","beforeSha256":null,"afterSha256":"","reason":"","source":"public-spec|v1-requirement|generated","actor":"Codex"}
```

## Desktop 差异归类

| 路径 | 首次变化阶段 | 差异摘要 | 分类 | 是否项目必需 | 归因证据 |
| --- | --- | --- | --- | --- | --- |

允许分类：`CACHE_LOCAL`、`SERIALIZATION_EQUIVALENT`、`DEFAULT_ENRICHMENT`、`VERSION_UPGRADE`、`STRUCTURAL_REQUIRED`、`SEMANTIC_CHANGE`、`UNKNOWN`。

## 失败与归因

- 现象：
- 主因代码：`GEN` / `SPEC` / `DESKTOP` / `PATH` / `MCP` / `ENV` / `HUMAN` / `PROVENANCE`
- 促成因素：
- 直接证据：
- 是否使本次运行无效：
- 是否需要新 attempt：

## 本次结论

- 打开：通过 / 失败 / 环境阻塞
- 首存：通过 / 失败 / 未执行
- 重开：通过 / 失败 / 未执行
- 结构性补写：无 / 有 / 未知
- 候选分级：完全零种子 / Desktop 首次补写 / 仍需人工种子 / 无法判定
- 该候选分级仍需另一组独立试验确认：是 / 否
