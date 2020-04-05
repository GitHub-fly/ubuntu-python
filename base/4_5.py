"""
爬取一页知乎某专栏数据
"""

import requests
import csv
import json


def crawl():
    url = "https://www.zhihu.com/api/v4/columns/NewsFlash/followers"
    # 必须制定 UA，否则知乎服务器会判定请求不合法
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    # 选择并打开一个文件夹
    csvfile = open('./resources/csv/data.csv', 'w', newline='')
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    keys = ['id', 'name', 'url', 'gender', 'avatar_urll', 'follower_count']
    writer.writerow(keys)
    for i in range(10000):
        # 查询参数
        params = {
            'limit': 20,
            'offset': i,
            'include': 'data[*].follower_count, gender, is_followed, is_following'
        }
        response = requests.get(url, headers=headers, params=params)
        # 解析返回的数据
        j = 1
        for dic in response.json().get('data'):
            writer.writerow([dic['id'], dic['name'], dic['url'],
                             dic['gender'], dic['avatar_url'], dic['follower_count']])
            j += 1
    csvfile.close()


if __name__ == "__main__":
    crawl()
