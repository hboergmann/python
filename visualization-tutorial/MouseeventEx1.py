# MouseeventEx1.py

from gpanel import *

def onMousePressed(x, y):
    setColor("green")
    pos(x, y) 
    fillCircle(0.02) 

def onMouseDragged(x, y):
    setColor("red") 
    pos(x, y)
    setColor("red")
    fillCircle(.04) 
    setColor("black")
    circle(.04)  

makeGPanel(mousePressed = onMousePressed, mouseDragged = onMouseDragged)

keep()
