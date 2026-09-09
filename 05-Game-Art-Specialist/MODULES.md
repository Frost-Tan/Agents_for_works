# 模块清单
状态：游戏美术专家已配置；Meowa 能力已接入、认证待本地配置。

| 文件/目录 | 必需性 | 本包状态 |
| --- | --- | --- |
| AGENTS.md、AGENT.md | 必需 | 启用：跨品类游戏视觉资产生产身份 |
| WORKFLOW.md、TOOLS.md | 必需 | 启用：内置 imagegen 与 Meowa 能力路由 |
| templates/OUTPUT.md | 必需 | 启用：版本化资产、检查和工程交接 |
| templates/TASK.md、HANDOFF.md | 必需 | 启用：资产契约与真实交接 |
| memory/ | 必需 | 启用：实际项目记忆独立保存 |
| collaboration/PROTOCOL.md | 必需 | 启用：回报、续接与交接 |
| 向下委派 | 可选 | 关闭：本角色为美术执行者，可由主 Agent 调用 |
| skills/game-assets/ | 可选 | 启用：Meowa 官方完整 Skill，认证待配置 |
| skills/professional-method/ | 可选 | 关闭：专业流程已由 WORKFLOW 和 Meowa Skill 定义 |
| references/DOMAIN.md | 可选 | 启用：通用游戏美术质量与工程交接规则 |
| references/API.md | 可选 | 启用：Meowa 来源、版本、认证、费用和恢复入口 |
| scripts/ | 可选 | 关闭：顶层无专用脚本；Meowa 自带脚本保留在 Skill 内 |
| assets/ | 可选 | 关闭：仅保留固定角色资源说明，不存项目成品 |
| README.md、SETUP.md、START-HERE.md | 必需 | 启用：角色说明、配置和调用方法 |

未启用模块不构成能力。项目资产和实际记忆必须保存在任务授权目录，不得写回角色包。Meowa Skill 必须整体维护；不能只替换 SKILL.md、runner 或单个参考文件。
