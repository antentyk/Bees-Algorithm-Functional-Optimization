from PointFabric import PointFabric
from Point import Point

class RandomApproachText:
    def __init__(self, func, settings, pointsnum):
        self.fabric = PointFabric(settings.XRANGE,
                                  settings.YRANGE,
                                  func)
        self.bestpoint = Point(float('inf'),
                               float('inf'),
                               float('inf'))
        self.pointsnum = pointsnum

    def get(self):
        for i in range(self.pointsnum):
            point = self.fabric.get()
            if(point.z < self.bestpoint.z):
                self.bestpoint = point
        return self.bestpoint

    def formreport(self):
        result = ""
        result += "Points analyzed: {}\n".format(self.pointsnum)
        result += "Best fit: z = {} for x = {} and y = {}".format(self.bestpoint.z,
                                                                  self.bestpoint.x,
                                                                  self.bestpoint.y)
        return result