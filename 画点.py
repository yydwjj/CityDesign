#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 假设你的文件路径为 'pointData.xls'
file_path = 'pointData.xls'

# 使用pandas读取excel文件，只选择第3列、第4列和第5列
df = pd.read_excel(file_path, usecols=[2, 4, 5])

# 重命名列
df.columns = ['type', 'x', 'y']

# 假设你的地图背景图像和边界范围
img = plt.imread('CityImg03.png')  # 读取地图背景图像
x_min, x_max = 120.0993, 120.1082  # 地图的经度范围
y_min, y_max = 30.2784, 30.2865  # 地图的纬度范围

# 定义一个颜色列表，使用你提供的十六进制颜色值
colors = [
    "#4B7C9A",
    "#9A4741",
    "#756975",
    "#8FAA87",
    "#849AC1",  # 注意：原代码中的 "CI" 应该是 "C1"
    "#929BC2"
]

# 按分类列分组
grouped = df.groupby('type')

# 创建一个总的图像
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img, extent=[x_min, x_max, y_min, y_max], aspect='auto')

# 记录当前使用的颜色索引
current_color_index = 0

# 遍历每个分组并绘制地图
for group_name, group_data in grouped:
    # 获取当前分类的颜色
    color = colors[current_color_index % len(colors)]  # 循环使用颜色列表
    # 在指定坐标处添加多个标记
    ax.plot(group_data['x'], group_data['y'], marker='o', color=color, markersize=8, linestyle='',
            label=f"{group_name}")

    # 更新颜色索引
    current_color_index += 1

# 添加图例
ax.legend()

# 保存图像
plt.savefig('map_all_types.png')

# 显示图像
plt.show()