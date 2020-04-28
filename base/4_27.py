"""
用myqr库制作二维码
"""
from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont

# 图片登录二维码，如使用gif背景，则可以生成动态背景效果


def img_code():
    # myqr.run(words='https://wx4.sinaimg.cn/mw690/006eX5q01y1ge8qjozqxkj30wg0p63zo.jpg',
    myqr.run(words='https://v.qq.com/x/page/b09584l320o.html',
             # 设置容错率为最高
             version=1,
             # 控制纠错水平，范围是L、M、Q、H从左到右依次升高
             level='H',
             # 背景图
             picture='./resources/img/1.jpg',
             # 彩色二维码
             colorized=True,
             # 用以调色图片的对比度，1.0标识原始图片，更小的值标识更低的对比度，更大反之，默认为1.0
             contrast=1.0,
             # 用来调节图片亮度，其余用法和取值上相同
             brightness=1.0,
             # 保存文件的名字，格式可以使jpg、png、bmp、gif
             save_name='codeImg.png',
             # 保存位置
             save_dir=os.getcwd() + '/resources/img/')


def draw():
    img = Image.open('./resources/img/codeImg.png')
    w, h = img.size
    txt = '曾经的岁月---“这么棒的阅读”',
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./resources/font/SimHei.ttf', 26)
    # draw.text((w/2-100, 10), txt, (0, 0, 0), font=font)
    draw.text(xy=((w/2-100, 10)), text=txt)
    img.save('./resources/img/code2.png')


if __name__ == '__main__':
    img_code()
    draw()
