# Star.py

from gpanel import *
from math import sqrt, radians, sin, cos

class Star():
    def __init__(self, size):
        self.size = size
        self.color = "yellow"
        self.direction = 0
        self.triangle1 = [[-sqrt(3)/2 * self.size, -self.size/2],
                     [sqrt(3)/2 * self.size, -self.size/2],
                     [0, self.size]]
        self.triangle2 = [[-sqrt(3)/2 * self.size, self.size/2],
                     [sqrt(3)/2 * self.size, self.size/2],
                     [0, -self.size]]
 
    def setColor(self, color):
        self.color = color

    def getDirection(self):
        return self.direction

    def rotate(self, angle):
        self.direction += angle
        self.triangle1 = self._rotatePolygon(self.triangle1, angle)             
        self.triangle2 = self._rotatePolygon(self.triangle2, angle)             
        
    def draw(self, position):
        setColor(self.color)
        fillPolygon(self._translatePolygon(self.triangle1, 
                    position[0], position[1]))
        fillPolygon(self._translatePolygon(self.triangle2, 
                    position[0], position[1]))
                  
    def _translatePolygon(self, polygon, x, y):
        translatedPolygon = []
        for corner in polygon:
            translatedPolygon.append([corner[0] + x, corner[1] + y])
        return translatedPolygon

    def _rotatePolygon(self, polygon, theta):
        theta = radians(theta)
        rotatedPolygon = []
        for corner in polygon :
            rotatedPolygon.append(
            [corner[0] * cos(theta) - corner[1] * sin(theta), 
             corner[0] * sin(theta) + corner[1] * cos(theta)])
        return rotatedPolygon                 
