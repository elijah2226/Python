# 1.奥运五环
import turtle as p

def drawCircle(x, y, c='red'):
    p.pu() # 抬笔
    p.goto(x, y)
    p.pd() # 下笔
    p.color(c)
    p.circle(30, 360)

# p = turtle
# p.pensize(3)

# drawCircle(0,0,'blue')
# drawCircle(60,0,'black')
# drawCircle(120,0,'red')
# drawCircle(90,-30,'green')
# drawCircle(30,-30,'yellow')

# p.done() # 能不立刻结束程序

# 2.漫天雪花
import random

def snow(snow_count):
    p.hideturtle()
    p.speed(500)
    p.pensize(2)
    for i in range(snow_count):
        r = random.random()
        g = random.random()
        b = random.random()
        p.pencolor(r, g, b)
        p.pu()
        p.goto(random.randint(-350, 350), random.randint(1, 270))
        p.pd()
        dens = random.randint(8, 12)
        snowsize = random.randint(10, 14)
        for _ in range(dens):
            p.forward(snowsize) # 向当前画笔方向移动snowsize像素长度
            p.backward(snowsize)
            p.right(360 / dens) # 顺时针旋转


def ground(ground_line_count):
    p.hideturtle()
    p.speed(500)
    for i in range(ground_line_count):
        p.pensize(random.randint(5, 10))
        x = random.randint(-400, 350)
        y = random.randint(-280, -1)
        r = -y/280
        g = -y/280
        b = -y/280
        p.pencolor(r, g, b)
        p.pu()
        p.goto(x, y)
        p.pd()
        p.forward(random.randint(40, 100))

def main():
    p.setup(800, 600, 0, 0)
    p.bgcolor('black')
    ground(30)
    snow(30)
    p.mainloop()

# main()

# 3.词云
import hashlib
import pandas as pd
from wordcloud import WordCloud

# engine要设置好，因为最近的read_excel不支持xlsx
# https://blog.csdn.net/weixin_44073728/article/details/111054157
geo_data = pd.read_excel(r"geo_data.xlsx", engine='openpyxl')
# print(geo_data)

words = ','.join(x for x in geo_data['city'] if x != [])

# font_path是如何找到的？
wc = WordCloud(
    background_color="green",
    max_words=100,
    font_path='simhei.ttf',
    min_font_size=5,
    max_font_size=100,
    width=500
).generate(words)

# x = wc.generate(words)
# wc.to_file('geo_data.png')

# 4.plotly画柱状图和折线图
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=[0, 1, 2, 3, 4, 5],
        y=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
    ))
fig.add_trace(
    go.Bar(
        x=[0, 1, 2, 3, 4, 5],
        y=[2, 0.5, 0.7, -1.2, 0.3, 0.4]
    ))

# fig.show()

# 5.热力图
# 导入库
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 生成数据集
data = np.random.random((6, 6)) # 返回6*6矩阵的随机数
np.fill_diagonal(data, np.ones(6)) #设置矩阵对角线的值，ones生成全是1的一维数组
features = ['prop1', 'prop2', 'prop3', 'prop4', 'prop5', 'prop6']
data = pd.DataFrame(data, index=features, columns=features)
# print(data)

# 绘制热力图
# plt如何跟热力图联系在一起？
# Seaborn 库是建立在 Matplotlib 之上的。我们可以使用 seaborn.heatmap() 函数创建 2D 热图。
# https://www.delftstack.com/zh/howto/matplotlib/how-to-plot-a-2d-heatmap-with-matplotlib/#imshow-%25E5%2587%25BD%25E6%2595%25B0%25E7%25BB%2598%25E5%2588%25B6-2d-%25E7%2583%25AD%25E5%259B%25BE
heatmap_plot = sns.heatmap(data, center=0, cmap='gist_rainbow')
# plt.show()

# 6.折线图
# 创立画图fig和axes

# import example_utils
def setup_axes():
    # figsize用来设置图形的大小，a为图形的宽， b为图形的高
    # fig代表绘图窗口(Figure)；ax代表这个绘图窗口上的坐标系(axis)，一般会继续对ax进行操作
    fig, axes = plt.subplots(ncols=3, figsize=(6, 5))
    for ax in fig.axes:
        ax.set(xticks=[], yticks=[])
    fig.subplots_adjust(wspace=0, left=0, right=0.93)
    return fig, axes

# 图片标题
def title(fig, text, y=0.9):
    fig.subtitle(text, size=14, y=y, weight='semibold', x=0.98, ha='right', bbox=dict(boxstyle='round', fc='florawhite', ec='#8B7E66', lw=2))

# 为数据添加文本注释
def label(ax, text, y=0):
    ax.annotate(text, xy=(0.5, 0.00), xycoords='axes fraction', ha='center', style='italic', bbox=dict(boxstyle='round', facecolor='floralwhite', ec='#8B7E66'))

# 上面这部分就是example_utils

# 主程序
x = np.linspace(0, 10, 100) #linspace创建一个等差序列

# 设置子图边界
fig, axes = setup_axes()
for ax in axes:
    ax.margins(y=0.10)

# 子图1,设置plot多条线，颜色系统分配
for i in range(1, 6):
    axes[0].plot(x, i*x)

