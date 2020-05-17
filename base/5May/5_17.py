"""
列表和迭代器
"""
from collections.abc import Iterator

# 列表 a 不是迭代器类型
a = [1, 3, 5, 7]
# 要想成为迭代器，需要经过内置函数 iter 包装
a_iter = iter(a)
# 验证 a_iter 是否 Iterator 迭代器
flag = isinstance(a_iter, Iterator)
print(flag)  # True

# 分别遍历 a、a_iter
for i in a:
    print(i, end=' ')
print()

for i in a_iter:
    print(i, end=' ')
print('\n*************')

# 再次遍历 a、a_iter 就会不同，a 正常打印，a_iter 没有打印任何信息
# 列表不论遍历多少次，表头位置始终是第一个元素
# 迭代遍历结束后，不再指向原来的表头位置，而是为最后元素的下一个位置
for i in a:
    print(i, end=' ')

print()

for i in a_iter:
    print(i, end=' ')
# 要想迭代器 a_iter 重新指向 a 的表头，需要重新创建一个新的迭代 a_iter_copy
a_iter_copy = iter(a)
# 只有迭代器对象才能与内置函数 next 结合使用
# 调用 next，输出迭代器指向 a 的第一个元素
print(next(a_iter_copy))
# 无法通过调用 len 获得迭代器的长度，下面语句会报错
# print(len(a_iter_copy))

# 原因：等迭代到最后一个元素后，再执行 next，会触发 StopIteration 异常
# 通过捕获这个异常，可以求出迭代器指向 a 的长度
a = [1, 3, 5, 7]
a_iter_copy2 = iter(a)
iter_len = 0
try:
    while True:
        i = next(a_iter_copy2)
        print(i, end=' ')
        iter_len += 1
except StopIteration:
    print('\niterator stops')

print('length of iterator is %d' % (iter_len,))
