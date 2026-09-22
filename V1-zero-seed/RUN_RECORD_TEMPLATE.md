# V1 Zero Seed — Run 记录模板

复制本模板内容到 `runs/<run-id>/RUN.md`；同时从 `VALIDATION.template.md` 创建该 Run 的 `VALIDATION.md`。不得复制任何既有工程文件。

## 1. Run 身份

- Run ID：
- Attempt：
- 试验组：A / B / 补充组
- 项目名：
- 项目绝对路径：
- Playbook 基线：`3ee871d618db84d55b3b2f86a198ac552864317e`
- 需求冻结提交：
- Run 起点提交：
- 生成规则版本或提交：
- 开始时间与时区：
- Experiment Owner：
- Human Approver：

## 2. 环境、权限与安全

- Power BI Desktop 完整版本：
- PBIP/PBIR 功能状态：
- Modeling MCP 包版本和服务端自报版本：
- Windows / 文件系统 / 路径特征：
- Desktop/MSAS 进程预检：
- 允许的外部访问：
- 权限检查：
- 敏感信息与脱敏检查：
- 初始 Git 状态与 rollback point：

## 3. 来源声明

- 使用的 V1 文档及提交：
- 使用的微软公开文档/Schema（URL、获取时间、SHA-256 如可得）：
- 使用的验证工具或脚本：
- `V0/seed/**` 未读取/未复制：是 / 否
- `V0/runs/**/project/**` 未作为实现参考：是 / 否
- 未复制其他 Run 的工程文件：是 / 否
- 来源例外或 Evidence Gap：

## 4. Trusted baseline：空目录证明

- 创建时间：
- 检查命令：
- 文件数：
- 子目录数：
- 证据位置：
- Gate：`Not Started / Passed / Blocked / Failed`

## 5. 分离式操作日志

### 人工操作：`logs/HUMAN_ACTIONS.md`

| 时间 | Gate ID | 请求与目标 | 预期 | Human 实际动作/观察 | 继续授权 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |

只记录真实人工动作；不得把请求或建议写成已执行事实。

### MCP 操作：`logs/MCP_ACTIONS.jsonl`

```json
{"timestamp":"","gate":"","tool":"","operation":"","target":"","inputSummary":{},"confirmation":"","result":"","evidence":""}
```

### Codex 文件操作：`logs/CODEX_FILE_ACTIONS.jsonl`

```json
{"timestamp":"","stage":"","operation":"create|modify|delete|hash","path":"","beforeSha256":null,"afterSha256":"","reason":"","source":"public-spec|v1-contract|generated","actor":"Codex","verification":""}
```

### 异常：`logs/EVENTS.jsonl`

```json
{"id":"EVT-001","timestamp":"","stage":"","eventType":"Validation Failure|Environment Failure|Safety/Permission Blocker|Governance Failure|Evidence Gap|Expected Negative Result|Warning","severity":"Blocking|Non-blocking|Informational","v1Cause":"GEN|SPEC|DESKTOP|PATH|MCP|ENV|HUMAN|PROVENANCE","observation":"","impact":"","action":"retry|rollback|new-run|continue|stop","evidence":""}
```

## 6. Desktop 差异

| 路径 | 变化阶段 | 原始差异摘要 | 结构/语义解释 | 分类 | 项目必需 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |

允许分类：`CACHE_LOCAL`、`SERIALIZATION_EQUIVALENT`、`DEFAULT_ENRICHMENT`、`VERSION_UPGRADE`、`STRUCTURAL_REQUIRED`、`SEMANTIC_CHANGE`、`UNKNOWN`。

## 7. R-VLD-003 计量

写入 `logs/R-VLD-003-METRICS.json`，至少包含：

```json
{
  "coreRoundtrip": {"desktopStarts": 0, "humanActiveMinutes": 0, "waitMinutes": 0, "machineCheckMinutes": 0, "evidenceFiles": 0, "evidenceBytes": 0, "uniqueFindings": []},
  "playbookOnlyFinalRoundtrip": {"desktopStarts": 0, "humanActiveMinutes": 0, "waitMinutes": 0, "machineCheckMinutes": 0, "evidenceFiles": 0, "evidenceBytes": 0, "uniqueFindings": []},
  "counterfactualRiskIfOmitted": "",
  "utilityAssessment": "Helpful|Neutral|Burdensome|Harmful",
  "recommendation": "Keep|Change|Retire|Move"
}
```

## 8. 本 Run 候选结论

- 功能结果：完全零种子 / Desktop 首次补写 / 仍需人工种子 / 无法判定
- Contract 符合度：
- 证据完整度：
- 持久化/重启状态：
- 安全与权限状态：
- 已知限制和不能声称的内容：
- 是否需另一组独立 Run：是 / 否
- Run 最终 checkpoint：
