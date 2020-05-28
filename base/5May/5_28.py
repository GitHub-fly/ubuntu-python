"""
Pandas_2
"""
import pandas as pd
# Pandas 之分块读入数据
# iterator 取值 boolean，默认为 False，返回一个 TestFileReader 对象，以便逐块处理文件
chunk = pd.read_csv('test.csv', sep='\s+', iterator=True)
# 先读入一行，get_chunk 设置为 1 表示一次读入一行，目标文件一共 2 行
print(chunk.get_chunk(1))
# 再读入下一行
# print(chunk.get_chunk(1))
# 此时已到文件末尾，再次读入会报异常

# Pandas 读取 空值处理
# 假设我们的数据文件如下，data 列中有一个 # 值，我们想把它处理成 NaN 值
d = {'id': [1, 2], 'name': ['xxq', 'zhj'], 'age': [21, 21], 'data': ['2020-05-28', '#']}
df = pd.DataFrame(d)
df.to_csv('test_date.csv', sep=' ', index=False)
df = pd.read_csv('test_date.csv', sep='\s+', na_values=['#'])
print('\n', df)


"""
Pandas_3
"""
import pandas as pd
import numpy as np

# Series 是 pandas 两大数据结构中（DataFrame，series）的一种
# 每个 Series 对象都由两个数组组成：
# index: 它是从 NumPy数组继承的 Index 对象，保存标签信息
# values：保存值的 NumPy数组

# 1. 创建一个 series
# Series 的标准构造函数：Series(data=None, index=None, dtype=None, name=None)
ps = pd.Series(data=[-3, 2, 1], index=['a', 'f', 'b'], dtype=np.float32)
print(ps)
print('***************')
# 2. Series 增加元素（Pandas 允许包含重复的标签）
ps = ps.append(pd.Series(data=[-8.0], index=['f']))
print(ps)
print('***************')
# 3. Series 访问元素，有两种方法
# 工通过索引访问
print(ps[2])
# 工通过标签访问
print(ps['f'])
# 4. Series 之删除元素，append 操作和 drop 操作都是发生在原数据的副本上，不是原数据上
ps = ps.drop('f')
print(ps)
print('***************')
# 5. Series 之修改元素
ps['b'] = 10.0
print(ps)