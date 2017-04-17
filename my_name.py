Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> wn = turtle.Screen()
t1 = turtle.Turtle()

SyntaxError: multiple statements found while compiling a single statement
>>> wn = turtle.Screen()
>>> t1 = turtle.Turtle()
>>> t1.shape('turtle')
>>> t1.pencolor('cold blue')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t1.pencolor('cold blue')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2252, in pencolor
    color = self._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: cold blue
>>> t1.pencolor('dark blue')
>>> t1.goto(-200,200)
>>> t1.clear
<bound method RawTurtle.clear of <turtle.Turtle object at 0x03B7F5B0>>
>>> t1.clear()
>>> t1.goto(-250,200)
>>> t1.clear()
>>> t1.circle(100)
>>> t1.clear()
>>> t1.goto(-250,1300)
>>> t1.goto(-250,130)
>>> t1.clear()
>>> t1.circle(100)
>>> t1.penup()
>>> t1.right(90)
>>> t1.fd(90)
>>> t1.lt(90)
>>> t1.pendown()
>>> t1.fd(90)
>>> t1.fd(90)
>>> t1.bk(360)
>>> t1.penup()
>>> t1.fd(70)
>>> t1.fd(20)
>>> t1.rt(90)
>>> t1.pendown()
>>> t1.fd(90)
>>> t1.fd(90)
>>> t1.lt(180)
>>> t1.fd(180)
>>> t1.rt(90)
>>> t1.fd(90)
>>> t1.fd(90)
>>> t1.rt(90)
>>> t1.fd(180)
>>> t1.penup()
>>> t1.goto(-10,240)
>>> 
>>> t1.goto(-10,270)
>>> t1.goto(-10,310)
>>> t1.pendown()
>>> t1.goto(-30,110)
>>> t1.goto(-10,310)
>>> t1.goto(40,50)
>>> t1.penup()
>>> t1.goto(50,1800)
>>> t1.goto(50,180)
>>> t1.lt(90)
>>> t1.pendown()
>>> t1.fd(120)
>>> t1.lt(90)
>>> t1.fd(120)
>>> t1.bk(250)
>>> t1.penup()
>>> t1.lt()90
SyntaxError: invalid syntax
>>> t1.lt(90)
>>> t1.fd(90)
>>> t1.lt(90)
>>> t1.lt(40)
>>> t1.rt(40)
>>> t1.fd(40)
>>> t1.circle(110)
>>> t1.circle(100)
>>> t1.fd(30)
>>> t1.rt(90)
>>> t1.fd(30)
>>> t1.circle(100)
>>> t1.pendown()
>>> t1.circle(100)
>>> t1.penup()
>>> t1.goto(240.310)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    t1.goto(240.310)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1774, in goto
    self._goto(Vec2D(*x))
TypeError: type object argument after * must be an iterable, not float
>>> t1.goto(240,310)
>>> t1.rt(180)
>>> t1.pend
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    t1.pend
AttributeError: 'Turtle' object has no attribute 'pend'
>>> t1.pendown()
>>> t1.fd(150)
>>> t1.rt(90)
>>> t1.fd(150)
>>> t1.penup()
>>> t1.t1.fd(150)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    t1.t1.fd(150)
AttributeError: 'Turtle' object has no attribute 't1'
>>> t1.fd(150)
>>> t1.bk(50)
>>> t1.rt(90)
>>> t1.pendown()
>>> t1.fd(140)
>>> t1.fd(40)
>>> t1.bk(240)
>>> t1.penup()
>>> t1.fd(140)
>>> t1.lt(90)
>>> t1.fd(240)
>>> t1.rt(90)
>>> t1.pendown
<bound method TPen.pendown of <turtle.Turtle object at 0x03B7F5B0>>
>>> t1.pendown()
>>> t1.fd(70)
>>> t1.bk(300)
>>> t1.fd(300)
>>> t1.rt(90)
>>> t1.fd(2400)
>>> t1.pencolor('white')
>>> t1.bk(2400)
>>> t1.pencolor('cold blue')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    t1.pencolor('cold blue')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2252, in pencolor
    color = self._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2696, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: cold blue
>>> t1.pencolor('dark blue')
>>> t1.fd(240)
>>> t1.rt(180)
>>> t1.pencolor('white')
>>> t1.fd(20)
>>> t1.penup()
>>> t1.pos()
(240.00,40.00)
>>> t1.rt(180)
>>> t1.fd(20)
>>> t1.pos()
(240.00,60.00)
>>> t1.dot()
>>> t1.pendown()
>>> t1.dot()
>>> t1.penup()t1.fd(240)
SyntaxError: invalid syntax
>>> t1.penup()
>>> t1.fd(240)
>>> t1.bk(240)
>>> t1.pencolor('dark blue')
>>> t1.pendown()
>>> t1.dot()
>>> t1.rt(180)
>>> t1.rt(90)
>>> t1.bk(2)
>>> t1.penup()
>>> t1.home()
>>> 