# 2 展示线的不同style
for i, ls in enumerate(['-', '--', ':', '-.']):
    axes[1].plot(x, np.cos(x) + i, linestyle=ls)

# 3.展示线的不同linestyle和marker
for i, (ls, mk) in enumerate(zip(['', '-', ':'], ['o', '^', 's'])):
    axes[2].plot(x, np.cos(x) + i*x, linestyle=ls, marker=mk, markevery=10)

# fig.savefig('plot_example.png', facecolor='none')
# plt.show()
# 7.散点图
# 随机生成数据
np.random.seed(1874)
x, y, z = np.random.normal(0, 1, (3, 100)) # 第一个参数是期待，第二个是方差， 第三个是规模
# print(x, y, z)

t = np.arctan2(y, x) # 大概正切值
size = 50 * np.cos(2 * t)**2 + 10

fig, axes = setup_axes()

# 子图1
axes[0].scatter(x, y, marker='o', color='darkblue', facecolor='white', s=80)
label(axes[0], 'scatter(x, y)')

# 2
axes[1].scatter(x, y, marker='s', color='darkblue', s=size)
label(axes[1], 'scatter(x, y, s)')

# 3
axes[2].scatter(x, y, s=size, c=z, cmap='gist_ncar')
label(axes[2], 'scatter(x, y, s, c)')

fig.savefig('scatter_example.png', facecolor='none')
# plt.show()

# 8.柱状图
# 子图1
def basic_bar(ax):
    y = [1, 3, 4, 5.5, 3, 2]
    err = [0.2, 1, 2.5, 1, 1, 0.5]
    x = np.arange(len(y))
    ax.bar(x, y, yerr=err, color='lightblue', ecolor='black')
    ax.margins(0.05)
    ax.set_ylim(bottom=0)
    label(ax, 'bar(x, y, yerr=e)')

# 2
def tornado(ax):
    y = np.arange(8)
    x1 = y + np.random.random(8) + 1
    x2 = y + 3*np.random.random(8) + 1
    ax.barh(y, x1, color='lightblue')
    ax.barh(y, -x2, color='salmon')
    ax.margins(0.15)
    label(ax, "barh(x, y)")

# 3
def general(ax):
    num = 10
    left = np.random.randint(0, 10, num)
    bottom = np.random.randint(0, 10, num)
    width = np.random.random(num) + 0.5
    height = np.random.random(num) + 0.5
    ax.bar(left, height, width, bottom, color='salmon')
    ax.margins(0.15)
    label(ax, "bar(l, h, w, b)")

def main():
    fig, axes = setup_axes()

    basic_bar(axes[0])
    tornado(axes[1])
    general(axes[2])

    fig.savefig('bar_example.png', facecolor='none')
    plt.show()

# main()

# 9.等高线
from matplotlib.cbook import get_sample_data

z = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))

fig, axes = setup_axes()

# 线
axes[0].contour(z, cmap='gist_earth')
label(axes[0], 'contour')

# 面
axes[1].contourf(z, cmap='gist_earth')
label(axes[1], 'contourf')

# 线面+标记
axes[2].contourf(z, cmap='gist_earth')
cont = axes[2].contour(z, colors='black')
axes[2].clabel(cont, fontsize=6)
label(axes[2], 'contourf + contour\n + clabel')

fig.savefig('contour_example.png', facecolor='none')
# plt.show()

# 10.imshow图
from mpl_toolkits import axes_grid1

def plot(axes, img_data, scalar_data, ny):
    # 默认线性插值
    axes[0].imshow(scalar_data, cmap='gist_earth', extent=[0, ny, ny, 0])

#     最近邻插值
    axes[1].imshow(scalar_data, cmap='gist_earth', interpolation='nearest', extent=[0, ny, ny, 0])

#     展示源数据
    axes[2].imshow(img_data)

def load_data():
    img_data = plt.imread(get_sample_data('grace_hopper.png'))
    ny, nx, nbands = img_data.shape
    scalar_data = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))
    return img_data, scalar_data, ny

def setup_axes():
    fig = plt.figure(figsize=(6, 3))
    axes = axes_grid1.ImageGrid(fig, [0, 0, .93, 1], (1, 3), axes_pad=0)

    for ax in axes:
        ax.set(xticks=[], yticks=[])
    return fig, axes

def main():
    fig, axes = setup_axes()
    plot(axes, *load_data())
    fig.savefig('imshow_example.png', facecolor='none')
    plt.show()

# main()

# 11.pyecharts绘制仪表盘
from pyecharts import charts

# 仪表盘
gauge = charts.Gauge()
gauge.add('Python小李子', [('Python机器学习', 30), ('Python基础', 70.), ('Python正则', 90)])
gauge.render(path='仪表盘.html')

# 12.漏斗图
from pyecharts import options as opts
from pyecharts.charts import Funnel, Page
from random import randint

# 箭头是给函数增加参数注释
def funnel_base() -> Funnel:
    c = (
        Funnel()
        .add('豪车', [list(z) for z in zip(['宝马', '法拉利', '奔驰', '奥迪', '大众', '丰田', '特斯拉'], [randint(1, 20) for _ in range(7)])])
        .set_global_opts(title_opts=opts.TitleOpts(title="豪车漏斗图"))
    )
    return c

funnel_base().render('funnel.html')