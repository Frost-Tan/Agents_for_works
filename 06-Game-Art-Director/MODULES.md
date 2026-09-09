# 模块清单
状态：游戏美术总监已配置；独立审核启用，生成能力关闭。

| 文件/目录 | 必需性 | 本包状态 |
| --- | --- | --- |
| AGENTS.md、AGENT.md | 必需 | 启用：美术指导、门禁与生成治理 |
| WORKFLOW.md、TOOLS.md | 必需 | 启用：只读正式资产，仅写审核产物 |
| templates/OUTPUT.md | 必需 | 启用：门禁、评分、ART 问题与例外 |
| templates/TASK.md、HANDOFF.md | 必需 | 启用：审核输入与真实交接 |
| memory/ | 必需 | 启用：项目记忆独立保存 |
| collaboration/PROTOCOL.md | 必需 | 启用：回报、续接与交接 |
| 向下委派 | 可选 | 关闭：由主 Agent 调用 05 和 06 |
| skills/professional-method/ | 可选 | 关闭：审核规则已由 WORKFLOW 和 DOMAIN 定义 |
| Meowa Skill | 可选 | 不复制；只读引用 05 的官方 Skill |
| references/DOMAIN.md | 可选 | 启用：评分、问题等级和滥用治理 |
| references/API.md | 可选 | 启用：记录对 05 Meowa Skill 的只读引用 |
| scripts/ | 可选 | 关闭：没有专用生成或审核脚本 |
| assets/ | 可选 | 关闭：项目审核辅助图保存在项目 reviews 目录 |
| README.md、SETUP.md、START-HERE.md | 必需 | 启用：角色说明、维护和调用方法 |

未启用模块不构成能力。06 不持有生成凭据、不调用生成工具、不消耗积分。项目审核产物和实际记忆不得写回角色包。
