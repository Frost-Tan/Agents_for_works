# 游戏QA记忆规则【必需】
实际记忆放在任务指定memory_root，不存入角色包。团队共享记录由主Agent唯一写入，08返回建议；单独工作仅在授权目录维护。
开始与复核先读INDEX、STATE，再检索DECISIONS和WORKLOG，核实项目、构建哈希、设计基线、GQA状态和报告路径。记忆不恢复实例身份，也不能代替实际构建。
STATE保存当前门禁和未决问题；WORKLOG追加测试轮次；DECISIONS记录用户例外；问题保持稳定GQA编号及open、awaiting_recheck、resolved、dismissed状态。
不保存真实玩家存档、凭据、个人数据、完整原始日志或内部思维。写入成功后才能声称已保存。
