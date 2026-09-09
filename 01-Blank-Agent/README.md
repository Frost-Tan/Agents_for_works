# 完整空白 Agent 母版
两份包的路径完全一致。空白母版填写职责后得到专业角色；本示例没有省略母版模块。
目录内 AGENTS 是入口，AGENT 是身份，两者用途不同。
本包只面向 Codex 显式文件读取，不是常驻程序、原生角色注册或权限沙箱。

## 必须填写什么：先按这张表操作
“必须保留文件”不等于“每个文件都必须重写”。复制母版后先完成以下 5 个文件：

| 文件 | 必须填写/修改的项目 | 填写完成的判断 |
| --- | --- | --- |
| AGENT.md | role_id、名称、专职目标、适用任务、不负责事项、必需输入、专业行为与质量标准、完成条件 | 所有【填…】已替换；能明确判断任务是否属于这个角色 |
| WORKFLOW.md | 专业分析方法、执行方法、验证与证据要求、常见失败和停止条件 | 另一会话能据此开展实际工作，不只有“认真检查”等口号 |
| TOOLS.md | 必需/可选能力、可读写范围、不允许行动、工具缺失处理、验证命令规则与副作用 | 不存在的能力不写成已可用；与职责及实际宿主一致 |
| templates/OUTPUT.md | 交付物、必需字段、证据格式、结论取值、未验证/受阻表达、下一步 | 可以据此检查交付是否合格 |
| MODULES.md | 角色配置状态，以及每个可选模块是否启用 | 未使用模块明确“关闭/不适用”，引用与实际文件一致 |

### 必须保留、通常不用重写
- AGENTS.md：通用加载入口，已有内容可沿用。
- memory/POLICY.md：记忆规则可沿用，按专业补充而非删除必要读写步骤。
- collaboration/PROTOCOL.md：回报、续接与交接可沿用；不委派时关闭向下委派。
- SETUP.md、README.md、START-HERE.md：保留使用说明；专职化后修正角色名称和实际调用路径。

### 运行时填写，不在母版中编造
- templates/TASK.md：真实目标、项目路径、范围、验收和授权。
- templates/HANDOFF.md：发生交接时的真实状态。
- memory/templates/*.md：复制到项目记忆目录后填写项目身份、进度、决策和历史。
- START-HERE.md 中目标路径与任务：调用时填写。
这些表格留空不代表角色没有配置，但 AGENT/WORKFLOW/TOOLS/OUTPUT 中的必填占位符不能留空。

### 可选模块：启用才需要填写
| 模块 | 启用时要做什么 |
| --- | --- |
| skills/ | 放入完整技能目录，登记实际 SKILL.md 路径、触发条件、依赖及凭据配置方式 |
| references/DOMAIN.md | 填专业准则、适用范围与来源 |
| references/API.md | API 由你自己封装时填接口、认证、解析、超时和执行入口；若由外部 Skill 完整封装，可引用其权威文档，不重复维护 |
| scripts/ | 放入需要的实际脚本，登记依赖、副作用并验证 |
| assets/ | 放入实际资源，登记用途、来源与必要许可 |
| 向下委派 | 说明何时委派；成员和任务可在每次调用中提供 |

### 接入第三方 Skill（例：Meowa game-assets）
skills/professional-method 是占位模块，可以保留关闭，也可以由完整的 game-assets 技能目录替代。
应复制完整 skills/game-assets 目录，保留其 SKILL.md、脚本、references 和元数据的相对结构，不只替换 SKILL.md，也不要拆散脚本放到顶层 scripts。
也可以安装到 Codex 的技能位置，在本包仅引用安装后的实际入口路径。不必保留两份拷贝。
本包普通 skills/ 目录用于显式读取，并不意味着 Codex 会自动发现。

接入后同步：
1. MODULES.md：技能名称、位置、启用状态。
2. AGENT.md：什么任务读取该技能。
3. TOOLS.md：实际执行入口、依赖、认证方式与输出目录；不写密钥值。
4. WORKFLOW.md：在适当步骤调用技能，避免重复抄写其全部规则。

可用于 Codex 的安装命令（需要 Node.js/npx；本次没有执行）：
```text
npx skills add https://github.com/Meowa-AI/meowa-skills --skill game-assets --agent codex
```
这条命令通过安装器安装，不保证写入本包的普通 skills/ 目录。核对安装结果中的实际路径；默认项目范围，添加 -g 表示用户范围。
Meowa 仓库还要求 Python requests、Pillow 以及 MEOWART_API_KEY。Skill 安装成功不等于依赖、认证和服务调用已经可用。
凭据通过环境变量或不入库的本地配置提供，不写到角色说明或聊天中。

参考（2026-09-08 核对）：
- https://github.com/Meowa-AI/meowa-skills
- https://github.com/vercel-labs/skills

### 配置完成的最后检查
必填角色内容无占位符；可选项有状态；技能路径存在；工具能力可用；输出可验收；真实记忆与母版分离。
首次用一个小任务验证实际行为；文件齐全不能代替运行验证。


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
