# Godot游戏QA与试玩报告契约【必需，已填写】
## 报告头
- 门禁结论：approved / changes_requested / inconclusive
- 测试模式、构建版本/哈希、Godot版本、平台、环境和执行时间
- 实际输入设备、分辨率、语言、隔离存档和随机种子
- 设计/验收基线、覆盖范围、排除项及例外

## 执行矩阵
逐项记录用例ID、目标、前置条件、操作、预期、实际、结果、次数和证据。区分executed、static和reported；只有executed可支持正式试玩通过。
平衡结论需报告样本、构筑、敌人、地图种子、关键指标和限制。单次体验不得写成统计规律。

## GQA问题
按blocking、major、minor、observation排序。每项包含稳定GQA编号、类型、状态、置信度、构建、平台、种子/存档、位置、前置条件、复现步骤、期望/实际、频率、影响、证据、责任角色和复核条件。
状态为open、awaiting_recheck、resolved、dismissed。修复声明只能进入awaiting_recheck；新基线实测后才能resolved。

## 门禁与交接
- 阻断项、门禁关键major、用户例外和未覆盖范围
- 分别交给04、07、05/06、09或03的行动清单
- 是否允许标记可玩候选版本
- 下一轮测试范围和需要用户决定的事项
- 记忆更新建议

默认保存到reviews/game-qa/<build-id>/。未发现问题只表示当前范围内通过，不表示项目无缺陷。
