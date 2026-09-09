# 配置与维护说明
本包已完成“游戏美术专家”专职化，可直接通过 START-HERE.md 显式调用。内置 imagegen 可由宿主直接提供；Meowa 已接入但认证待配置。

## Meowa 首次认证
1. 在 Meowa 网站创建以 `ma_live_` 开头的 API Key。
2. 仅在本机 PowerShell 会话设置：`$env:MEOWART_API_KEY = "你的密钥"`；或写入已被 Git 忽略的本地 `.env`。
3. 不要把密钥粘贴到聊天、提示词、命令参数、截图、日志或仓库。
4. 从本包目录运行：`python skills/game-assets/meowart_api.py credits-balance`。
5. 只有实际返回余额，才把认证视为可用。

## 更新 Meowa
来源副本位于同级 `meowa-skills-main` 仓库。更新时整体替换 `skills/game-assets/`，保留 MIT 许可；重新验证 `--version`、`--help`、依赖、路由和认证。不得只替换 SKILL.md 或 runner。

## 运行时输入与维护
templates/TASK.md、HANDOFF.md 和 memory/templates 的空字段只在真实任务中填写。职责或输出契约变化时同步 AGENT.md、WORKFLOW.md、TOOLS.md、templates/OUTPUT.md 和 MODULES.md；Meowa 接入变化时同步 references/API.md。
修改后验证结构、占位符、内部引用、Skill 格式、无密钥路由、付费确认、版本化输出和 04 工程交接。
