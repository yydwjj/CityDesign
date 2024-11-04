import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 创建示例数据
data = {
    'Activity': ['聊天', '溜娃', '跑步', '骑车', '闲逛', '休息'],
    '早': [20, 15, 10, 5, 25, 25],
    '中': [15, 20, 15, 10, 30, 20],
    '晚': [10, 25, 20, 15, 35, 15]
}

# 转换为 DataFrame
df = pd.DataFrame(data)

# 设置雷达图的轴
activities = df['Activity'].values
num_vars = len(activities)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# 创建雷达图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

# 绘制每个时间段的数据
for time in ['早', '中', '晚']:
    values = df[time].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=time)
    ax.fill(angles, values, alpha=0.25)

# 添加标题和标签
# ax.set_title('公园中人群活动分布 (雷达图)')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(activities)
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# 显示图形
plt.show()