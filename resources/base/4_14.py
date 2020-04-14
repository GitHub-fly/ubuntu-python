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


jpg_number = 0
py_number = 0
other_number = 0


def deal_date(date):
    print(date)
    for item in date:
        type = item[(item.rindex('.') + 1):]
        if type == 'jpg':
            jpg_number += 1
        elif type == 'py':
            py_number += 1
        else:
            other_number += 1


def draw():
    # 准备数据
    items = ['jpg图片', 'py文件', '其它文件']
    num = [jpg_number, py_number, other_number]
    color_series = ['rgn(255, 204, 188)',
                    'rgb(255, 236, 179)', 'rgb(178, 223, 219)']
    # 实例化 Pie 类
    pie = Pie(init_opts=opts.InitOpts(width='1000px', height='800px'))
    # 设置颜色
    pie.set_colors(color_series)
    # 添加数据，设置饼图的半径，是否展示成南丁格尔玫瑰图
    pie.add(series_name="文件类型比",
            data_pair=[list(z) for z in zip(items, num)],
            radius=['20%', '30%'],
            label_opts=opts.LabelOpts(is_show=False, position='center')
            )
    # 设置全局配置项
    pie.set_global_opts(title_opts=opts.TitleOpts(title='南丁格尔玫瑰图'),
                        legend_opts=opts.LegendOpts(is_show=False),
                        toolbox_opts=opts.ToolboxOpts())
    # 设置系列配置项
    pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='inside', font_size=12,
                                                  formatter='{a} <br/>{b} : {c} ({d}%)', font_style='italic', font_weight='bold', font_family='Miscrosooft YaHei')
                        )
    pie.render('./resources/南丁格尔玫瑰图.html')


if __name__ == "__main__":
    # 取得当前目录: /home/xunmi/python-learning
    cur_path = os.getcwd()
    all = get_all(cur_path)
    deal_date(all)
    # print(jpg_number)
    draw()
