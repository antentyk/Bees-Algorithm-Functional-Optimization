from random import random
from Point import Point
from math import pi, sin, cos

class NeighbourPointFabric:
    def __init__(self, xrange, yrange, func, center, ngh):
        self.xrange = xrange
        self.yrange = yrange
        self.func = func
        self.center = center
        self.ngh = ngh
    def get(self):
        while(True):
            d = self.ngh * random()
            angle = (pi * 2) * random()

            x = d * cos(angle) + self.center.x
            y = d * sin(angle) + self.center.y

            newpoint = Point(x, y, 0)
            if(newpoint.x < self.xrange[0] or newpoint.x > self.xrange[1]):continue
            if(newpoint.y < self.yrange[0] or newpoint.y > self.yrange[1]):continue
            newpoint.z = self.func(newpoint.x, newpoint.y)
            return newpoint