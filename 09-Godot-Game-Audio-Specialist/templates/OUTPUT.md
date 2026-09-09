# Godot游戏音频交付契约【必需，已填写】
## 报告头
- 任务状态：completed / partial / blocked / awaiting_approval
- 音频成熟度：draft / proposed / approved / superseded
- 项目、资产组、版本、Godot版本、目标平台和审批人
- 实际使用的本地脚本、专业工具或外部任务标识

## 资产交付
- 最终媒体、试听预览、源文件和audio-manifest.md路径
- 每项用途、触发事件、变体关系、来源/生成参数、授权、版本和哈希
- 时长、声道、采样率、位深/编码、峰值、响度、循环点、BPM/拍数及分层信息
- 实际试听设备、视觉波形/指标检查、未验证项和限制

## Godot接入规格
- AudioStreamPlayer或AudioStreamPlayer2D建议及理由
- 目标总线、相对音量、优先级、max_polyphony、随机变体和防疲劳规则
- 循环、转场、同步、导入与平台注意事项
- 交给04的事件、资源路径建议和验收条件
- 交给08的游戏内触发、混音、可辨识性和重复测试

## 批准与下一步
- 用户批准状态、待选变体和superseded关系
- 付费批次确认/恢复状态，不暴露凭据或内部URL
- 未完成音乐、复杂拟音或语音的专业生成简报
- 记忆更新建议

默认保存到assets/audio/generated/<asset-group>/vNNN/。生成成功不等于试听或用户批准；没有实际媒体不得声称完成资产。
