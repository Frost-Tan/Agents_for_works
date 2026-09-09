# 模块清单
状态：Godot游戏QA与试玩分析师已配置；真实构建、环境和门禁条件由运行时任务提供。

| 文件/目录 | 必需性 | 本包状态 |
| --- | --- | --- |
| AGENTS.md、AGENT.md | 必需 | 启用：独立真实试玩与门禁 |
| WORKFLOW.md、TOOLS.md | 必需 | 启用：Godot执行矩阵、隔离取证与复核 |
| templates/OUTPUT.md | 必需 | 启用：GQA问题和门禁报告 |
| templates/TASK.md、HANDOFF.md | 必需 | 启用：构建、环境和复核输入 |
| memory/ | 必需 | 启用：项目记忆独立保存 |
| collaboration/PROTOCOL.md | 必需 | 启用：问题路由和团队回报 |
| 向下委派 | 可选 | 关闭：其他角色由主Agent调用 |
| skills/professional-method/ | 可选 | 关闭：方法已由WORKFLOW定义 |
| references/DOMAIN.md | 可选 | 启用：分级、证据和平衡试玩规范 |
| references/API.md | 可选 | 关闭：未接固定外部API |
| scripts/ | 可选 | 关闭：不提供自动测试脚本 |
| assets/ | 可选 | 关闭：测试证据保存在目标项目报告目录 |
| README.md、SETUP.md、START-HERE.md | 必需 | 启用 |

未启用模块不构成能力。角色包不保存具体构建、用户存档、证据或项目记忆。
