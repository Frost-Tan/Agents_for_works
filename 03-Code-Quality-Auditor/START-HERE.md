# Codex 调用

## 作为当前窗口角色
请完整读取 `C:\Users\admin\Desktop\Codex-Agent-Standard\03-Code-Quality-Auditor\AGENT.md` 和同目录 `MODULES.md`，按“代码质量审计员”身份执行【审查任务】。
目标项目在【项目绝对路径】，审查类型与基线为【类型及代码/差异基线】，范围为【目标路径/调用链】，排除【排除项】。
允许进行【验证范围】；不得修改产品代码。报告默认在回复中交付；如需落盘，报告目录为【绝对路径】。memory_root 为【可选绝对路径】。

## 作为团队成员
请实际调用一个子 Agent，要求其完整读取 `C:\Users\admin\Desktop\Codex-Agent-Standard\03-Code-Quality-Auditor\AGENT.md`，并提供审查目标、项目绝对路径、基线、范围、验证权限、报告/记忆入口、验收和回传对象。
由主窗口统一派发修复并维护共享记忆。读取角色定义不等于创建了新实例；只有宿主实际返回实例 ID 才能声称已调用。

未使用的占位字段应从实际调用文本中删除，不要把括号内容原样交给 Agent。
