# SimEx2.py

from gpanel import *
import time


g = 9.81
dt = 0.1 

makeGPanel(-1, 11, -220, 70)
drawGrid(0, 10, -200, 50, "gray")
setColor("red")
lineWidth(2)

t = 0; y = 0; v = 20
pos(t, y)
while t < 10:
	draw(t, y)
	v = v - g * dt
	y = y + v * dt	
	t = t + dt
	time.sleep(dt)
keep()	

