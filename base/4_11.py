import time
from threading import Thread

import requests

# 继承 Thread 类创建自定义的线程类


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        # filename = self.url[self.url.rfind('/') + 1:]
        filename = self.url[(self.url.find('-') + 1): self.url.find('?')]
        resp = requests.get(self.url)
        with open('./resources/img/unsplash/' + filename + '.jpg', 'wb') as f:
            f.write(resp.content)


def main():
    """ 老班的
    # 使用了天行数据接口提供的网络 API，用自己的 Key 替换掉下面代码的中 APIKey 即可

    resp = requests.get('http: // api.tianapi.com/film/index?key=c3c7fe4d48dcd3164eee8ca54eaaf180'
                        '& num=10')
    # 将服务器返回的 JSON 格式化的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()
    """

    """ 自己的
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    page = 3
    url = 'https://unsplash.com/napi/photos?page=' + str(page) + '&per_page=30'
    for page in range(2):
        time.sleep(0.5)
        response = requests.get(url, headers=headers)
        for item in response.json():
            url = item['urls']['raw']
            print(url)
            # 通过多线程的方式实现图片下载
            DownloadHanlder(url).start()


if __name__ == '__main__':
    main()
