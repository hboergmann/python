#AminEx2.py

from gpanel import *
import math

makeGPanel(Size(800, 400))
window(-1, 100, -1, 40)
bgColor("darkgreen")
enableRepaint(False)

g = 9.81
dt= 0.1
v = 32 
alpha = 50

t = 0; x = 0; y = 0
vx = v * math.cos(alpha * 2*math.pi/360) 
vy = v * math.cos(alpha * 2*math.pi/360)

img = getImage("sprites/football.gif")
while t < 10: 
    vy = vy - g * dt 
    x = x + vx * dt
    y = y + vy * dt 
    image(img, x, y)
    repaint()
    t = t + dt        
    delay(50) 
    clear()   
keep()
