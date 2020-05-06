# MouseeventsEx3.py

from gpanel import *
from math import cos, exp, pi
import thread

def f(x):
    y = a * exp(-5 *x) * cos(2 * pi * f1 * x)
    return y
   
def drawGraph(xmin, xmax, ymin, ymax):
    clear()
    setColor("black")
    lineWidth(1)
    xspan = xmax - xmin
    yspan = ymax - ymin
    dx = xspan / 1000.0
    window(xmin - 0.1 * xspan, xmax + 0.1 * xspan, ymin - 0.1 * yspan, ymax + 0.1 * yspan)
    drawGrid(1.0 * xmin, xmax, 1.0 * ymin, ymax, "gray")
    x = xmin
    while x <= xmax:
        y = f(x)
        pos(x, y) if x == xmin else draw(x, y)
        x += dx

def onMousePressed(x, y):
    global x1, y1, x2, y2
    setColor("white")
    lineWidth(2)
    setXORMode("blue") # set XOR paint mode
    x1 = x2 = x
    y1 = y2 = y

def onMouseDragged(x, y):
    global x2, y2
    rectangle(x1, y1, x2, y2) # erase old
    x2 = x
    y2 = y
    rectangle(x1, y1, x2, y2) # draw new
    repaint()

def onMouseReleased(x, y):
    rectangle(x1, y1, x2, y2) # erase old
    setPaintMode() # establish normal paint mode
    repaint()
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    thread.start_new_thread(drawGraph, (xmin, xmax, ymin, ymax))

a = 1
f1 = 100
makeGPanel(mousePressed = onMousePressed,
    mouseDragged = onMouseDragged,
    mouseReleased = onMouseReleased)
drawGraph(0, 1, -2, 2)
keep() 
