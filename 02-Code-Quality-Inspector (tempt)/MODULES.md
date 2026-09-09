# 模块清单
状态：专业角色已填写；运行时目标由用户提供。

| 文件/目录 | 必需性 | 本包状态 |
| --- | --- | --- |
| AGENTS.md、AGENT.md | 必需 | 启用：代码质量检查 |
| WORKFLOW.md、TOOLS.md | 必需 | 启用：只检查产品，限定记录写入 |
| templates/OUTPUT.md | 必需 | 启用：有证据的问题报告 |
| templates/TASK.md、HANDOFF.md | 必需 | 启用；表格运行时填写 |
| memory/ | 必需 | 启用；实际项目记忆独立保存 |
| collaboration/PROTOCOL.md | 必需 | 回报、续接、交接启用 |
| 向下委派 | 可选 | 关闭：本角色是检查执行者；可被主窗口调用 |
| skills/professional-method/ | 可选 | 关闭：WORKFLOW 已足够，无需重复流程 |
| references/DOMAIN.md | 可选 | 启用：问题分级与证据规则 |
| references/API.md | 可选 | 关闭：未接入外部 API |
| scripts/ | 可选 | 关闭：没有额外执行脚本 |
| assets/ | 可选 | 关闭：不需要输出资源 |
| README.md、SETUP.md、START-HERE.md | 必需 | 使用、填写与调用说明 |

必需文件不得删除；可选模块可以关闭并保留目录，或删除后同步本清单及引用。
这两个交付包保留完全一致的路径。新增专业资料或脚本只能放入预留模块，无需新增顶层架构。
运行时表格的空字段是输入位置，不是遗漏的专业角色定义。
