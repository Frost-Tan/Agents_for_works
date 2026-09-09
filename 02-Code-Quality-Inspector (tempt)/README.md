# 代码质量检查员：母版填写实例
两份包的路径完全一致。空白母版填写职责后得到专业角色；本示例没有省略母版模块。
目录内 AGENTS 是入口，AGENT 是身份，两者用途不同。
本包只面向 Codex 显式文件读取，不是常驻程序、原生角色注册或权限沙箱。

## 从哪里开始
先看 MODULES.md 的必需/可选清单，再看 AGENT.md；SETUP.md 解释如何填写。
START-HERE.md 提供主窗口及子 Agent 调用格式。

## 固定结构与对应职责
| 文件/目录 | 作用 |
| --- | --- |
| AGENTS.md | 包入口和加载顺序 |
| AGENT.md | 完整角色身份、范围、协作与结束条件 |
| MODULES.md | 必需/可选及启用状态 |
| WORKFLOW.md | 专业执行流程 |
| TOOLS.md | 能力、权限、副作用与不可用处理 |
| memory/POLICY.md | 固定记忆读写规则 |
| memory/templates/ | 运行时记忆的空白表格 |
| collaboration/PROTOCOL.md | 回报、消息、续接与可选委派 |
| templates/TASK.md | 任务输入 |
| templates/OUTPUT.md | 专业输出契约 |
| templates/HANDOFF.md | 新实例交接 |
| skills/professional-method/ | 预留专业技能 |
| references/DOMAIN.md | 专业参考 |
| references/API.md | API 接入说明 |
| scripts/ | 可验证脚本位置 |
| assets/ | 输出资源位置 |
| SETUP.md、START-HERE.md | 编辑和使用方法 |

## 记忆
角色包只存规则和空表，实际记忆按项目存储。例：项目记录目录/memory/INDEX.md。
每次恢复读入口及状态，再按需读历史与决定；不能保证未保存内容或原会话永不丢失。
角色定义与规则不会因为加载而变得不可写；要求不自行修改属于行为约束。

## 使用边界
Skill 可以封装 API 方法，但不提供密钥、网络或执行权限。
可以作为主窗口身份，也可被实际子 Agent 工具调用；无固定成员数量，委派按模块状态和用户授权。
本次仅做结构和内容校验，没有运行真实项目审查或外部 API。
