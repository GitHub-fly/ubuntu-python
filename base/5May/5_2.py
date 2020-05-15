"""
基本操作
"""


def base_operation():
    # 去掉列表中的一个最小值和一个最大值，计算剩余元素的平均值
    from random import randint, sample

    def score_mean(lst):
        lst.sort()
        lst2 = lst[1:-1]
        return round((sum(lst2)/len(lst2)), 1)

    lst = [9.1, 9.0, 8.1, 9.7, 19, 8.2, 8.6, 9.8]
    result = score_mean(lst)
    print('平均值：', result)

    # 九九乘法表
    print('九九乘法表')
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d * %d = %d' % (j, i, j * i), end='\t')
        print()

    # 样本抽样
    print('样本抽样')
    lst = [randint(0, 50) for _ in range(100)]
    print(lst[:5])  # [38, 19, 11, 3, 6]
    lst_sample = sample(lst, 10)
    print(lst_sample)   # [33, 40, 35, 49, 24, 15, 48, 29, 37, 24]


"""
字符串高频操作
"""


def str_high_frequency():
    # re 为正则表达式库
    import re
    # strip 用于去除字符串前后的空格
    print(' I love python\t\n '.strip())
    # replace 用于字符串的替换
    print('i love python'.replace(' ', '_'))
    # join 用于合并字符串
    print('_'.join(['book', 'store', 'count']))
    # title 用于单词的首字符大写
    print('i love python'.title())
    # find 用于返回匹配字符串的起始位置索引
    print('i love python'.find('python'))

    # 正则
    # 密码安全要求：6 到 12位，包含英语字母和数字
    # 方法：\da-zA-Z 满足“密码只包含英文字母和数字”
    # \d 匹配数字 0-9
    # a-z 匹配所有小写字符：A-Z 匹配所有大写字符
    # 选用最保险的 fullmatch 方法，查看是否整个字符串都匹配
    pat = re.compile(r'[\da-zA-Z]{6, 12}')
    print(pat.fullmatch('qaz12'))   # 返回 None，长度小于 6
    print(pat.fullmatch('qaz12wsxedc43434'))    # None 长度大于 12
    print(pat.fullmatch('qaz_231'))  # None 含有下划线
    print(pat.fullmatch('n0passw0Rd'))  # 符合


"""
使用 @property 装饰类属性
"""
class Book(object):
    def __init__(self, name, sale):
        self.__name = name
        self.__sale = sale

    @property
    def name(self):
        return self.__name

a_book = Book('magic_book', 100000)
print(a_book.name)


if __name__ == '__main__':
    str_high_frequency()
    base_operation()