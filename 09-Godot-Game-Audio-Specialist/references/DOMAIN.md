# Godot游戏音频专业规范【已启用】
## 来源
Godot事实以目标项目实际版本及对应官方文档为准。最近核对：2026-09-09。
- https://docs.godotengine.org/en/stable/tutorials/audio/audio_streams.html
- https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_audio_samples.html
- https://docs.godotengine.org/en/stable/tutorials/audio/audio_buses.html
- https://docs.godotengine.org/en/stable/classes/class_audiostreamwav.html

## 设计质量
每个声音必须有游戏信息功能、触发条件、优先级、频率、变体和与其他声音的层级。高频卡牌/UI反馈避免过长尾音、音高单一和重复疲劳。
音乐与环境音说明情绪、结构、循环、转场、BPM/拍数、动态层和退出条件。声音风格来自项目指南，不模仿未授权作品、艺术家或人物身份。

## 技术质量
检查静音、截断、爆音、削波、底噪、声道、峰值、响度、循环接缝和目标设备。不能实际试听时不得批准。
短SFX默认48kHz PCM16 WAV；音乐/长环境音保留无损母版，编码工具可用时提供Ogg Vorbis运行版。格式、采样率、声道和压缩仍按目标平台调整。
Godot可用AudioStreamPlayer处理非定位UI/音乐，AudioStreamPlayer2D处理2D定位声音。总线、效果、导入、循环和播放器引用由04实现，09只交规格。

## 授权与语音
记录每项素材、生成器、提示词/参数、许可证和可交付范围。来源不明、许可冲突、未批准台词或未授权声音身份不得进入正式资产。
不得要求用户在聊天中粘贴密钥。新增付费生成批次逐批确认；恢复同一job不重复提交。

## 批准
成熟度为draft、proposed、approved、superseded。09自检和08游戏内验证都不能替代用户批准；approved必须有真实审批记录。
