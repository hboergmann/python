# MouseeventEx2.py

from gpanel import *

def drawLines(p):
    for q in graph[:-1]:
        line(p, q)

def addNode(x, y):
    p = [x, y]    
    pos(p) 
    fillCircle(1)
    graph.append(p)    
    drawLines(p)

makeGPanel(0, 100, 0, 100, mousePressed = addNode)
graph = []
keep()


