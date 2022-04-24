import os
import turtle
import random






def rand():
    global a 
    a= random.choice([1,2])
    print(a)
    if a == 1:
        blue_main()
    else:
        purple_main()







def blue_ini():
    global blue_r, blue_p, blue_b
    blue_r = turtle.Turtle()   #创建画人的对象
    blue_p = turtle.Turtle()   #创建放文字的对象
    blue_b = turtle.Turtle()   #创建画海报背景和图案的对象

def blue_bsk( an, x):
    blue_b.up()
    blue_b.right(an)     #画笔顺时针旋转
    blue_b.fd(x)
    blue_b.down()

def blue_rsk( an, x):
    blue_r.up()
    blue_r.right(an)     #画笔顺时针旋转
    blue_r.fd(x)
    blue_r.down()




def blue_drawbd():
    turtle.tracer(False)
    blue_b.begin_fill()
    blue_b.pensize(5)
    blue_b.color("#e3f9fd")
    blue_b.speed(0)
    blue_bsk(231 , 320.15)
    blue_b.left(231.34)
    blue_b.fd(400)
    blue_b.right(90)
    blue_b.fd(600)
    blue_b.right(90)
    blue_b.fd(400)
    blue_b.right(90)
    blue_b.fd(600)
    blue_b.fillcolor("#e3f9fd")
    blue_b.end_fill()

    #白色竖线
    blue_b.right(90)
    blue_b.fd(133.33)
    blue_b.color("white")
    blue_b.width(20)
    blue_b.right(90)
    blue_b.fd(600)
    blue_b.up()
    blue_b.left(90)
    blue_b.fd(133.33)
    blue_b.left(90)
    blue_b.down()
    blue_b.fd(600)

    #白色横线
    blue_b.up()
    blue_b.right(90)
    blue_b.fd(134)
    blue_b.right(90)
    blue_b.fd(100)
    blue_b.right(90)
    blue_b.down()
    blue_b.fd(430)
    blue_b.left(90)
    blue_b.fd(100)
    blue_b.left(90)
    blue_b.fd(430)
    blue_b.right(90)
    blue_b.fd(100)
    blue_b.right(90)
    blue_b.fd(430)
    blue_b.left(90)
    blue_b.fd(100)
    blue_b.left(90)
    blue_b.fd(430)
    blue_b.right(90)
    blue_b.fd(100)
    blue_b.right(90)
    blue_b.fd(420)



def blue_drawren():
    blue_r.ht()
    turtle.tracer(True,0)
    blue_rsk(75,150)
    blue_r.width(3)
    blue_r.color("black")
   

    #头发
    blue_r.seth(90)
    blue_r.circle(-15,185)
    blue_r.circle(-2,180)
    blue_r.circle(-20,190)
    blue_r.seth(90)
    blue_r.circle(-40,30)
    blue_r.circle(-12,170)
    blue_r.circle(-40,20)
    blue_r.circle(-2,190)
    blue_r.circle(-20,170)
    blue_r.circle(30,10)
    
    blue_r.seth(0)
    blue_r.left(40)
    blue_r.circle(-13,180)
    blue_r.circle(-40,75)
    blue_r.circle(-4,310)
    blue_r.circle(-80,30)
    blue_r.circle(-10,150)
    blue_r.circle(-2,130)
    blue_r.circle(-25,180)
    blue_r.circle(-50,10)


    #脸
   
    blue_r.seth(270)
    blue_rsk(-5,40)
    blue_r.circle(90,40)
    blue_r.circle(30,30)
    blue_r.circle(80.30)
    blue_r.circle(30,30)
    blue_r.circle(70,55)

    
    blue_r.seth(180)
    blue_rsk(0,70)
    blue_r.begin_fill()
    blue_r.circle(-2)
    blue_r.fillcolor("black")
    blue_r.end_fill()

    blue_r.seth(0)
    blue_rsk(6,40)
    blue_r.begin_fill()
    blue_r.circle(2)
    blue_r.fillcolor("black")
    blue_r.end_fill()

    blue_r.seth(0)
    blue_rsk(55,11)
    blue_r.color("#ffb3a7")
    blue_r.begin_fill()
    blue_r.circle(-6)
    blue_r.fillcolor("#ffb3a7")
    blue_r.end_fill()
    
    blue_rsk(120, 55)
    blue_r.begin_fill()
    blue_r.circle(-6)
    blue_r.fillcolor("#ffb3a7")
    blue_r.end_fill()

    #身体
    blue_r.speed(0)
    blue_r.color("black")
    blue_r.width(3)
    blue_r.seth(270)
    blue_rsk(0,20)
    blue_r.right(40)
    blue_r.circle(70,60)

    blue_r.up()
    blue_r.seth(0)
    blue_r.left(43)
    blue_r.fd(90)
    blue_r.down()
    blue_r.seth(270)
    blue_r.left(20)
    blue_r.circle(-90,30)

    #书
    
    blue_r.up()
    blue_r.seth(270)
    blue_rsk(90,30)
    blue_r.down()
    blue_r.seth(0)
    blue_r.left(25)
    blue_r.circle(-50,60)


    blue_r.seth(0)
    blue_r.right(30)
    blue_r.fd(25)
    blue_r.seth(180)
    blue_r.right(25)
    blue_r.circle(50,60)

   

    blue_r.seth(180)
    blue_r.right(25)
    blue_r.circle(55,65)

    blue_r.seth(0)
    blue_r.left(120)
    blue_r.fd(25)

    blue_r.seth(0)
    blue_r.left(25)
    blue_r.circle(-80,40)

    blue_r.right(20)
    blue_r.fd(20)



