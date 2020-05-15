import math


# 输入半径计算圆的周长和面积
def circle():
    radius = float(input('请输入圆的半径：'))
    perimeter = 2 * math.pi * radius
    area = math.pi * radius * radius
    print('周长：%.2f' % perimeter)
    print('面积：%.2f' % area)


# 将华氏度转换为摄氏度的方法
def degree():
    f = float(input('请输入华氏温度：'))
    c = (f - 32) / 1.8
    print('%.1f 华氏度 = %.1f 摄氏度' % (f, c))


# 输入年份，如果是闰年输出True，否则输出False
def is_leap_year():
    year = int(input('请输入年份：'))
    # 如果代码太长写成一行不便于阅读，可以使用 “\” 对代码进行折行
    is_leap = (year % 4 == 0 and year % 100 != 0) or \
        year % 400 == 0
    print(is_leap)


if __name__ == '__main__':
    # circle()
    # degree()
    is_leap_year()
