# Mandelbrot2.py

from gpanel import *
import thread

def getIterationColor(it):
    return (30 * it) % 256, (4 * it) % 256, (255 - (30 * it)) % 256

def mandelbrot(c):
    z = 0
    for it in range(maxIterations):
        z = z*z + c
        if abs(z) > R: # diverging
            return it
    return maxIterations

def drawFractal(xmin, xmax, ymin, ymax):
    global enableZoom
    title("Mandelbrot Set. Drawing...please wait.")
    enableZoom = False
    xstep = (xmax - xmin) / 1000.0
    ystep = (ymax - ymin) / 1000.0
    clear()
    window(xmin, xmax, ymin, ymax)
    y = ymin
    while y <= ymax:
        x = xmin
        while x <= xmax:
            try:
                c = x + y*1j
                itCount = mandelbrot(c)
                if itCount == maxIterations: # inside Mandelbrot set
                    setColor("yellow")
                else: # outside Mandelbrot set
                   r, g, b = getIterationColor(itCount)
                   setColor(r, g, b)
                point(c)
                x += xstep
            except:  # Frame disposed
                return 
        y += ystep
        repaint()
    enableZoom = True
    title("Mandelbrot Set. Ready for Zooming.")

def onMousePressed(x,y):
    global x1, y1, x2, y2
    if not enableZoom:
        return
    setColor("white")
    lineWidth(3)
    setXORMode("blue") # set XOR paint mode
    x1 = x2 = x
    y1 = y2 = y

def onMouseDragged(x, y):
    global x2, y2
    if not enableZoom:
        return
    rectangle(x1, y1, x2, y2) # erase old
    x2 = x
    y2 = y
    rectangle(x1, y1, x2, y2) # draw new
    repaint()

def onMouseReleased(x, y):
    if not enableZoom:
        return
    rectangle(x1, y1, x2, y2) # erase old
    setPaintMode() # establish normal paint mode
    repaint()
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    thread.start_new_thread(drawFractal, (xmin, xmax, ymin, ymax))

x1 = y1 = 0
x2 = y2 = 0
maxIterations = 50
R = 2
xmin = -2
xmax = 1
ymin = -1.5
ymax = 1.5

makeGPanel(mousePressed = onMousePressed, 
    mouseDragged = onMouseDragged, 
    mouseReleased = onMouseReleased)
title("Mandelbrot Set")
enableRepaint(False)
enableZoom = False
thread.start_new_thread(drawFractal, (xmin, xmax, ymin, ymax))
keep()
