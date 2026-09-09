# 游戏音频记忆规则【必需】
实际项目记忆放在指定memory_root，音频媒体和manifest放项目版本目录，不存入角色包。团队共享记忆由主Agent唯一写入，09返回建议。
开始与续接读取INDEX、STATE，再检索DECISIONS和WORKLOG，核实项目、资产组、版本、成熟度、授权、付费job、批准记录和文件哈希。
STATE维护当前资产与审批状态；WORKLOG追加生成、试听、失败与接入验证；DECISIONS记录风格、工具、授权和用户批准；INDEX指向当前approved版本。
不保存密钥、未授权素材、声音身份数据、内部URL或思维链。只有实际写入成功才能声称已保存。