def blue_write():
    blue_p.up()
    blue_p.goto(-130,180)
    blue_p.down()
    ab="STUDY REPORT"
    blue_p.color("#225670")
    blue_p.write(ab ,font=("微软雅黑", 24 ,"bold"))

    letterpaiban()


def blue_main():
    blue_ini()
    turtle.tracer(False)
    blue_drawbd()
    blue_drawren()
    blue_write()
   






def purple_ini():
    global purple_c, purple_p, purple_b
    purple_c = turtle.Turtle()   #创建画城堡的对象
    purple_p = turtle.Turtle()   #创建放文字的对象
    purple_b = turtle.Turtle()



def purple_bsk( an, x):
    purple_b.up()
    purple_b.right(an)     #画笔顺时针旋转
    purple_b.fd(x)
    purple_b.down()




def purple_csk( an, x):
    purple_c.up()
    purple_c.right(an)     #画笔顺时针旋转
    purple_c.fd(x)
    purple_c.down()




def purple_drawbd():
    turtle.tracer(False)
    purple_b.begin_fill()
    purple_b.pensize(5)
    purple_b.color("#cca4e3")
    purple_b.speed(0)
    purple_bsk(231 , 320.15)
    purple_b.left(231.34)
    purple_b.fd(400)
    purple_b.right(90)
    purple_b.fd(600)
    purple_b.right(90)
    purple_b.fd(400)
    purple_b.right(90)
    purple_b.fd(600)
    purple_b.fillcolor("#cca4e3")
    purple_b.end_fill()

    purple_bsk(130,110)
    purple_b.seth(0)
    purple_b.color("white")
    purple_b.width(20)
    purple_b.fd(200)
    purple_bsk(120,50)
    purple_b.right(60)
    purple_b.fd(200)





def purple_home():
    purple_b.up()
    purple_b.home()
    purple_b.down()





def purple_claw(x,y):
    #脚印
    
    purple_bsk(x,y)
    purple_b.color("white")
    purple_b.width(3)
    purple_b.speed(0)
    purple_b.begin_fill()
    purple_b.circle(15)
    purple_b.fillcolor("white")
    purple_b.end_fill()

    purple_bsk(60, 13)
    purple_b.begin_fill()
    purple_b.circle(5)
    purple_b.fillcolor("white")
    purple_b.end_fill()

    purple_b.begin_fill()
    purple_bsk(135, 10)
    purple_b.circle(5)
    purple_b.fillcolor("white")
    purple_b.end_fill()

    purple_b.begin_fill()
    purple_bsk(18, 15)
    purple_b.circle(5)
    purple_b.fillcolor("white")
    purple_b.end_fill()




