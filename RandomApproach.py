import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

from Point import Point
from functions import cross_in_tray
from settings import *


class ColoredPoint:
    idcounter = 0
    def __init__(self):
        self.id = self.idcounter
        ColoredPoint.idcounter += 1
        self.x = 0
        self.y = 0
        self.z = 0
        self.color = (0,0,0,0)
        self.size = 0
    def __str__(self):return str(self.id)

class RandomApproach:
    def __init__(self,
                 func=cross_in_tray,
                 p1=p1,
                 p2=p2,
                 badsize=badsize,
                 goodsize=goodsize,
                 colormap=colormap,
                 pointsnum=10**4,
                 skip=1):

        self.fig = plt.figure(100)
        plt.xlim(p1.x, p2.x)
        plt.ylim(p1.y, p2.y)
        self.graph = plt.scatter([], [], cmap=colormap)

        self.holder = Holder()

        self.p1 = p1
        self.p2 = p2

        self.pointsnum = pointsnum
        self.goodsize = goodsize
        self.badsize = badsize

        self.func = func
        self.skip = skip

        self.best = self.getrandompoint()
        self.holder.addPoint(self.best)
        self.makegood(self.best)
    def getrandompoint(self):
        x = self.p1.x + random.random() * (self.p2.x - self.p1.x)
        y = self.p1.y + random.random() * (self.p2.y - self.p1.y)
        res = ColoredPoint()
        res.x = x
        res.y = y
        res.z = self.func(x, y)
        res.size = self.badsize
        res.color = badcolor
        return res
    def makegood(self, p):
        i = self.holder.getposition(p)
        self.holder.colors[i] = goodcolor
        self.holder.sizes[i] = goodsize
    def makebad(self, p):
        i = self.holder.getposition(p)
        self.holder.colors[i] = badcolor
        self.holder.sizes[i] = badsize
    def update(self, p):
        newz = self.func(p.x, p.y)
        self.holder.addPoint(p)
        if(newz < self.best.z):
            self.makebad(self.best)
            self.best = p
            self.makegood(p)
    def __iter__(self):
        while(self.pointsnum > 0):
            for i in range(min(self.pointsnum, self.skip)):
                self.update(self.getrandompoint())
            self.pointsnum -= self.skip
            self.graph.set_offsets(self.holder.offsets)
            self.graph.set_sizes(self.holder.sizes)
            self.graph.set_facecolors(self.holder.colors)
            yield self.graph

class Holder:
    def __init__(self):
        self.offsets = []
        self.sizes = []
        self.colors = []
    def getposition(self, p):
        return p.id
    def addPoint(self, p):
        self.offsets.append([p.x, p.y])
        self.sizes.append(p.size)
        self.colors.append(p.color)

r = RandomApproach(skip=10)
it = r.__iter__()

def animate(i):
    return it.__next__()

ani = FuncAnimation(r.fig, animate, repeat=False, interval=1)
plt.show()