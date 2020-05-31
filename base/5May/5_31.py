"""
使用 matplotlib 进行数据绘图
pip3 install matplotlib
"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# matplotlib 命令与格式包括：画布赫尔图形 (Figure and Axis)
# 创建自定义图像
# figure(numm=None, figsize=None, dpi=Node, facecolor=None, edgecolor=None, frameon=True)
# num: 图像编号或名称，数字为编号，字符串为名称
# figsize: 指定figure的宽和高，单位为英寸
# dpi 参数指定绘图对象的分辨率，即每寸多少个像素，缺省值为 80
# facecolor: 背景颜色
# edgecolor: 边框颜色
# frameon: 是否显示边框

fig = Figure()
# 获得绘图对象
canvas = FigureCanvas(fig)
# 指定图形为线段，绘制的区域，自己调整参数观察变化
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
line, = ax.plot([0, 2], [0, 2])
# 图表标题
ax.set_title('a straight line')
# x 和 y 轴的标签
ax.set_xlabel('x label')
ax.set_ylabel('y label')
# 指定位置绘制图片
canvas.print_figure('././resources/img/chatpic1.jpg')
