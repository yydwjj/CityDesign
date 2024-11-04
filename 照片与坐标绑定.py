import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import pandas as pd

# 读取 PNG 图片
img = mpimg.imread('CityImg03.png')

# 设置图片对应的地理范围（假设已知左下角和右上角的坐标）
x_min, y_min = (120.0993, 30.2784)  # 左下角坐标
x_max, y_max = (120.1082, 30.2865)  # 右上角坐标

# 示例数据：假设包含人群坐标的 DataFrame
data = pd.DataFrame({
        'longitude': [120.1018, 120.1061, 120.1047, 120.1052, 120.1047, 120.1046, 120.1042, 120.0999],
    'latitude': [30.2785, 30.2792, 30.2807, 30.282, 30.2843, 30.2821, 30.2853, 30.2847]
})

# 创建图像并显示图片
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(img, extent=[x_min, x_max, y_min, y_max])  # 将图片加载到特定的地理范围内

# 使用 kdeplot 在图片上绘制密度图
sns.kdeplot(
    x=data['longitude'], y=data['latitude'],
    cmap="coolwarm",    # 颜色梯度，用于显示热点和冷点
    shade=True,         # 显示密度填充
    alpha=0.5,          # 透明度，确保底图可以透出
    ax=ax,
    thresh=0.15         # 控制图像边界的阈值
)

# 设置标题和标签
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("地理热点和冷点分布")

# 显示图像
plt.show()
