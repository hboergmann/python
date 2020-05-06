#AnimEx3.py

from gpanel import *
from random import randint
import time

def drawSky():    
    for (x, y) in sky:     
        pos(x, y)
        fillCircle(5)
                                
makeGPanel(0, 600, 0, 600)
bgColor("darkblue")
setColor("white") 
sky = []
dt = 0.06
enableRepaint(False)

for i in range(100):
    x = randint (5, 595)
    y = randint (0, 600)  
    sky.append((x, y))
    
while True:
    clear()
    drawSky()
    repaint()
    skyTemp = []     
    for (x, y) in sky:
        if y < -20:
            y = 620
        else:    
            y -= 1
        skyTemp.append((x, y))
    sky = skyTemp    
    time.sleep(dt)


