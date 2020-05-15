"""
requests 请求 api，用字典和列表保存为 json
"""

import requests
import json


def test_api():
    resp = requests.get(
        'http://api.tianapi.com/allnews/index?key=6108db9f49b44a21f43304eb78af39f6&num=10&col=7')
    newslist = json.loads(resp.text)['newslist']
    result = []
    data = './resources/json/data.json'
    for news in newslist:
        temp_dict = {}
        temp_dict['ctime'] = news['ctime']
        temp_dict['title'] = news['title']
        temp_dict['description'] = news['description']
        temp_dict['pic_url'] = news['picUrl']
        temp_dict['url'] = news['url']
        result.append(temp_dict)
    with open(data, 'w',) as f:
        json.dump(result, f, ensure_ascii=False)


if __name__ == "__main__":
    test_api()
