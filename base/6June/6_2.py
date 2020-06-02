"""
数据分析案例--猫眼电影
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 用 pandas 导入数据集
# read_csv 使用说明
# 第一个参数表示文件的相对路径
# 第二个关键字参数：delimiter='::',表示文件分隔符使用::
# 后面几个关键字参数分别代表使用的引擎，文件没有表头，所以 header 为 None;
# 导入后 DataFrame 的列名，使用 names 关键字设置，这个参数比较有用。
path = '././resources/dataset/maoyan.csv'
df = pd.read_csv(path, sep=',', encoding='utf-8', index_col=False)

# drop 函数用法：DataFrame.drop(label=None, axis=0, index=None, columns=None, inplace=False)
# 参数说明：
# labels 就是要删除的行列的名字，用列表给定
# axis 默认为0，只删除行，因此删除 columns 时要指定 axis=1：
# index 直接指定要删除的行
# columns 直接指定要删除的列
# inplace=False，默认该删除操作不改变原数据，而是返回一个执行删除操作后的新 dataframe:
# inplace=True, 则会直接在原数据上进行删除操作，删除后无法返回
# 从数据中删除了第一列（电影编号）
df.drop(df.columns[0], axis=1, inplace=True)
# 滤除缺失数据
df.dropna(inplace=True)
# 删除重复数据
df.dropna(inplace=True)
# 删除重复数据
df.drop_duplicates(inplace=True)
# 查看数据
df.head(10)
print(df)

# 查看数据的结构
df.info()
print(df.columns)
print(df.shape)

# 数据可视化，不加一下设置，图标标题等会中文乱码
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # mac 系统中文显示
# plt.rcParams['font.sans-serif'] = ['./resources/font/SimHei'] # Ubuntu做法？
fig, ax = plt.subplots(figsize=(9, 6), dpi=70)
df[df[u'上映时间'] < 2018][u'上映时间'].value_counts(
).sort_index().plot(kind='line', ax=ax)
ax.set_xlabel(u'时间（年）')
ax.set_ylabel(u'上映数量')
ax.set_title(u'上映时间&上映的电影数目')
plt.savefig('./resources/img/maoyan1.png')
plt.show()

# 上映时间&上映数量&评分的关系图
x = df[df[u'上映时间'] < 2018][u'上映时间'].value_counts().sort_index().index
y = df[df[u'上映时间'] < 2018][u'上映时间'].value_counts()
y2 = df[df[u'上映时间'] < 2018].sort_values(
    by=u'上映时间').groupby(u'上映时间').mean()[u'评分'].values

fig, ax = plt.subplots(figsize=(10, 5), dpi=70)
ax.plot(x, y, label=u'上映数量')
ax.set_xlim(1980, 2017)
ax.set_xlabel(u'上映时间')
ax.set_ylabel(u'上映数量')
ax.set_title(u'时间&上映数量&评分均值')
ax2 = ax.twinx()
ax2 = ax.twinx()
ax2.plot(x, y2, c='y', ls='--', label=u'评分')
ax.legend(loc=1)
ax2.legend(loc=2)
plt.savefig('././resources/img/maoyan2.png')
plt.show()

# 世界&上映时间&均值评分
fig, ax = plt.subplots(figsize=(10, 7), dpi=60)
df[df[u'评分'] > 0].groupby(u'上映时间').mean()[u'评分'].plot(kind='line', ax=ax)
ax.set_ylabel(u'评分')
ax.set_title(u'世界&上映时间&均值评分')
plt.savefig('././resources/img/manyan3.png')
plt.show()
