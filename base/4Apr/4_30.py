"""
使用Pandas做数据分析（1）
如果已经安装的请忽略
pip3 install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com pandas
四月，再见，Hi~~May
"""

import pandas as pd

# 导入数据集
path1 = './resources/csv/data.csv'
# 数据集存入一个名为 chipo 的数据框
chipo = pd.read_csv(path1, sep='\t')
# 查看前 10 行
print(chipo.head(10))
# 数据集中有多少列
print(chipo.shape[1])
# 打印出全部的列名
print(chipo.columns)
# 数据集的索引
print(chipo.index)
# print(chipo['follower_count'].nunique())