# Codex 调用

## 作为当前窗口角色
请完整读取 `C:\Users\admin\Desktop\Codex-Agent-Standard\04-Code-Implementation-Engineer\AGENT.md` 和同目录 `MODULES.md`，按“代码实现工程师”身份执行【具体开发任务】。
目标项目在【项目绝对路径】；目标行为和验收为【说明】；范围为【相关路径或模块】，兼容要求与排除项为【说明】。
允许写入【范围】并运行【验证范围】。涉及生产依赖、公共契约变化、数据迁移、真实外部服务或不可逆操作时先向我确认。报告或记忆目录为【可选绝对路径】。

## 作为团队成员
请实际调用一个子 Agent，要求其完整读取 `C:\Users\admin\Desktop\Codex-Agent-Standard\04-Code-Implementation-Engineer\AGENT.md`，并提供项目、目标、基线、范围、验收、写入与验证权限、记忆入口和回传对象。
读取定义不等于创建实例；只有宿主实际返回实例 ID 才能声称已调用。高风险变更可在实现完成后另行调用 `03-Code-Quality-Auditor` 复核。

使用时删除未使用的占位字段，不把方括号内容原样交给 Agent。
