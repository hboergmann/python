# ShapesEx6.py

from gpanel import *

xRed = 200
yRed = 200
xGreen = 300
yGreen = 200
xBlue = 250
yBlue = 300

makeGPanel(Size(501, 501))
enableRepaint(False)
window(0, 500, 500, 0)    # y axis downwards
for x in range(501):
    for y in range(501):
        red = green = blue = 0
        if (x - xRed) * (x - xRed) + (y - yRed) * (y - yRed) < 16000:
            red = 255
        if (x - xGreen) * (x - xGreen) + (y - yGreen) * (y - yGreen) < 16000:
            green = 255
        if (x - xBlue) * (x - xBlue) + (y - yBlue) * (y - yBlue) < 16000:
           blue = 255
        setColor(makeColor(red, green, blue))
        point(x, y)
    repaint()
keep()
