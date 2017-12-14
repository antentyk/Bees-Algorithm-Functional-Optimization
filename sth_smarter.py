import math
import random

e = 0.1
bound = (-10, 10)
dimension = 2

def shubert(x):
    res = 1
    for item in x:
        current = sum([i * math.cos((i + 1) * item + i) for i in range(1, 6)])
        res *= current
    return res

def gennumber():
    res = random.randint(bound[0], bound[1])
    res += random.random()
    if(res < bound[0]):res += 1
    if(res > bound[1]):res -= 1
    return res

def genvector():
    return [gennumber() for i in range(dimension)]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, number):return Point(self.x * number, self.y * number)
    def __truediv__(self, number):return Point(self.x / number, self.y / number)
    def __ge__(self, other):return self.x >= other.x and self.y >= other.y
    def __le__(self, other):return self.x <= other.x and self.y <= other.y
    def __str__(self):return "Point with x={} and y={}".format(self.x, self.y)
    def __repr__(self):return str(self)

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)**0.5

class Rect:
    def __init__(self, bl, ur):
        self.bl = bl
        self.ur = ur
        self.size = ur.y - bl.y
        self.terminal = self.size / 2 <= e
        self.children = []
        self.points = []
        if(not self.terminal):self.grow()
    def grow(self):
        middle = (self.bl + self.ur) / 2
        self.children.append(Rect(middle - Point(self.size / 2, 0),
                                  middle + Point(0, self.size / 2)))
        self.children.append(Rect(middle, self.ur))
        self.children.append(Rect(middle - Point(0, self.size / 2),
                                  middle + Point(self.size / 2, 0)))
        self.children.append(Rect(self.bl, middle))
    def overlay(self, p):
        if(self.inside(p)):return True
        if(p + Point(e, 0) >= self.bl and p + Point(e, 0) <= self.ur):return True
        if(p - Point(e, 0) >= self.bl and p - Point(e, 0) <= self.ur):return True
        if(p + Point(0, e) >= self.bl and p + Point(0, e) <= self.ur):return True
        if(p - Point(0, e) >= self.bl and p - Point(0, e) <= self.ur):return True
        if(distance(p, self.bl) <= e):return True
        if(distance(p, self.bl + Point(0, self.size)) <= e):return True
        if(distance(p, self.bl + Point(self.size, 0)) <= e):return True
        if(distance(p, self.ur) <= e):return True
        return False
    def inside(self, p):
        return (self.bl <= p and p <= self.ur)
    def __str__(self):
        return ' '.join(map(str, [self.bl, self.ur, self.size]))
    def add(self, p):
        if(not self.overlay(p)):return
        if(self.terminal):
            self.points.append(p)
            return
        for child in self.children:
            child.add(p)
    def possible(self, p):
        if(not self.inside(p)):return []
        if(self.terminal):return self.points
        res = []
        for child in self.children:
            res.extend(child.possible(p))
        return res

r = Rect(Point(-10, -10), Point(10, 10))
r.add(Point(-1.2, -1.2))
