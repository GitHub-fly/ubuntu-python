"""
几种方式读文本文件
"""


def main_one():
    import time
    try:
        # 一次性读取整个文件内容
        with open('./resources/text/大鱼海棠.txt', 'r', encoding='utf-8') as f:
            print(f.read())
        # 读取文件按行读取到列表中
        with open('./resources/text/大鱼海棠.txt', mode='r') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
            print()
    except FileNotFoundError as e:
        print(e)
    except LookupError as e:
        print(e)
    except UnicodeDecodeError as e:
        print(e)


"""
写文本文件
"""


def main_two():
    str = '''    昨天老师还在问我们，希望是什么？在这之前，我根本不相信希望这种东西，但现在
我相信，我相信希望是我们这个年代，像钻石一样珍贵的东西。希望，希望是我们唯一回
家的方向。回来吧！加入我们一起战斗！点燃木星！救回我们的地球！
    '''

    """
    # w 写入，如果文件存在，则清空内容后写入，不存在则创建
    try:
        f = open('./resources/text/大鱼海棠.txt', 'w', encoding='utf-8')
        print(f.write(str))
        f.close

        # a 写入，文件存在，则在文件内容后追加写入，不存在则创建
        f = open('./resources/text/大鱼海棠.txt', 'a', encoding='utf-8')
        print(f.write(str))
        f.close()
    except IOError as e:
        print(e)
    """
    # with 关键字系统会自动关闭文件和处理异常
    with open('./resources/text/大鱼海棠.txt', 'a') as f:
        f.write(str)
    print('写入完毕')


"""
读写二进制文件
"""


def main_three():
    # 将 1.jpg 以二进制只读方式打开，读入 data 变量
    with open('./resources/img/59.jpg', 'rb') as fs1:
        data = fs1.read()
        print(type(data))
    # 将 1.jpg 二进制写的方式打开，写入 1_copy.jpg
    with open('./resources/img/59_copy.jpg', 'wb') as fs2:
        fs2.write(data)


"""
读写 JSON 文件
"""


def main_four():
    # json 模块主要有四个比较重要的函数，分别是：
    # dump  - 将 python 对象按照 JSON 格式序列化到文件中
    # dumps - 将 python 对象处理成 JSON 格式的字符串
    # load  - 将文件中的 JSON 数据反序列化成对象
    # loads - 将字符串的内容反序列化成 python 对象
    import json
    # 定义字典对象
    mydict = {
        'name': 'Jack',
        'age': 20,
        'qq': 12345678,
        'friends': ['Mary', 'Sophia'],
        'cars': [
            {
                'brand': 'Audi 奥迪',
                'max_speed': 280
            },
            {
                'brand': 'Benz 奔驰',
                'max_speed': 320
            }
        ]
    }
    # 将字典对象序列化到文件
    with open('./resources/json/Jack.json', 'w', encoding='utf-8') as fs:
        json.dump(mydict, fs, ensure_ascii=False)
    print('保存数据完成！')

    # 从文件中读取，反序列化成对象
    with open('./resources/json/Jack.json', 'r', encoding='utf-8') as fs:
        mydict = json.load(fs)
        print(mydict)
    print('保存数据完成！')


if __name__ == '__main__':
    # main_one()
    # main_two()
    # main_three()
    main_four()
