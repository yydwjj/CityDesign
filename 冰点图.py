import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 示例数据：假设包含人群坐标的 DataFrame
data = pd.DataFrame({
    'longitude': [120.1045, 120.1060, 120.1050, 120.1030, 120.1075],  # 示例经度
    'latitude': [30.2800, 30.2820, 30.2810, 30.2790, 30.2835]        # 示例纬度
})

# 创建图像并设置背景
fig, ax = plt.subplots(figsize=(10, 10))

# 使用 kdeplot 进行密度绘制，cmap 为颜色映射表
sns.kdeplot(
    x=data['longitude'], y=data['latitude'],
    cmap="coolwarm",  # 颜色渐变，coolwarm 表示热点和冷点
    shade=True,       # 显示密度填充
    thresh=0.02,      # 控制图像边界的阈值
    ax=ax
)

# 设置标题和标签
plt.title("热点图和冷点图")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.show()
