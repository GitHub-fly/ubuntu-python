"""
Pandas_1
"""
import pandas as pd
# Pandas 读取 URL 路径的文件，得到（149 rows x 5 columns）的数据集
result = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
print(result)
# 创建并保存数据
d = {'id': [1, 2], 'name': ['gz', 'lh'], 'age': [10, 12]}
df = pd.DataFrame(d)
# test.csv 文件分割符为 \t，如果使用 sep 默认的逗号分隔符，读入后的数据混为一体
df.to_csv('test.csv', sep='\t')
# 读取数据，查看结果
df = pd.read_csv('test.csv')
print(df)
# sep 必须设置为 '\t'，数据分割才会正常
df = pd.read_csv('test.csv', sep='\t')
print(df)

# 读取之列选择属性
# 参数用于选取数据文件的哪儿些列到 DataFrame 中
# 只想使用元数据文件的  id 和 age 两列，那么可以为 usecols 参数赋值为 ['id', 'name']
df = pd.read_csv('test.csv', delim_whitespace=True, usecols=['id', 'name'])
print(df)
