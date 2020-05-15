
"""
定义一个类
"""


class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repf__(self):
        return 'id = ' + self.id + ', name = ' + self.name


xiaoming = Student('001', 'xiaoming')
# 返回对象的哈希值
print(hash(xiaoming))
# 返回对象的内存地址
print(id(xiaoming))

# 如果迭代器的所有元素都为真，返回True，否则为false
print(all([1, 0, 3, 6]))
print(all([1, 2, 3]))
# 如果迭代器里有一个元素为真，返回True，否则返回False
print(any([0, 0, 1]))

# 分别将十进制转成二进制、八进制、十六进制
print(bin(10))
print(oct(9))
print(hex(15))

"""
数学内置函数
@Date 2020.05.07
"""

# 长度
dic = {'a': 1, 'b': 3}
print(len(dic))
a = [{'name': 'xiaoming', 'age': 18, 'gender': 'male'},
     {'name': 'xiaoming', 'age': 20, 'gender': 'female'}]
# 最大值
print(max(a, key=lambda x: x['age']))
# pow(x,y,z=None,/) x为底的y次幂，如果有z，取余
print(pow(3, 2, 4))
# 四舍五入，第二个参数代表小数点后保留几位
print(round(10.02222, 3))
a = [1, 4, 3, 2, 1]
# 求和
print(sum(a))
# 指定求和的初值为10
print(sum(a, 10))
# 求绝对值或复数的模
print(abs(-6))
# 分别取商和余数
print(divmod(10, 3))
# 定义复数
print(complex(1, 2))
