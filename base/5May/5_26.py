"""
Numpy_4
"""
import numpy as np
m = np.random.randint(1, 10, (3, 4))
print('原矩阵\n', m)
# 所有元素的平均值，求某一维度的平均值，设置 axis 参数
print('平均值：', m.mean(), m.mean(axis=1))
# 最大值，某一个维度的最大值
print('最大值：', m.max(), m.max(axis=1))
# 最小值、求和同理，min(), sum()
# 求所有维度上元素的累乘、某一维度上的累成
print('累乘\n', m.cumprod(), m.cumprod(axis=1))
# 对角线成元素的和
print('对角线元素之和：', m.trace())
# 降维
v1 = np.random.randint(1, 10, (2, 3))
print('v1:\n', v1)
v2 = v1.flatten()
print('降维成v2:', v2)

# 使用 NumPy，下载 iris 数据集。仅提取数据集的第二列 usecols = [1]:
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[1])
print(data)
# 求出最大值、最小值
smax = np.max(data)
smin = np.min(data)
print('max=', smax, ',min=', smin)
# 归一化：把数据变成(0, 1) 或者 (1, 1) 之间的小数
# 把数据映射到 0~1 范围之内处理，更加便捷快速
# 归一化公式
s = (data - smin) / (smax - smin)
# 只打印小数点后三位
np.set_printoptions(precision=3)
print(s)
