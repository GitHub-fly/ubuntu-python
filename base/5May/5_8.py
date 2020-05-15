"""
传递当前目录，批量修改文件后缀
"""

import re
from collections import defaultdict
import time
import zipfile
import argparse
import os


def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        # 获取得到文件后缀
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 定位后缀名为 old_ext 的文件
        if old_ext == file_ext:
            # 修改后文件的完整名称
            newfile = split_file[0] + new_ext
            # 实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print('完成重命名')
    print(os.listdir(work_dir))


"""
批量压缩文件
"""
# 导入 zipfile，用来做压缩文件操作


def batch_zip(start_dir):
    # 要压缩的文件夹路径
    start_dir = start_dir
    # 压缩后文件夹的名字
    file_news = start_dir + '.zip'

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(start_dir):
        # 不 replace 的话，就从根目录开始复制
        f_path = dir_path.replace(start_dir, '')
        # 实现当前文件夹以及包含的所有文件的压缩
        f_path = f_path and f_path + os.sep
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    return file_news


"""
按行读文件
"""


def read_line():
    # 正则，匹配单词
    rec = re.compile(r'\s+')
    # 统计单词出现频次
    dd = defaultdict(int)
    # 读取文件 a.txt，r+ 表示读写模式
    with open('./resources/text/大鱼海棠.txt', 'r+') as f:
        # 每次读取一行
        for line in f:
            clean_line = line.strip()
            if clean_line:
                # 正则分词
                words = rec.split(clean_line)
                # 遍历，统计
                for word in words:
                    dd[word] += 1
    # 按照频次降序排列
    dd = sorted(dd.items(), key=lambda x: x[1], reverse=True)
    print('---输出结果---')
    print(dd)


if __name__ == '__main__':
    # batch_rename('./resources/img/', '.jpg', '.jpg')
    # batch_zip('./resources/img')
    read_line()
