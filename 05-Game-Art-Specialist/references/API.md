# Meowa 接入状态【可选，已启用】
- 官方 Skill：`../skills/game-assets/SKILL.md`
- 来源：`C:\Users\admin\Desktop\Codex-Agent-Standard\meowa-skills-main\meowa-skills-main\skills\game-assets`
- 复制时 runner 版本：`2026.09.08.4`
- 许可：MIT，副本见 `../skills/game-assets/LICENSE`
- 执行入口：`python skills/game-assets/meowart_api.py <command>`
- 依赖：Python、requests、Pillow；创建本角色时均已验证可用
- 认证：本地 `MEOWART_API_KEY` 或被 Git 忽略的 `.env`；当前待配置，禁止在聊天、命令参数、日志、报告或记忆中记录值
- 验证：`credits-balance` 返回余额后才表示认证可用
- 费用：生成任务消耗积分；每个新付费批次必须取得确认。恢复原 job 使用对应 poll 命令，不得重复提交
- 输出：每次指定新的 `--output-dir`；只交付官方声明的最终媒体和净化后的 `final_outputs.json`

完整认证、更新、参数、超时和恢复规则以随包 Meowa Skill 为准。更新时必须整体替换 `skills/game-assets` 并重新验证版本、帮助、依赖、许可和路由，不能只更新单个文件。
