"""
集合基本操作
"""
# 创建，也是{}，但容器内的元素不是键值对
a = {1, 2, 3}
print(a)
# 也可以用内置的 set 函数创建
b = set([1, 3, 5, 7])
print(b)

# 常用方法：集合间的并、交、差集、子集判断
# 求并集
a = {1, 3, 5, 7}
b, c = {3, 4, 5, 6}, {6, 7, 8, 9}
d = a.union(b, c)   # {1, 3, 4, 5, 6, 7, 8, 9}

# 求差集
a = {1, 3, 5, 7}
b, c = {3, 4, 5, 6}, {6, 7, 8, 9}
d = a.difference(b, c)  # {1}

# 求交集
a = {1, 3, 5, 7}
b, c = {3, 4, 5, 6}, {6, 7, 8, 9}
d = a.intersection(b, c)    # {}

# 判断 a 是否为 b 的子集
a = {1, 3, 5, 7}
b = {3, 4, 5, 6}
print(a.issubset(b))    # False
print(a.issubset({1, 3, 5, 7, 8}))  # True


"""
字典基本操作
"""
d = {'a': 1, 'b': 2, 'c': 3}
# 遍历
for key, val in d.items():
    print(key, val)
# 两种方法获取所有键集合
set(d)
set(d.keys())
# 获取所有值集合
set(d.values())
# 判断键是否在字典中
if 'c' in d:
    print('键 c 在字典 d 中')
# 获取某键对应的值
d.get('c')
# 添加或修改一个键值对
d['d'] = 4
print(d)
# 两种方法删除一个键值对
del d['d']
print(d)
d.pop('c')
print(d)

# 字典的三个视图
d = {'a': 1, 'b': 2, 'c': 3}
d.keys()
d.values()
d.items()


"""
字典创建方法
"""
# 5 种创建方法，注意 dict 是关键词，所有变量名取的是 dic
# 1、手动创建
empty = {}
dic = {'a': 1, 'b': 2, 'c': 3}
print(dic)
# 2、使用 dict() 构造函数
dict(a=1, b=2, c=3)
print(dic)
# 3、键值对 + 关键字参数
dict({'a': 1, 'b': 2}, c=3, d=4)
print(dic)
# 4、可迭代对象：列表、元素又为一个元组，后面再加一系列关键字参数
dict([('a', 1), ('b', 2)], c=3)
print(dic)
# 5、fromkeys() 方法
dic = {}.fromkeys(['k1', 'k2', 'k3'], [1, 2, 3])
print(dic)
