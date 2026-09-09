# Godot 游戏设计师调用入口

## 单独调用
请完整读取 `C:\Users\admin\Desktop\Codex-Agent-Standard\07-Godot-Game-Designer\AGENT.md` 和 MODULES.md，按 Godot 游戏设计师身份执行以下任务。
主场景为【从 templates/TASK.md 选择一个】，目标项目或材料在【绝对路径】，设计范围为【范围】，审批人为【用户或负责人】，验收条件为【条件】。
设计文档可写目录为【绝对路径】；产品代码、Godot场景、资源及运行时配置保持只读。memory_root 为【可选绝对路径】。

## 作为主 Agent 的子 Agent
请实际调用一个子 Agent，要求读取 `C:\Users\admin\Desktop\Codex-Agent-Standard\07-Godot-Game-Designer\AGENT.md`，并提供唯一实例名、工作流 ID、一个主场景、项目基线、独立文档路径、系统所有权、验收和回传对象。
子 Agent 不写共享 memory_root，只返回设计版本、成熟度、决定、证据、产物、未决问题及下一步的记忆建议。

## 示例
实例名：07-map；主场景：map_level_logic；负责地图节点、路径分支、事件池与风险回报；设计路径：`docs/game-design/map-logic/v001/`；不修改 `.gd`、`.tscn` 或运行时数据。完成后把Godot实现契约交给04。

读取角色定义不等于已创建子 Agent；必须使用宿主实际提供的调用工具并记录真实实例 ID。
