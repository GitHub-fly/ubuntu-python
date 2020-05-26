"""
Numpy_3
"""
import numpy as np
v1 = np.arange(5)
print('输出v1:')
print(v1)   # [0 1 2 3 4]
# 按照元素顺序逐个加 2
print('输出v1+2:')
print(v1+2) # [2 3 4 5 6]
# 执行 v1 * v1，矩阵的乘法是按照元素逐个相乘
print('输出v1*v1：')
print(v1*v1)    # [0 1 4 9 16]
# 5行2列矩阵，取值为 [1-10]的随机整数
v2 = np.random.randint(1, 10, (5, 2))
print('输出v2:')
print(v2)
# 此时无法直接将两个矩阵相乘。why？
# print(v1*v2)
# 1、使用 dot 函数实现矩阵乘法，自己运算验证
v3 = np.dot(v1, v2)
print('输出 dot 函数实现矩阵相乘结果：')
print(v3)
# 输出矩阵的“矩形”，也就是行列维度
print('输出v3的shape：')
print(v3.shape)
# 2、转化为 matrix 对象，在相乘
v3 = np.matrix(v1)*np.matrix(v2)
print('输出使用 matrix 实现的矩阵相乘结果：')
print(v3)
