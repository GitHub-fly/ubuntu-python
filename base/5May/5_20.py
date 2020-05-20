"""
那些操作
"""
from functools import reduce
import random

# 一行代码生成 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 使用列表生成式，创建列表，观察元素出现规律，可得出如下代码
a = [2*i+1 for i in range(10)]
print(a)

# 写一个等差数列，产生一个首项为 10，公差为 12，末项不大于 100 的列表
# 使用列表生成式创建
a = list(range(10, 100, 12))
print(a)

# 一行代码求 1 到 1000 内整数和
# 方法1：使用 Python 内置函数 sum 求和
s = sum(range(1000))
print(s)
# 方法2：使用 functools 模块中的 reduce 求和
s = reduce(lambda x, y: x+y, range(1000))
print(s)

# 打乱一个列表
# 使用 random 模块，shuffle 函数打乱原来列表
a = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(a)
print(a)
