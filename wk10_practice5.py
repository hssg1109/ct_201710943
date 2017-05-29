import turtle
wn = turtle.Screen()
t1 = turtle.Turtle()

width = wn.window_width()
w3 = (width-40)/3
x1 = 0.0 - w3
x2 = 0.0
x3 = 0.0 + w3

t1.home()
t1.clear()

def Tg(size):
    t1.right(60)
    t1.fd(size)
    t1.right(120)
    t1.fd(size)
    t1.right(120)
    t1.fd(size)
def drawTriangleAt(size,pos):
    t1.penup()
    t1.goto(pos,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    Tg(size)

def Ptg(size):
    t1.rt(36)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
def drawPentagon(size,pos):
     t1.penup()
     t1.goto(pos,0)
     t1.setheading(0)
     t1.pendown()
     t1.write(t1.pos())
     Ptg(size)

def St(size):
    t1.fd(size)
    t1.lt(216)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
def drawStarAt(size,pos):
     t1.penup()
     t1.goto(pos,0)
     t1.setheading(0)
     t1.pendown()
     t1.write(t1.pos())
     St(size)

drawTriangleAt(185,x1)
drawPentagon(185,x2)
drawStarAt(185,x3)
wn.exitonclick()


    