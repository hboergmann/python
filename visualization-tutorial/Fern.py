# Fern.py

from gpanel import *
import random

def fern():
    z = 0
    n = 0
    while n < nbPoints:
        r = random.random()
        c = "black"
        if r < 0.01:
            c = "yellow"
            z = f(z, 0, 0, 0, 0.16, 0, 0) # Stem
        elif r < 0.86:
            c = "green"
            z = f(z, 0.85, 0.04, -0.04, 0.85, 0, 1.60) # symmetry
        elif r > 0.86 and r < 0.93:
            c = "red"
            z = f(z, 0.20, -0.26, 0.23, 0.22, 0, 1.60)  # left leaves
        elif r > 0.93:
            c = "blue"
            z = f(z, -0.15, 0.28, 0.26, 0.24, 0, 1.44) # right leaves
        setColor(c)
        point(z)
        n += 1
        if n % 100 == 0:
			repaint()

def f(z, a, b, c, d, e, f):
    re = a * z.real + b * z.imag + e
    im = c * z.real + d * z.imag + f
    return complex(re, im)

makeGPanel(-3.5, 3.5, 0, 10)
enableRepaint(False)
bgColor("black")
nbPoints = 40000
fern()
keep()
