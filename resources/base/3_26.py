# 英制单位英寸和公制单位厘米互换
def meter():
    value = float(input('请输入长度：'))
    unit = input('请输入单位：')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    elif unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('请输入有效的单位')


# 百分制成绩转换为等级制成绩
def grade_def():
    score = float(input('请输入成绩：'))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('对应的等级是：', grade)


# 输入三条边长，如果能构成三角形就计算周长和面积
def triangle_area():
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print('周长：%f' % (a + b + c))
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('面积：%f' % area)
    else:
        print('不能构成三角形')


if __name__ == '__main__':
    # meter()
    # grade_def()
    triangle_area()

