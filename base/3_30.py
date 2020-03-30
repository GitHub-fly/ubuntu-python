import os
import time
from termcolor import *


# 打印杨辉三角
def main_pascal():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col in range(len(yh[row])):
                if col == 0 or col == row:
                    yh[row][col] = 1
                else:
                    yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
                print(yh[row][col], end='\t')
        print()


# 跑马灯
def main_marquee():
    content = '北京欢迎你，为你开天辟地。。。。。。。。'
    color = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    i = 0
    while True:
        # 清理屏幕上的输出
        os.system('cls')
        index = i % len(color)
        # print(colored(content[i % len(content)], color[index]))
        print(colored(content, color[index]))
        # print(content)
        # 休眠 200 毫秒
        time.sleep(0.1)
        content = content[1:] + content[0]
        i = i + 1


if __name__ == '__main__':
    # main_pascal()
    main_marquee()
