# GuiEx2.py

from gpanel import *
import random
from javax.swing import *

def actionCallback(e):
    global c
    if e.getSource() == btn4:
        setColor(c)
        moire()
    if e.getSource() == btn1:
        c = "red"
    if e.getSource() == btn2:
        c = "green"
    if e.getSource() == btn3:
        c = "blue"
    
def createGUI():
    addComponent(btn1)
    addComponent(btn2)
    addComponent(btn3)
    addComponent(btn4)
    validate()

def moire():
    for i in range(11):
        for k in range (11):
            line(i, 0, k, 10)
    
    for i in range(11):
        for k in range (11):
            line(0, i, 10, k)
 
btn1 = JButton("Red", actionListener = actionCallback)
btn2 = JButton("Green", actionListener = actionCallback)
btn3 = JButton("Blue", actionListener = actionCallback)
btn4 = JButton("GO", actionListener = actionCallback)

makeGPanel(0, 10, 0, 10.5)
createGUI()
c = "black"

