#ShapesEx2.py

from gpanel import *
from random import randint

makeGPanel(0, 100, 0, 100)

for i in range(80):
    pos(randint(0, 100), randint(0, 100))
    setColor(makeColor(randint(0, 255), randint(0, 255), randint(0, 255)))
    fillRectangle(randint(10, 30), randint(5, 30)) 
keep()    
