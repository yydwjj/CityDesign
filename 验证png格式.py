from PIL import Image

try:
    img = Image.open('CityImg02.png')
    img.verify()  # 检查文件是否为有效图像
    print("图像文件有效")
except Exception as e:
    print("图像文件无效或格式不正确:", e)
