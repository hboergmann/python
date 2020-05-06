#SimEx1.py

from gpanel import *
import random
import thread

NB_DROPS = 10000

def onMousePressed(x, y):
    if isLeftMouseButton():
        pt = [x, y]
        move(pt)
        circle(0.5)
        corners.append(pt)
    if isRightMouseButton():
        thread.start_new_thread(go,())

def go():
    global nbHit
    setColor("gray")
    fillPolygon(corners)
    title("Working. Please wait...")
    for i in range(NB_DROPS):
        x = 100 * random.random()
        y = 100 * random.random()
        color = getPixelColorStr(x, y)
        if color == "black":
            setColor("green")
            point(x, y)
        if color == "gray" or color == "red":
            nbHit += 1
            setColor("red")
            point(x, y)
    title("All done. #hits: " + str(nbHit) + " of " + str(NB_DROPS))

makeGPanel(0, 100, 0, 100, mousePressed = onMousePressed)
title("Select corners with left button. Start dropping with right button")
bgColor("black")
setColor("gray")
corners = []
nbHit = 0
keep()
