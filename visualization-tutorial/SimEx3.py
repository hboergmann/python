# SimEx3.py

from gpanel import *
import time

dt = 0.01
m = 0.5
k = 4
r = 0.1

t = 0; y = 0.8; v = 0

makeGPanel(-1, 11, -1.2, 1.2)
drawGrid(0, 10.0, -1.0, 1, "darkgray")
setColor("red")
lineWidth(3)

pos(t, y)
while t < 10:
      pos(t, y) if t == 0 else draw(t, y)
      F = -k*y - r*v
      a = F/m
      if t == 0:
          v = v + a*dt/2
      else:
          v = v + a*dt
      y = y + v*dt
      t = t + dt
      time.sleep(dt)
keep()

