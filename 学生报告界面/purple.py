import os
import turtle
from time import sleep
import tkinter
from itertools import islice


def ini():
    global c, p, b
    turtle.screensize(600,800,"white")
    turtle.setup(550,760,600,0)
    turtle.ht()
    c = turtle.Turtle()   #创建画城堡的对象
    p = turtle.Turtle()   #创建放文字的对象
    b = turtle.Turtle()   #创建画海报背景和图案的对象

#抬起笔移动函数
def bsk( an, x):
    b.up()
    b.right(an)     #画笔顺时针旋转
    b.fd(x)
    b.down()

def csk( an, x):
    c.up()
    c.right(an)     #画笔顺时针旋转
    c.fd(x)
    c.down()

def drawbd():
    b.begin_fill()
    b.pensize(5)
    b.color("#cca4e3")
    b.speed(0)
    bsk(231 , 320.15)
    b.left(231.34)
    b.fd(400)
    b.right(90)
    b.fd(600)
    b.right(90)
    b.fd(400)
    b.right(90)
    b.fd(600)
    b.fillcolor("#cca4e3")
    b.end_fill()

    bsk(130,110)
    b.seth(0)
    b.color("white")
    b.width(20)
    b.fd(200)
    bsk(120,50)
    b.right(60)
    b.fd(200)

    


def home():
    b.up()
    b.home()
    b.down()

def claw(x,y):
    #脚印
    
    bsk(x,y)
    b.color("white")
    b.width(3)
    b.speed(0)
    b.begin_fill()
    b.circle(15)
    b.fillcolor("white")
    b.end_fill()

    bsk(60, 13)
    b.begin_fill()
    b.circle(5)
    b.fillcolor("white")
    b.end_fill()

    b.begin_fill()
    bsk(135, 10)
    b.circle(5)
    b.fillcolor("white")
    b.end_fill()

    b.begin_fill()
    bsk(18, 15)
    b.circle(5)
    b.fillcolor("white")
    b.end_fill()
    
    


def drawca():
    c.color("#56004f")
    c.width(3)
    c.speed(0)
    #中间部分
    csk(295, 190)
    c.seth(0)
    c.right(20)
    c.circle(50,45)
    c.seth(270)
    c.fd(60)
    c.right(70)
    c.circle(-50,45)
    c.seth(90)
    c.fd(60)

    c.seth(0)
    c.circle(-50,10)
    c.seth(270)
    c.fd(5)
    c.bk(30)
    c.seth(0)
    c.fd(20)
    c.right(90)
    c.fd(30)
    c.bk(5)
    c.seth(0)
    c.circle(-50,10)
    csk(215, 37)
    c.seth(90)
    c.right(20)
    c.fd(25)
    c.right(140)
    c.fd(25)

    #右边
    c.seth(0)
    csk(75,40)
    c.seth(0)
    c.right(5)
    c.circle(50, 25)
    c.seth(270)
    c.fd(50)
    c.seth(180)
    c.left(15)
    c.circle(-50, 25)

    c.seth(90)
    csk(0,48)
    c.right(30)
    c.fd(20)
    c.right(120)
    c.fd(20)

    #左边
    c.seth(180)
    c.up()
    c.fd(60)
    c.right(90)
    c.fd(10)
    c.left(90)
    c.down()
    c.left(10)
    c.circle(-50,25)
    c.seth(180)
    c.right(120)
    c.fd(20)
    c.right(120)
    c.fd(20)
    c.seth(270)
    c.up()
    c.fd(55)
    c.right(90)
    c.down()
    c.left(15)
    c.circle(-35,35)
    c.seth(90)
    c.fd(55)
    c.ht()

    #门
    c.width(2)
    csk(150,69)
    c.seth(90)
    c.fd(30)
    c.right(90)
    c.fd(15)
    c.right(90)
    c.fd(32)

    



def write():
    p.up()
    p.goto(-130,137)
    p.down()
    a="STUDY REPORT"
    p.color("#425066")
    p.write(a ,font=("微软雅黑", 24 ,"bold"))

    word1()

    word2()


def word1():
    p.up()
    p.goto(-170,0)
    p.down()
    p.color("#425066")
    f=open("result.txt","r", encoding="utf-8")
    f.seek(0,0)
    b = f.readline()
    print(b)
    
    p.write(b,font=("微软雅黑",20,"bold"))
    f.close()

def word2():
    p.color("black")
    p.up()
    p.goto(-170,-80)
    p.down()
    p.color("#425066")
    f=open("result.txt","r", encoding="utf-8")
    #f.seek(6,0)
    #print(f.tell())
    next(f) #跳过第一行读取内容
    c = f.readline()
    print(c)
    
    p.write(c,font=("微软雅黑",20,"bold"))
    f.close()

def pa():
    home()
    bsk(120,280)
    b.seth(0)
    b.color("yellow")
    b.width(5)
    b.left(50)
    b.circle(-30,100)
    b.circle(50,50)
    b.circle(25,100)

def main():
    turtle.tracer(False) #省略绘图过程
    ini()
    drawbd()


    home()
    claw(-10,100)
    home()
    b.seth(270)
    b.up()
    b.fd(40)
    b.down()
    b.seth(0)
    claw(20,100)
    home()
    b.seth(270)
    b.up()
    b.fd(120)
    b.down()
    b.seth(0)
    claw(40,70)


    home()
    b.seth(270)
    b.up()
    b.fd(150)
    b.seth(180)
    b.fd(70)
    b.down()
    b.seth(0)
    claw(60,90)
    drawca()
    
    
    write()

    
    turtle.mainloop()

    

if __name__=='__main__':
    main()