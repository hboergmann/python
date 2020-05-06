#LineEx2.py

from pygpanel import *

makeGPanel(0, 100, 0, 100)
     
pA = [80, 15]
pB = [10, 30]
pC = [30, 90]

line(pA, pB)
line(pA, pC)

r = 0
while r <= 1:
    pX1 = getDividingPoint(pA, pB, r)
    pX2 = getDividingPoint(pA, pC, 1 - r)
    line(pX1, pX2)
    r += 0.04
    delay(300)
keep()
