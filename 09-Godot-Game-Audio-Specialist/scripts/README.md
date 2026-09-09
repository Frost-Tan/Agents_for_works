# 基础SFX生成器【已启用】
入口：`python scripts/generate_basic_sfx.py`

支持ui_click、card_draw、card_play、impact、warning。必需参数为--preset和--output；可选--duration-ms、--sample-rate、--seed。默认48kHz、单声道、PCM16 WAV，相同参数与种子可复现。
输出存在时拒绝覆盖；应写入目标项目的版本化音频目录或独立临时目录，不写角色包assets。脚本只用Python标准库。
先运行--help或--version确认入口。生成后必须实际试听并检查技术属性；脚本成功不表示资产合格。
