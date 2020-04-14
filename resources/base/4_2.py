# 列表排序
def list_sorted():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    # 默认排序为首字母排序
    list2 = sorted(list1)
    # sorted 函数返回列表排序后的拷贝不会修改传入的列表
    list3 = sorted(list1, reverse=True)
    # 通过 key 关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


def list_split():
    fruits = ['grape', 'apple', 'straberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 列表切片
    fruits2 = fruits[1:4]
    # ['apple', 'strawberry', 'waxberry']
    print(fruits2)
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    # ['grape', 'apple', 'straberry', 'waxberry', 'pitaya', 'pear', 'mango']
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['pitaya', 'pear']
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    # ['mango', 'pera', 'pitay', 'waxberry', 'strawberry', 'apple', 'grape']
    print(fruits5)


if __name__ == '__main__':
    # list_sorted()
    list_split()
