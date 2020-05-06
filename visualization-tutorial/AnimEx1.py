#AnimEx1.py

from gpanel import *
import time

makeGPanel(-6, 6, -220, 70)
setColor("red")
enableRepaint(False)

g = 9.81
dt= 0.05

t = 0; y = 0
v = 25 # Geschwindigkeit

while t < 10: 
    v = v - g * dt 
    y = y + v * dt 
    t = t + dt
    drawGrid(-5, 5, -200, 50, "gray")
    pos(0, y)  
    fillCircle(0.3)
    repaint()  
    time.sleep(dt)
    clear()   
keep()

