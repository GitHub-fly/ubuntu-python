"""
使用 Pillow 来处理图像：pip3 install Pillow
"""
# 图片相关
from io import BytesIO
from PIL import Image
import requests as req
from PIL import Image, ImageFilter
# 系统相关
import os


def pillow():
    # 打开图片，打印其格式、大小、图片类型
    img = Image.open('./resources/img/59.jpg')
    print(img.format, img.size, img.mode)

    Image.open('./resources/img/59.jpg').save('./resources/img/59_copy_plus.jpg')

    # 用 thumbnail() 方法为其生成原尺寸 1/3 大小的缩略图
    w, h = img.size
    img.thumbnail((w//3, h//3))
    img.save('./resources/img/59_thumbnail.jpg', 'jpeg')

    # 使用 filter() 滤镜，此处使用模糊效果
    img = Image.open('./resources/img/59.jpg')
    img1 = img.filter(ImageFilter.BLUR)
    img1.save('./resources/img/59_blur.jpg', 'jpeg')


def overturn():
    # 翻转
    img = Image.open('./resources/img/59.jpg')
    img1 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img1.save('./resources/img/左右翻转.jpg', 'JPEG')
    img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img1.save('./resources/img/上下翻转.jpg', 'JPEG')
    img1 = img.transpose(Image.ROTATE_90)
    img1.save('./resources/img/旋转90度.jpg', 'jpeg')
    img1 = img.transpose(Image.ROTATE_180)
    img1.save('./resources/img/旋转180度.jpg', 'jpeg')

    # 学习遍历目录和文件
    list = os.listdir('./resources/img')
    # print(list)
    # 此处仅遍历 img 跟目录，遍历其子目录可以自行学习
    # 使用 os.path.splitext(file)[0] 可获得主文件名
    # 使用 os.path.splitext(file)[-1] 可获得以 . 开头的文件后缀名
    for file in list:
        if os.path.splitext(file)[-1] == '.jpg':
            print(os.path.splitext(file)[0])
    # 处理网络图片
    resp = req.get(
        'https://picl.zhimg.com/100/***.jpg')
    image = Image.open(BytesIO(resp.content))
    # 在此之前可以做相关处理
    image.save('./resources/img/download_test.png')


if __name__ == "__main__":
    # pillow()
    overturn()
