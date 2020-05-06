#AnimEx3.py

from gpanel import *
from random import randint

def drawSky():    
    for (x, y) in sky:     
        move(x, y)
        image(img, x, y)  
                                
makeGPanel(0, 600, 0, 600) 
bgColor("deepskyblue") 
sky = []
img = getImage("sprites/alien.png")  
enableRepaint(False)

for i in range(30):
    x = randint (10, 590)
    y = randint (-20, 620)  
    sky.append((x, y))
    
while True:
    clear()
    drawSky()
    repaint()
    skyTemp = []
    for (x, y) in sky:
        if y < -40:
            y = 620
        else:    
            y -= 1
        skyTemp.append((x, y))
    sky = skyTemp    
    delay(25)

