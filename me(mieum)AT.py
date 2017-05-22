import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

def gy(size): #'gy'는 기역입니다
    
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)

def ne(size): #'ne'는 니은입니다
 
    t1.rt(90)
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)

def dg(size): #'dg'는 디귿입니다
    t1.bk(size)
    ne(size)

def me(size):
    gy(size)
    t1.penup()
    t1.home()
    t1.pendown()
    ne(size)

def gyAT(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)

def meAT(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    gy(size)
    t1.penup()
    t1.goto(x,y)
    t1.rt(270)
    t1.pendown()
    ne(size)

meAT(-100,100,200)
wn.exitonclick()






