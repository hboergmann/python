# DiagEx2.py

import random
import time
from gpanel import *

def decay():
    for i in range(N0):
        if z[i] == 1:
            if random.random() < k * dt:
                z[i] = 0

def updateDistribution():
    global N
    decayed = N - sum(z)
    if decayed <= 100:
        h[decayed] += 1
    for i in range(11):
        line(i, 0, i, h[i]) 
    N = sum(z)
      
makeGPanel(-1, 11, -5, 55)
drawGrid(0, 10, 0, 50, "gray")
lineWidth(10)
title("Number of decays in 1 sec")
k = 0.005     # Decay constant (/s) 
N0 = 1000     # Starting number of isotopes
N = N0        # Current number of isotopes
z = [1] * N0  # Population
dt = 0.01     # Time interval for population check (s)
t = 0         # Current time 
tSec = 0      # Current seconds
h = [0] * 101 # Decay distribution

while t < 100:
    currentTime = time.clock()
    decay()
    tSecNew = int(t)            
    if tSecNew != tSec: # every second
        updateDistribution()
        tSec = tSecNew
    while time.clock() - currentTime < dt:
        pass          
    t += dt
title("All done") 
keep()               
