"""
校园新闻爬取
"""
# 连接数据库出现 RuntimeError： cryptography is required for sha156_pass
# 解决办法：安装 crytography 即可：pip install cryptography

import requests
from bs4 import BeautifulSoup
import pymysql


def crawl():
    info_list = []
    for num in range(1, 3):
        url = 'http://news.niit.edu.cn/4000/list' + str(num) + '.htm'
        html = requests.get(url).content
        html_doc = str(html, 'utf-8')
        soup = BeautifulSoup(html_doc, 'html.parser')
        content_div = soup.find(
            'div', {'class': 'wp_articlecontent'})
        temp_dict['content'] = content_div.get_text()
        img_list = content_div.find_all('img')
        if len(img_list) >= 1:
            img_url = img_list[0]['src']
            temp_dict['cover'] = 'http://news.niit.edu.cn/' + img_url
        else:
            # 新闻没有图片，使用默认
            temp_dict['cover'] = 'https://profile.csdnimg.cn/E/B/4/3_u010775025'
        info_list.append(temp_dict)
    return info_list


def data_inser(info_list):
    db = pymysql.connect('localhost', 'root', 'root', 'db_python')
    cursor = db.cursor()
    val = []
    for dic in info_list:
        item = (dic['cover'], dic['created'], dic['updated'], dic['is_deleted'],
                dic['is_top'], dic['content'], dic['title'])
        val.append(item)
    sql = "INSERT INTO info_manage(cover, created, updated, is_deleted, is_top, title, content) VALUES(%s,%s,%s,%s,%s,%s,%s,)"
    try:
        # 执行 sql 语句，批量插入
        cursor.executemany(sql, val)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()
