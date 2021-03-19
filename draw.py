# 1.奥运五环
import turtle as p

def drawCircle(x, y, c='red'):
    p.pu() # 抬笔
    p.goto(x, y)
    p.pd() # 下笔
    p.color(c)
    p.circle(30, 360)

# p = turtle
p.pensize(3)

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


snow(10)

def ground(ground_line_count):
    p.hideturtle()
    


