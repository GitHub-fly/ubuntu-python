"""
爬取实验楼所有的课程信息
学习 xpath 和 tree 结合获取节点信息
可以按关键词统计一些数据，比如 Java、C 课程的数据
安装：pip3 install lxml
"""

import requests
from lxml import html


def crawl():
    course_list = []
    for num in range(1, 25):
        url = 'https://www.shiyanlou.com/courses/?page=' + str(num)
        content = requests.get(url)
        tree = html.fromstring(content.text)
        course_names = tree.xpath('//h6[@class="course-name"]/text()')
        course_descriptions = tree.xpath(
            '//div[@class="course-description"]/text()')
        course_covers = tree.xpath('//img[@class="cover-image"]/@src')
        for index in range(0, len(course_names) - 1):
            temp_dict = {}
            temp_dict['name'] = course_names[index].strip()
            temp_dict['description'] = course_descriptions[index].strip()
            temp_dict['cover'] = course_covers[index]
            course_list.append(temp_dict)
            # print(len(course_list))
    return course_list


if __name__ == "__main__":
    list = crawl()
    print(len(list))
    # print(list)
