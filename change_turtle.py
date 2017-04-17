Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.screen()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    turtle.screen()
AttributeError: module 'turtle' has no attribute 'screen'
>>> turtle.Screen()
<turtle._Screen object at 0x0328F1D0>
>>> wn = turtle.Screen()
>>> t1 = turtle.Turtle()
>>> t1.shape(C:\\Users\\400T6B\\Pictures\\momoc.jpg)
SyntaxError: invalid syntax
>>> t1.shape(C:\Users\\400T6B\\Pictures\\momoc.jpg)
SyntaxError: invalid syntax
>>> t1.shape(C:\\Users\\400T6B\\Pictures\\momoc.gif)
SyntaxError: invalid syntax
>>> t1.shape('C:\\Users\\400T6B\\Pictures\\momoc.gif')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\Pictures\\momoc.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\Pictures\momoc.gif
>>> t1.shape('C:\\Users\\400T6B\\Pictures\\momoc.gif')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\Pictures\\momoc.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\Pictures\momoc.gif
>>> t1.shape('C:\\Users\\400T6B\\Pictures\\3,523momoc.gif')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t1.shape('C:\\Users\\400T6B\\Pictures\\3,523momoc.gif')
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\Pictures\3,523momoc.gif
>>> t1.shape("C:\\Users\\400T6B\\Pictures\\3,523 momoc.gif")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t1.shape("C:\\Users\\400T6B\\Pictures\\3,523 momoc.gif")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 2776, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named C:\Users\400T6B\Pictures\3,523 momoc.gif
>>> wn.addshape("C:\\Users\\400T6B\\Pictures\\3,523 momoc.gif")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    wn.addshape("C:\\Users\\400T6B\\Pictures\\3,523 momoc.gif")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1133, in register_shape
    shape = Shape("image", self._image(name))
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 479, in _image
    return TK.PhotoImage(file=filename)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3539, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3495, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "C:\Users\400T6B\Pictures\3,523 momoc.gif": no such file or directory
>>> >>> wn.addshape("C:\\Users\\400T6B\\Pictures\\momoc.gif")
SyntaxError: invalid syntax
>>> 
>>> wn.addshape("C:\\Users\\400T6B\\Pictures\\momoc.gif")
>>> t1.shape("C:\\Users\\400T6B\\Pictures\\momoc.gif")
>>> 
