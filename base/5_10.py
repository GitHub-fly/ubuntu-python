"""
抓取天气
"""
from lxml import etree
import requests


def request_temperature():
    # 中国天气网
    url = 'http://www.weather.com.cn/weather1d/101190111.shtml#input'
    # request 发起请求
    with requests.get(url) as res:
        content = res.content
        # 使用 lxml 的 etree 解析页面
        html = etree.HTML(content)
    # 通过 xpath 定位周边城市和景区，返回 list
    location = html.xpath('//*[@id="around"]//a[@target="_blank"]/span/text()')
    # 温度 list
    temperature = html.xpath('//*[@id="around"]/div/ul/li/a/i/text()')
    # 将上述两个 list 作为 key 和 value 合成字典
    dictionary = dict(zip(location, temperature))
    return dictionary


if __name__ == '__main__':
    print(request_temperature())

