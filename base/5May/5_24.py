"""
Numpy_2
"""
import numpy as np
# 组合 ndarray 对象
a = np.arange(10).reshape(2, -1)
print(a)
# 找出 a 中大于 3 的元素索引
# 返回一个元组，带有 2 个 ndarray 对象，分别表示大于 3 的元素第一维、第二维度中的位置
b = np.array(np.where(a > 3))
print(b)
# 使用 np.transpose 方法转置后，结果就能看懂了
print(np.transpose(b))
# 创建一个 [3, 5] 所有元素为 True 的数组
a = np.ones((3, 5), dtype=bool)
print(a)
# 一维转二维
a = np.linspace(1, 5, 10)
print(a.reshape(5, 2))
# 提取出数组中所有奇数
m = np.arange(10).reshape(2, 5)
print(m[m % 2 == 1])
