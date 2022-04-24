import os
import turtle


import tkinter
from itertools import islice


def ini():
    global r, p, b
    turtle.screensize(600, 800, "white")
    turtle.setup(550, 760, 600, 0)
    turtle.ht()
    r = turtle.Turtle()   #创建画人的对象
    p = turtle.Turtle()   #创建放文字的对象
    b = turtle.Turtle()   #创建画海报背景和图案的对象

#抬起笔移动函数
def bsk( an, x):
    b.up()
    b.right(an)     #画笔顺时针旋转
    b.fd(x)
    b.down()

def rsk( an, x):
    r.up()
    r.right(an)     #画笔顺时针旋转
    r.fd(x)
    r.down()

def drawbd():
    b.begin_fill()
    b.pensize(5)
    b.color("#e3f9fd")
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
    b.fillcolor("#e3f9fd")
    b.end_fill()

    #白色竖线
    b.right(90)
    b.fd(133.33)
    b.color("white")
    b.width(20)
    b.right(90)
    b.fd(600)
    b.up()
    b.left(90)
    b.fd(133.33)
    b.left(90)
    b.down()
    b.fd(600)

    #白色横线
    b.up()
    b.right(90)
    b.fd(134)
    b.right(90)
    b.fd(100)
    b.right(90)
    b.down()
    b.fd(430)
    b.left(90)
    b.fd(100)
    b.left(90)
    b.fd(430)
    b.right(90)
    b.fd(100)
    b.right(90)
    b.fd(430)
    b.left(90)
    b.fd(100)
    b.left(90)
    b.fd(430)
    b.right(90)
    b.fd(100)
    b.right(90)
    b.fd(420)
    
def drawren():
    r.ht()
    r.speed(0)
    rsk(75,150)
    r.width(3)
    r.color("black")
   

    #头发
    r.seth(90)
    r.circle(-15,185)
    r.circle(-2,180)
    r.circle(-20,190)
    r.seth(90)
    r.circle(-40,30)
    r.circle(-12,170)
    r.circle(-40,20)
    r.circle(-2,190)
    r.circle(-20,170)
    r.circle(30,10)

    r.seth(0)
    r.left(40)
    r.circle(-13,180)
    r.circle(-40,75)
    r.circle(-4,310)
    r.circle(-80,30)
    r.circle(-10,150)
    r.circle(-2,130)
    r.circle(-25,180)
    r.circle(-50,10)


    #脸
   
    r.seth(270)
    rsk(-5,40)
    r.circle(90,40)
    r.circle(30,30)
    r.circle(80.30)
    r.circle(30,30)
    r.circle(70,55)

    
    r.seth(180)
    rsk(0,70)
    r.begin_fill()
    r.circle(-2)
    r.fillcolor("black")
    r.end_fill()

    r.seth(0)
    rsk(6,40)
    r.begin_fill()
    r.circle(2)
    r.fillcolor("black")
    r.end_fill()

    r.seth(0)
    rsk(55,11)
    r.color("#ffb3a7")
    r.begin_fill()
    r.circle(-6)
    r.fillcolor("#ffb3a7")
    r.end_fill()

    rsk(120, 55)
    r.begin_fill()
    r.circle(-6)
    r.fillcolor("#ffb3a7")
    r.end_fill()

    #身体
    r.speed(0)
    r.color("black")
    r.width(3)
    r.seth(270)
    rsk(0,20)
    r.right(40)
    r.circle(70,60)

    r.up()
    r.seth(0)
    r.left(43)
    r.fd(90)
    r.down()
    r.seth(270)
    r.left(20)
    r.circle(-90,30)

    #书
    r.speed(0)
    r.up()
    r.seth(270)
    rsk(90,30)
    r.down()
    r.seth(0)
    r.left(25)
    r.circle(-50,60)


    r.seth(0)
    r.right(30)
    r.fd(25)
    r.seth(180)
    r.right(25)
    r.circle(50,60)

   

    r.seth(180)
    r.right(25)
    r.circle(55,65)

    r.seth(0)
    r.left(120)
    r.fd(25)

    r.seth(0)
    r.left(25)
    r.circle(-80,40)

    r.right(20)
    r.fd(20)














    

def write():
    p.up()
    p.goto(-180,200)
    p.down()
    a="Hello kid~This is your study report !"
    p.write(a ,font=("Ink free", 16 ,"bold"))

    word1()

    word2()

    word3()


def word1():
    p.up()
    p.goto(-180,50)
    p.down()
    p.color("black")
    f=open("result.txt","r", encoding="utf-8")
    f.seek(0,0)
    b = f.readline()
    print(b)
    p.write(b,font=("微软雅黑",20,"bold"))
    f.close()

def word2():
    p.color("black")
    p.up()
    p.goto(-180,-50)
    p.down()
    f=open("result.txt","r", encoding="utf-8")
 
    next(f) #跳过第一行读取内容
    c = f.readline()
    print(c)
    p.write(c,font=("微软雅黑",20,"bold"))
    f.close()

def word3():
    p.color("black")
    p.up()
    p.goto(-180,-100)
    p.down()
    p.color("black")
    f=open("result.txt","r", encoding="utf-8")
    #f.seek(6,0)
    #print(f.tell())
    next(f) #跳过第一行读取内容
    next(f)
    c = f.readline()
    print(c)
    p.write(c,font=("微软雅黑",20,"bold"))
    f.close()



def main():
    turtle.tracer(False)  # 省略绘图过程
    ini()
    drawbd()
    drawren()
    write()
    turtle.mainloop()




if __name__=='__main__':
    main()
