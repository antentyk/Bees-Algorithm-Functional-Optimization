from Point import Point
from PointFabric import PointFabric
from NeighbourPointFabric import NeighbourPointFabric
from Settings import Settings

class BeesAlgoText:
    def __init__(self, settings):
        self.settings = settings
        self.fabric = PointFabric(self.settings.XRANGE,
                                  self.settings.YRANGE,
                                  self.settings.FUNC)
        self.best = Point(float('inf'),
                          float('inf'),
                          float('inf'))

    def get(self):
        points = []
        for i in range(self.settings.BEESNUM):
            points.append(self.fabric.get())
        points.sort(key=lambda item: item.z)
        for i in range(min(self.settings.ELITE, len(points))):
            current = self.neighbourhoodsearch(points[i], True)
            if(current.z < self.best.z):self.best = current
        for i in range(self.settings.NONELITE):
            if(i + self.settings.ELITE >= len(points)):break
            current = self.neighbourhoodsearch(points[i + self.settings.ELITE], False)
            if (current.z < self.best.z): self.best = current
        return self.best

    def neighbourhoodsearch(self, center, iselite):
        result = center
        neighbourfabric = NeighbourPointFabric(self.settings.XRANGE,
                                               self.settings.YRANGE,
                                               self.settings.FUNC,
                                               center,
                                               self.settings.NGH)
        if(iselite):itnum = self.settings.RECRUITEDELITE
        else:itnum = self.settings.RECRUITEDNONELITE
        for i in range(itnum):
            current = neighbourfabric.get()
            if(current.z < result.z):result = current
        return result

    def formreport(self):
        pointsnum = self.settings.RECRUITEDELITE * self.settings.ELITE
        pointsnum += self.settings.RECRUITEDNONELITE * self.settings.NONELITE
        result = ""
        result += "Points analyzed: {}\n".format(pointsnum)
        result += "Best fit: z = {} for x = {} and y = {}".format(self.best.z,
                                                                  self.best.x,
                                                                  self.best.y)
        return result
