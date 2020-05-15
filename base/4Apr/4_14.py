"""
查看当前目录所有文件
"""

import os
from pyecharts.charts import Pie
from pyecharts import options as opts

result = []


def get_all(cwd):
    # 遍历当前目录，获取文件列表
    get_dir = os.listdir(cwd)
    # print(get_dir)
    for i in get_dir:
        # 把第一步获取的文件加入路径，例如：os.path.join('root','test','runoob.txt') -> root/test/runoob.txt
        sub_dir = os.path.join(cwd, i)
        # print(sub_dir)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件名放入列表
            file_name = os.path.basename(sub_dir)
            result.append(file_name)

    return result


def deal_date(date):
    jpg_number = 0
    py_number = 0
    other_number = 0
    for item in date:
        type = item[(item.rindex('.') + 1):]
        if type == 'jpg':
            jpg_number += 1
        elif type == 'py':
            py_number += 1
        else:
            other_number += 1
    return [jpg_number, py_number, other_number]


def draw():
    # 取得当前目录: /home/xunmi/python-learning
    cur_path = os.getcwd() + '/resources'
    date = deal_date(get_all(cur_path))
    # 准备数据
    items = ['jpg图片', 'py文件', '其它文件']
    num = [date[0], date[1], date[2]]
    color_series = ['rgb(255, 87, 34)',
                    'rgb(76, 175, 80)', 'rgb(103, 58, 183)']
    # 实例化 Pie 类
    pie = Pie(init_opts=opts.InitOpts(width='1000px', height='800px'))
    # 设置颜色
    pie.set_colors(color_series)
    # 添加数据，设置饼图的半径，是否展示成南丁格尔玫瑰图
    pie.add(series_name="",
            data_pair=[list(z) for z in zip(items, num)],
            radius=['10%', '30%'],
            label_opts=opts.LabelOpts(is_show=False, position='center')
            )
    # 设置全局配置项
    pie.set_global_opts(title_opts=opts.TitleOpts(title='文件类型占比'),
                        legend_opts=opts.LegendOpts(
                            is_show=False, orient='vertical', pos_top='15%', pos_left='2%'),
                        toolbox_opts=opts.ToolboxOpts())
    # 设置系列配置项
    pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
                                                  formatter='{b} : {c}')
                        )
    pie.render('./resources/文件类型占比分析图.html')


if __name__ == "__main__":
    draw()
