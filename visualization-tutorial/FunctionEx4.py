# FunctionEx4.py

from gpanel import *
from math import sin, cos, pi

def cardiode(fi):
    x = a * cos(fi) * (1 + cos(fi))
    y = a * sin(fi) * (1 + cos(fi))
    return x, y

makeGPanel(-3, 13, -10, 10)
drawGrid(-1, 11, -8, 8, "gray")

setColor("blue")
lineWidth(2)
a = 5
fi = 0
dfi = 0.1
x = 0
while fi < 2 * pi + dfi:
    x, y = cardiode(fi)
    pos(x, y) if fi == 0 else draw(x, y)
    fi = fi + dfi    
keep() 
