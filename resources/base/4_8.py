"""
类和对象1
"""
from pyecharts import charts


class Student(object):

    # __init__ 是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定 name 和 age 两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('{}正在学习{}。'.format(self.name, course_name))

    # PEP 8 要求标识符的名字全用小写多个单词用下划线连接
    def watch_movie(self):
        if self.age < 18:
            print('{}只能看《熊出没》。'.format(self.name))
        else:
            print('{}正在看3D大片。'.format(self.name))


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('张晨', 28)
    # 给对象发 Student 消息
    stu1.study('Python程序设计')
    # 给对象发 watch_av 消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


"""
使用 pyecharts 绘制仪表盘
"""


def draw_gauge():
    # 仪表盘
    gauge = charts.Gauge()
    gauge.add(
        'Python 小例子',
        [
            ('Python 机器学习', 30),
            ('Python 基础', 70),
            ('Python 正则', 90)
        ]
    )
    gauge.render(path='./resources/仪表盘.html')
    print('ok')


if __name__ == '__main__':
    main()
    draw_gauge()
