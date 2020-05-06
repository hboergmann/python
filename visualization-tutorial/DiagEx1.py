#DiagEx1.py

from gpanel import *
from random import random

n = 1000

makeGPanel(-2, 10, -0.1 * n / 2, 1.1 * n / 2)
drawGrid(-1, 9, 0, n // 2, 10, 10)
setColor("red")

histo = [0] * 8 

for i in range(n):
    nbErrors = 0
    for k in range(8):
        if random() < 0.1:
            nbErrors += 1
    histo[nbErrors] += 1

lineWidth(5)
for i in range(0, 8):
    if histo[i] != 0:
        fillRectangle(i - 1/3, 0, i + 1/3, histo[i])
print "W'keit, höchstens 2 Zeichen falsch =",(histo[0] + histo[1] + histo[2])/n
keep()    
