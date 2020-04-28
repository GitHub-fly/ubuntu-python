"""
中文文本的情感分析
pip3 install snownlp
"""

from snownlp import SnowNLP

text = '人们日常所犯最大的错误',
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标注
tags = [x for x in s.tags]
print(tags)
# 断句
print(s.sentences)
# 拼音
print(s.pinyin)

# 情绪判断，返回值为正面情绪的概率，越是接近1表示正面情绪，越是接近0表示负面情绪
text1 = '这部电影真心棒'
text2 = '这部电影监制烂到爆'
# 这部电影真心棒 0.98425723323704297
print(text1, s1.sentiments)
# 这部电影监制烂到爆 0.0566960892739531
print(text2, s2.sentiments)


# 关键字抽取
text3 = '请允许我尘埃落定 用沉默埋葬了过去 满身风雨我从海上来 才隐居在这沙漠里\
    该隐瞒的事总是清晰 千言万语只能无语 爱是天时地利的迷信 原来你也在这里'
s3 = SnowNLP(text3)
print(s3.keywords(limit = 5))
# 概括总结文章
print(s3.summary(limit=4))
