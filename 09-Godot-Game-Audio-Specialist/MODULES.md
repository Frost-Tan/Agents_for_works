# 模块清单
状态：Godot游戏音频专家已配置；本地基础SFX脚本启用，专业外部生成认证未配置。

| 文件/目录 | 必需性 | 本包状态 |
| --- | --- | --- |
| AGENTS.md、AGENT.md | 必需 | 启用：音频指导、生产、自检与批准边界 |
| WORKFLOW.md、TOOLS.md | 必需 | 启用：版本化生产、试听和Godot交接 |
| templates/OUTPUT.md | 必需 | 启用：媒体、manifest和验证契约 |
| templates/TASK.md、HANDOFF.md | 必需 | 启用 |
| memory/ | 必需 | 启用：项目记忆独立保存 |
| collaboration/PROTOCOL.md | 必需 | 启用：04/08交接与主Agent回报 |
| 向下委派 | 可选 | 关闭 |
| skills/professional-method/ | 可选 | 关闭：没有已安装专业音频Skill |
| references/DOMAIN.md | 可选 | 启用：音频质量、授权和Godot规范 |
| references/API.md | 可选 | 关闭：外部生成服务待用户选择 |
| scripts/ | 可选 | 启用：确定性基础SFX生成器 |
| assets/ | 可选 | 关闭：项目音频不存入角色包 |
| README.md、SETUP.md、START-HERE.md | 必需 | 启用 |

角色包比母版多一个已验证脚本文件。未配置外部工具不构成可用能力；具体项目资产和凭据不存入本包。
