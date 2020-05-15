"""
多线程2
"""
import threading
from time import ctime, sleep

# 创建 player() 函数，用于接收 name 和 time，用于确定要播放的文件及时长


def player(name, sleepTime):
    for i in range(2):
        print('正在播放:', (name, ctime()))
        sleep(sleepTime)


# 字典：播放的文件与播放的时长（秒）
lists = {
    'test1.mp3': 5,
    'test2.mp3': 2,
    'test3.mp3': 3
}
threads = []
lens = len(lists)

# 遍历歌单，通过字典的 items() 方法来循环的取 name 和 time，取到的这两个值用于 创建线程
for n, t in lists.items():
    t = threading.Thread(target=player, args=(n, t))
    threads.append(t)


if __name__ == '__main__':
    # 启动线程
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print('结束播放', ctime())
