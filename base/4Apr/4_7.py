import hashlib


def tuple_def():
    # 定义元组
    t = ('张晨', 18, True, '四川成都')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤' # TypeError
    # 变量 t 重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)
    # 将元组转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改他的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    # 将列表转换成元组
    fruits_list = ['apple', 'banan', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)


# 对字符串 s 实现 32 位加密
def hash_cry32(s):
    m = hashlib.md5()
    m.update((str(s).encode('utf-8')))
    return m.hexdigest()


if __name__ == "__main__":
    tuple_def()
    print()
    print(hash_cry32(1))
    print(hash_cry32('hello'))
