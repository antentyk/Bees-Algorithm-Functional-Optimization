from random import random
from Point import Point


class PointFabric:
    def __init__(self, xrange, yrange, func):
        self.xrange = xrange
        self.yrange = yrange
        self.func = func
    def get(self):
        x = self.xrange[0] + random() * (self.xrange[1] - self.xrange[0])
        y = self.yrange[0] + random() * (self.yrange[1] - self.yrange[0])
        z = self.func(x, y)
        return Point(x, y, z)