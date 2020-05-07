"""
dict和set经典使用1
"""

# 1、批量插入
d = {'a': 1, 'b': 2}
d.update({'c': 3, 'd': 4, 'e': 5})
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 2、不存则插入，存在则不插入不更新
d = {'a': 1, 'b': 2}
x = d.setdefault('c', 3)
y = d.setdefault('a', 1)
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# 3、字典并集


def merge(d1, d2):
    return {**d1, **d2}


print(merge({'a': 1, 'b': 2}, {'c': 3}))
# {'a': 1, 'b': 2, 'c': 3}

# 4、字典差


def difference(d1, d2):
    return dict([(k, v) for k, v in d1.items() if k not in d2])


print(difference({'a': 1, 'b': 2, 'c': 3}, {'b': 2}))
#{'a': 1, 'c': 3}

# 5、按键排序


def sort_by_key(d):
    return sorted(d.items(), key=lambda x: x[0])


print(sort_by_key({'a': 3, 'b': 1, 'c': 2}))
#[('a', 3), ('b', 1), ('c', 2)]
# 6、按值排序


def sort_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])


print(sort_by_value({'a': 3, 'b': 1, 'c': 2}))
#[('b', 1), ('c', 2), ('a', 3)]

"""
dict和set经典使用2
"""

# 7、最大值


def max_key(d):
    if len(d) == 0:
        return []
    max_key = max(d.keys())
    return (max_key, d[max_key])


print(max_key({'a': 3, 'c': 3, 'b': 2}))  # ('c', 3)

# 8、最大字典值


def max_value(d):
    if len(d) == 0:
        return []
    max_val = max(d.values())
    return [(key, max_val) for key in d if d[key] == max_val]


print(max_key({'a': 3, 'c': 3, 'b': 2}))  # ('c', 3)

# 9、集合最值：找出集合中的最大、最小值，并装到元组中返回


def max_min(s):
    return (max(s), min(s))


print(max_min({1, 3, 5, 7}))  # (7, 1)

# 10、单字符串：若组成字符串的所有字符仅出现一次，则被称为单字符串


def single(string):
    return len(set(string)) == len(string)


print(single('love_python'))  # False
print(single('python'))  # True