def purple_drawca():
    purple_c.color("#8d4bbb")
    purple_c.width(3)
    purple_c.speed(0)
    #中间部分
    purple_csk(295, 190)
    purple_c.seth(0)
    purple_c.right(20)
    purple_c.circle(50,45)
    purple_c.seth(270)
    purple_c.fd(60)
    purple_c.right(70)
    purple_c.circle(-50,45)
    purple_c.seth(90)
    purple_c.fd(60)

    purple_c.seth(0)
    purple_c.circle(-50,10)
    purple_c.seth(270)
    purple_c.fd(5)
    purple_c.bk(30)
    purple_c.seth(0)
    purple_c.fd(20)
    purple_c.right(90)
    purple_c.fd(30)
    purple_c.bk(5)
    purple_c.seth(0)
    purple_c.circle(-50,10)
    purple_csk(215, 37)
    purple_c.seth(90)
    purple_c.right(20)
    purple_c.fd(25)
    purple_c.right(140)
    purple_c.fd(25)

    #右边
    purple_c.seth(0)
    purple_csk(75,40)
    purple_c.seth(0)
    purple_c.right(5)
    purple_c.circle(50, 25)
    purple_c.seth(270)
    purple_c.fd(50)
    purple_c.seth(180)
    purple_c.left(15)
    purple_c.circle(-50, 25)

    purple_c.seth(90)
    purple_csk(0,48)
    purple_c.right(30)
    purple_c.fd(20)
    purple_c.right(120)
    purple_c.fd(20)

    #左边
    purple_c.seth(180)
    purple_c.up()
    purple_c.fd(60)
    purple_c.right(90)
    purple_c.fd(10)
    purple_c.left(90)
    purple_c.down()
    purple_c.left(10)
    purple_c.circle(-50,25)
    purple_c.seth(180)
    purple_c.right(120)
    purple_c.fd(20)
    purple_c.right(120)
    purple_c.fd(20)
    purple_c.seth(270)
    purple_c.up()
    purple_c.fd(55)
    purple_c.right(90)
    purple_c.down()
    purple_c.left(15)
    purple_c.circle(-35,35)
    purple_c.seth(90)
    purple_c.fd(55)
    purple_c.ht()

    #门
    turtle.tracer(True)
    purple_c.width(2)
    purple_csk(150,69)
    purple_c.seth(90)
    purple_c.fd(30)
    purple_c.right(90)
    purple_c.fd(15)
    purple_c.right(90)
    purple_c.fd(32)


def purple_write():
    purple_p.up()
    purple_p.goto(-130,137)
    purple_p.down()
    a="STUDY REPORT"
    purple_p.color("#392f41")
    purple_p.write(a ,font=("微软雅黑", 24 ,"bold"))

    letterpaiban()





def purple_main():
    purple_ini()
    purple_drawbd()


    purple_home()
    purple_claw(-10,100)
    purple_home()
    purple_b.seth(270)
    purple_b.up()
    purple_b.fd(40)
    purple_b.down()
    purple_b.seth(0)
    purple_claw(20,100)
    purple_home()
    purple_b.seth(270)
    purple_b.up()
    purple_b.fd(120)
    purple_b.down()
    purple_b.seth(0)
    purple_claw(40,70)


    purple_home()
    purple_b.seth(270)
    purple_b.up()
    purple_b.fd(150)
    purple_b.seth(180)
    purple_b.fd(70)
    purple_b.down()
    purple_b.seth(0)
    purple_claw(60,90)
    purple_drawca()
    
    
    purple_write()

    


def letterpaiban():
    turtle.tracer(False)
    pen=turtle.Turtle()
    turtle.ht()
    f=open("result.txt", "r", encoding="utf-8" )
    pen.color("black")
   
    aa=f.readline()
    print(aa)
    if len(aa)==0 :
        pen.up()
        pen.goto(-166,0)
        pen.down()
        nice="真棒 认真的你可以放松一下啦"
        pen.write(nice, font=("楷体",18,'bold'))
    else :
        
        if a==1:
            d1=60
            pen.color("#225670")
            pen.up()
            pen.goto(-170,140)
            no="以下知识点还没掌握哟"
            pen.write(no, font=("楷体",15,'bold'))
            f.seek(0,0)
            next(f)
            next(f)
            for i in range(20):
                b=f.readline()
                pen.up()
                pen.goto(-130, d1)
                pen.down()
                d1-=50
                pen.write(b,font=("楷体",15,'bold'))
        else:
            d2= 20
            pen.color("#392f41")
            pen.up()
            pen.goto(-150,100)
            no="以下知识点还没掌握哟"
            pen.write(no, font=("楷体",15,'bold'))
            f.seek(0,0)
            next(f)
            next(f)
            for i in range(20):
                b=f.readline()
                pen.up()
                pen.goto(-130, d2)
                pen.down()
                d2-=50
                pen.write(b,font=("楷体",15,'bold'))
    f.close()


    
def realmain():

    turtle.screensize(600,800,"white")
    turtle.setup(600,800,200,80)
    turtle.ht()
    rand()
    turtle.mainloop()


if __name__=='__main__':
    realmain()
    




    