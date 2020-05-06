# FunctionEx3.py

from gpanel import *
from math import exp, sin, pi

def f(x):
    y = a * exp(-k * x) * sin(omega * x + fi) 
    return y
   
makeGPanel(-10, 110, -7, 7)
drawGrid(0, 100, -6, 6, "gray")

setColor("blue")
lineWidth(2)
x  = 0
a = 5
k = 0.04
omega = 0.6
fi = pi/2
dx = 0.1
while x < 100:
    y = f(x)
    pos(x, y) if x == 0 else draw(x, y)
    x = x + dx 
keep() 
