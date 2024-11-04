import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import pandas as pd
import numpy as np

# 读取 PNG 图片
img = mpimg.imread('CityImg03.png')

# 设置图片对应的地理范围（假设已知左下角和右上角的坐标）
x_min, y_min = (120.0993, 30.2784)  # 左下角坐标
x_max, y_max = (120.1082, 30.2865)  # 右上角坐标

# 控制生成的组数
num_groups = 5  # 您可以调整组的数量，每组将生成一张图

for i in range(num_groups):
    # 生成一组 10 个随机点
    num_random_points = 10
    random_longitudes = np.random.uniform(x_min, x_max, num_random_points)
    random_latitudes = np.random.uniform(y_min, y_max, num_random_points)
    group_data = pd.DataFrame({'longitude': random_longitudes, 'latitude': random_latitudes})

    # 创建图像并显示图片
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(img, extent=[x_min, x_max, y_min, y_max])  # 将图片加载到特定的地理范围内

    # 使用 kdeplot 在图片上绘制密度图
    sns.kdeplot(
        x=group_data['longitude'], y=group_data['latitude'],
        cmap="coolwarm",    # 颜色梯度，用于显示热点和冷点
        shade=True,         # 显示密度填充
        alpha=0.5,          # 透明度，确保底图可以透出
        ax=ax,
        thresh=0.15          # 控制图像边界的阈值
    )

    # 设置标题和标签
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title(f"地理热点和冷点分布 - 组 {i + 1}")

    # 显示图像
    plt.show()
