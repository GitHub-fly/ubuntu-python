"""
基础词云
推荐一键安装一下库，部分已经安装过的也可以不安装
pip3 install numpy matplotlib pillow wordclound imageio jieba snownlp \
    itchat -i https://pypi.tuna.tsinghua.edu.cn/simple
"""


def basic_word_cloud():

    import wordcloud
    import random

    # 创建词云对象
    w = wordcloud.WordCloud()
    # 通过字符串生成词云
    w.generate('From tomorrow on, be a happy man.Feed horses, chop wood, travel the world.\
        From tomorrow on, care about food and vegetables. I have a house, facing the sea, spring flowers.')
    # 生成本地图片
    # w.to_file('./resources/img/output1.png')

    # 创建词云对象，设置词云图片宽、搞、字体、背景颜色等参数
    # 中文字体需要提前下载中文字体文件
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='#eeeeee',
                            font_path='./resources/font/SimHei.ttf')
    # w.generate('从明天起，做一个幸福的人，喂马、劈柴、周游世界，从明天起，关心粮食和蔬菜。 \
    #     我有一所房子，面朝大海，春暖花开。从明天起，和每一个亲人通信，告诉他们我的幸福。 \
    #     愿你有一个灿烂的前程，愿你有情人终成眷属，愿你在尘世获得幸福，我只愿面朝大海，春暖花开。')
    w.generate('刘亚东、李志鹏、司凯旋、司凯超、司晋宇、彭雨茹、赵天宁、张浩杰、张晨星、李瑞杰、张泽欣、韩敏蝶、苏佳妮、田晋婷、司毅卓')
    w.to_file('./resources/img/output2.png')


def participle_word_cloud():
    # 导入词云制作库 wordcloud 和中文分词库 jieba
    import jieba
    import wordcloud

    # 构建并配置词云对象 w
    w = wordcloud.WordCloud(
        width=1000,
        height=700,
        background_color='#6c909e',
        colormap='GnBu',
        font_path='./resources/font/SimHei.ttf'
    )

    # 调用 jieba 的 lcut() 方法对原始文本进行中文分词，得到 string
    txt = '南京工业职业技术学院（本科）毗邻著名的钟山风景区，是一所历史悠久、底蕴厚重的百年名校。 \
        前身是我国近代民主革命家、社会活动价、教育家黄炎培先生创建于1918年的中华职业学校---我国第一所 \
        以“职业”冠名的学校。1952年，黄炎培出任政务院副总理兼首任工业部长，将学校交由轻工业部管理：\
        1954年，更名为上海机械学校：1960年，整体搬迁至南京，更名为轻工业部南京机电学校：1998年。\
        由轻工业部划归江苏省管理：1999年，升格为高等职业院校，更名为南京工业职业技术学院：\
        2019年，升格为职业本科学校。'
    txtlist = jieba.lcut(txt)
    string = ' '.join(txtlist)

    # 将 string 变量传入 w 的 generate() 方法，给词云输入文字
    w.generate(string)

    # 将词云图片导出到当前文件夹
    w.to_file('./resources/img/output4.png')


def external_text_word_cloud():
    import wordcloud
    import random

    # 读入外部文本文件
    f = open('./resources/text/大鱼海棠.txt', encoding='utf-8')
    # txt = f.read()
    txt = '刘亚东、李志鹏、司凯旋、司凯超、司晋宇、彭雨茹、赵天宁、张浩杰、张晨星、李瑞杰、张泽欣、韩敏蝶、苏佳妮、田晋婷、司毅卓'
    # 更换一下背景颜色和整体风格
    # colormap 参考 https://matplotlib.org/examples/color/colormaps_reference.html
    w = wordcloud.WordCloud(
        scale=2,    # 缩放 2 倍
        max_font_size=100,
        background_color='#383838',
        colormap='PuRd',
        font_path='./resources/font/SimHei.ttf'
    )

    # 将 txt 变量传入
    w.generate(txt)
    w.to_file('./resources/img/output3.png')


if __name__ == "__main__":
    basic_word_cloud()
    # participle_word_cloud()
    external_text_word_cloud()
