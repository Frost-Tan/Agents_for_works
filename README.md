# Codex Agent 标准包

`01-Blank-Agent` 是完整空白母版。当前专业角色包括：

- `02-Code-Quality-Inspector (tempt)`：早期代码质量检查角色；
- `03-Code-Quality-Auditor`：独立代码质量审计；
- `04-Code-Implementation-Engineer`：跨语言代码实现；
- `05-Game-Art-Specialist`：游戏美术资产生产；
- `06-Game-Art-Director`：游戏美术指导与质量门禁；
- `07-Godot-Game-Designer`：Godot 4.x、2D与卡牌策略优先的游戏设计；
- `08-Godot-Game-QA-Playtest-Analyst`：Godot真实试玩、平衡验证与可玩版本门禁；
- `09-Godot-Game-Audio-Specialist`：Godot游戏音效、环境音、音乐和批准语音生产。

各标准角色包保留母版的 22 个文件和对应路径。先看各包 MODULES.md 区分必需与可选，再读取 AGENT.md 获取职责和调用边界。

此前桌面的 Universal-Agent-Template、Code-Quality-Inspector、Agent-Team-Template 在本轮用途上均被此标准包替代；旧文件原样保留，不再作为本轮母版。

必需角色内容由编辑时填写；TASK、HANDOFF、项目记忆表的实际目标/版本/结果在运行时填写。没有真实项目任务时留空是正确行为。
专业化只需编辑预留模块；所需资料、脚本可以放入现有目录，无须新增顶层架构。

显式调用入口：提供对应 AGENT.md 的绝对路径和实际任务。技能模块未自动安装，网络/API/权限仍依赖当前 Codex 宿主。

格式与提示词依据参考：
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://developers.openai.com/api/docs/guides/latest-model
- https://docs.godotengine.org/en/stable/

本包的通用目录约定是本次设计，不是 Codex 原生配置格式。
