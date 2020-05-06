# LineEx3.py

from gpanel import *

def drawCorners():
    for x, y in corners:
        pos(x, y) 
        fillCircle(0.2)

def drawLines():
    for p in corners:
        for q in corners:
            if p != q:
                line(p, q)

makeGPanel(0, 10, 0, 10)
corners = [(2, 3), (5, 2), (8, 5), (6, 8), (3, 7)]
drawCorners()
drawLines()
keep()
