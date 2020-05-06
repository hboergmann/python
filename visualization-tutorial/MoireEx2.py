# MoireEx2.py

from pygpanel import *

makeGPanel(0, 200, 0, 200)

for i in range(200):
	line(0, i, 200,100)
	delay(100)

for i in range(200):
	line(i, 0, 100,200)
	delay(100)
keep()




