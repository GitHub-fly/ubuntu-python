import math
import random
import os
from PIL import Image


def picture_wall():
    x = 0
    y = 0
    # 读取目录下所有文件
    imgs = os.listdir('./resources/img/M')
    # 将序列的所有元素随机排序
    random.shuffle(imgs)
    # 创建 640 * 640 的图片用于填充各小图片
    newImg = Image.new('RGBA', (640, 640))
    # 以 640 * 640 来拼接图片，math.sqrt() 开平方根计算每张小图片的宽高
    width = int(math.sqrt(640 * 640 / len(imgs)))
    # 每行图片数
    numLine = int(640 / width)
    for i in imgs:
        img = Image.open('./resources/img/M/' + i)
        # 缩小图片
        img = img.resize((width, width), Image.ANTIALIAS)
        # 拼接图片，一行排满，换行拼接
        newImg.paste(img, (x * width, y * width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1
            newImg.save('./resources/adl.png')


if __name__ == "__main__":
    picture_wall()
