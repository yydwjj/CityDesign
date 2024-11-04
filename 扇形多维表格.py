import matplotlib.pyplot as plt
import numpy as np

# 示例数据
data = {
    'Morning': {'聊天': 20, '带孩子': 15, '跑步': 10, '骑车': 5, '闲逛': 25, '休息': 25},
    'Afternoon': {'聊天': 15, '带孩子': 20, '跑步': 15, '骑车': 10, '闲逛': 30, '休息': 20},
    'Evening': {'聊天': 10, '带孩子': 25, '跑步': 20, '骑车': 15, '闲逛': 35, '休息': 15}
}

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建极坐标图
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# 扇形角度
theta = np.linspace(0.0, 2 * np.pi, 4, endpoint=False)  # 分成三个部分，所以是4个点
width = (2 * np.pi) / 3  # 每个扇形的角度宽度

# 颜色列表
colors = ['r', 'g', 'b']

# 绘制每个时间段的柱状图
for i, (time, activities) in enumerate(data.items()):
    # 计算每个活动的柱状图位置
    bars = []
    for j, (activity, count) in enumerate(activities.items()):
        angle = theta[i] + (j * width / len(activities))
        bars.append((angle, count))

    # 绘制柱状图
    bottom = 0
    for angle, count in bars:
        ax.bar(angle, count, width=width / len(activities), bottom=bottom, color=colors[i], alpha=0.7, edgecolor='w')
        bottom += count

    # 绘制扇形边界
    ax.bar(theta[i], 100, width=width, color=colors[i], alpha=0.3, edgecolor='k')

# 设置标签
labels = list(data.keys())
ax.set_xticks(theta)
ax.set_xticklabels(labels)

# 添加图例
legend_labels = list(next(iter(data.values())).keys())
ax.legend(legend_labels, loc='upper right', bbox_to_anchor=(1.15, 1.15))

# 显示图形
plt.show()