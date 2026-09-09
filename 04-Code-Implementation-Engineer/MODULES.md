# 模块清单
状态：代码实现工程师已配置；真实目标、项目基线和授权由运行时任务提供。

| 文件/目录 | 必需性 | 本包状态 |
| --- | --- | --- |
| AGENTS.md、AGENT.md | 必需 | 启用：跨语言代码实现身份与职责边界 |
| WORKFLOW.md、TOOLS.md | 必需 | 启用：任务内自主实现、测试与验证 |
| templates/OUTPUT.md | 必需 | 启用：变更、验证、未决风险交付契约 |
| templates/TASK.md、HANDOFF.md | 必需 | 启用：任务输入与真实交接 |
| memory/ | 必需 | 启用：实际项目记忆独立保存 |
| collaboration/PROTOCOL.md | 必需 | 启用：回报、续接和交接 |
| 向下委派 | 可选 | 关闭：默认单一实现负责人，可被主窗口调用 |
| skills/professional-method/ | 可选 | 关闭：方法已由 WORKFLOW 定义 |
| references/DOMAIN.md | 可选 | 启用：变更风险、授权和独立审计边界 |
| references/API.md | 可选 | 关闭：未接入固定外部 API |
| scripts/ | 可选 | 关闭：没有角色专用脚本；可使用目标项目已有脚本 |
| assets/ | 可选 | 关闭：没有角色专用输出资源 |
| README.md、SETUP.md、START-HERE.md | 必需 | 启用：角色说明、维护和调用方法 |

未启用模块不构成能力或隐含依赖。实际任务表和记忆模板中的空字段是运行时输入，不是未完成的角色定义。角色包不存放实际项目数据、代码或记忆。
