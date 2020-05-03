"""
List基本操作
"""


def list_def():
    # 创建
    empty = []
    lst = [1, 'xiaoming', 29.5, '17312662388']
    lst2 = ['001', '2019-11-11', ['三文鱼', '电烤箱']]
    # 长度
    print(len(lst2))
    # 遍历
    for _ in lst:
        print(f'{_}的类型为{type(_)}')

    # 插入删除等操作
    sku = lst2[2]
    # append 追加到 list 尾部
    sku.append('烤鸭')
    # insert 到指定索引处
    sku.insert(1, '牛腱子')
    # pop 移除尾部元素
    item = sku.pop()
    # remove 移除、或者 sku.remove(sku[0])
    sku.remove('三文鱼')
    print(sku)

    # 生成 1 到 20 的序列，步长为 3，放入 list
    a = list(range(1, 20, 3))
    print(a)
    # 各种切片操作
    print(a[-1], a[:-1], a[1:5], a[1:5:2], a[::3], a[::-3])


"""
元组是不可变的，所以没用插入和删除方法
"""


def numpy_def():
    from numpy import random
    a = ()  # 空元组对象
    b = (1, 'xiaoming', 29.5, '17312662388')
    c = ('001', '2020-05-03', ['三文鱼', '电烤箱'])
    # 从 [1, 5) 区间内随机选择 10 个数
    a = random.randint(1, 5, 10)
    # 转 tuple：(1, 4, 2, 1, 3, 3, 2, 3, 4, 2)
    at = tuple(a)
    # 统计 3 出现的次数
    print(at.count(3))


if __name__ == '__main__':
    list_def()
    numpy_def()
