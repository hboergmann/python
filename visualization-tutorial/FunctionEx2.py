# FunctionEx2.py

from gpanel import *

def f(x):    
    y = 2 / x     
    return y
   
makeGPanel(-12, 12, -11, 11)
drawGrid(-10, 10, -10, 10, "gray")
setColor("blue")
lineWidth(2)
dx = 0.1

x  = -10.0
while x < -0.1:
    y = f(x)
    pos(x, y) if x == -10.0 else draw(x, y)
    x = x + dx 

x = 0.1
while x < 10:
    y = f(x)
    pos(x, y) if x == 0.1 else draw(x, y)
    x = x + dx     
keep() 


