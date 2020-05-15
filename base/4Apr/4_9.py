"""
python 数据分组练习
"""

from itertools import groupby


def group():

    weather = [
        {
            'data': '2019-12-15', 'weather': 'clound'
        },
        {
            'data': '2019-12-13', 'weather': 'sunny'
        },
        {
            'data': '2019-12-14', 'weather': 'clound'
        },
    ]

    # 分组前没有按照分组字段排序，分组失败
    for k, items in groupby(weather, key=lambda x: x['weather']):
        print(k)
        for i in items:
            print(i)
    print('*************************************')

    # 分组前按照分组字段排序，分组成功
    weather.sort(key=lambda x: x['weather'])
    for k, items in groupby(weather, key=lambda x: x['weather']):
        print(k)
        for i in items:
            print(i)

# pyecharts 绘制柱状图示例


def draw():
    from pyecharts.charts import Bar
    from pyecharts import options as opts
    from pyecharts.globals import ThemeType
    # 内置主题类型可查看 pyecharts.globals.ThemeType
    # 有 LIGHT DARK WHITE CHALK ESSOS INFOGRAPHIC
    # MACARONS PURPLE_PASSION FOMA ROMANTIC SHINE
    # VINTAGE WALDEN WESTEROS WONDERLAND 等十余种

    # 第一幅图，数据固定
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(['服饰', '箱包', '鞋帽', '电子', '数码', '户外'])
        .add_yaxis('京东', [5, 20, 36, 10, 75, 90])
        .add_yaxis('天猫', [15, 6, 45, 20, 35, 66])
        .set_global_opts(title_opts=opts.TitleOpts(title='电商销售对比'))
    )
    bar.render(path='./resources/电商销售对比.html')

    # 第二幅图，数据分离
    items = ['Java', 'C', 'Python', 'C++', 'JavaScript', 'C#', 'PHP', 'SQL']
    data_list1 = [188, 166, 110, 108, 90, 80, 55, 45]
    data_list2 = [190, 160, 140, 100, 80, 70, 50, 40]
    bar1 = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(items)
        .add_yaxis('2020年', data_list1)
        .add_yaxis('2019年', data_list2)
        .set_global_opts(title_opts=opts.TitleOpts(title='编程语言排行', subtitle='2019-2020'))
    )
    bar1.render(path='./resources/编程语言排行.html')


if __name__ == "__main__":
    group()
    draw()
