# AnimEx4.py

from Star import Star
from gpanel import *
import time
from random import randint, random, gauss

dt = 0.01
makeGPanel(0, 100, 0, 100)
bgColor("blue")
clear()
nbStars = 50
stars = [0] * nbStars
for n in range(nbStars):
    stars[n] = Star(randint(3, 8))
for n in range(nbStars):
    stars[n].setColor(makeColor(randint(0, 255), 
            randint(0, 255),
        randint(0, 255)))
positions = [0] * nbStars
for n in range(nbStars):
    positions[n] = [randint(0, 100), randint(0, 100)]
rotIncrement = [0] * nbStars
for n in range(nbStars):
    rotIncrement[n] = (-2 + 4 * random())
enableRepaint(False)
while True:
    clear()
    positionTemp = []
    for n in range(nbStars):
        stars[n].rotate(rotIncrement[n])
        stars[n].draw(positions[n])
        if positions[n][1] < -5:
            positions[n][1] = 105
        else:    
            positions[n][1] -= 0.1
        positionTemp.append([positions[n][0], 
            positions[n][1]])
    position = positionTemp    
    repaint()
    time.sleep(dt)

