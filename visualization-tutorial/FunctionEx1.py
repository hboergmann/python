# FunctionEx1.py

from gpanel import *
from math import sin

def f(x):
    if x == 0:
        y = 1
    else:	
        y = sin(x) / x
    return y
	
makeGPanel(-12, 11, -1.8, 1.8)
drawGrid(-10, 10, -1.5, 1.5, "gray")

setColor("blue")
lineWidth(2)
x  = -10
while x < 10:
    y = f(x)
    pos(x, y) if x == -10 else draw(x, y)
    x = x + 0.01   
keep()    

