from NeighbourPointFabric import NeighbourPointFabric
from Point import Point
from Features import Features
from ColoredPoint import ColoredPoint

class LocalController:
    def __init__(self,
                 iselite,
                 pointscontroller,
                 settings,
                 center,
                 graph):
        if(iselite):self.pointsleft = settings.RECRUITEDELITE
        else: self.pointsleft = settings.RECRUITEDNONELITE
        self.pointscontroller = pointscontroller
        self.settings = settings
        self.center = center
        self.fabric = NeighbourPointFabric(
            settings.XRANGE,
            settings.YRANGE,
            settings.FUNC,
            center,
            settings.NGH
        )
        self.graph = graph
        self.currentlyadded = 2
        self.localbest = self.settings.getlocalbest(self.center)
        self.pointscontroller.add(self.localbest)
        torcenter = Point(self.center.x,
                         self.center.y,
                         self.center.z)
        tor = self.settings.gettor(torcenter)
        self.pointscontroller.add(tor)
    def add(self, point):
        self.currentlyadded += 1

        if(point.z >= self.localbest.point.z):
            current = self.settings.getbad(point)
            self.pointscontroller.add(current)
            return

        oldbestid = self.localbest.point.id
        self.pointscontroller.changesize(oldbestid,
                                         self.settings.SIZEBAD)
        newcolor = self.settings.decideoncolor(self.localbest.point.z)
        newcolor.append(self.settings.OPACITYBAD)
        self.pointscontroller.changecolor(oldbestid, newcolor)

        current = self.settings.getlocalbest(point)
        self.pointscontroller.add(current)

        self.localbest = current

        self.pointscontroller.swap(self.localbest.point.id, oldbestid)
        return
    def clear(self):
        self.pointscontroller.pop(self.currentlyadded)
    def getlocalbest(self):
        return self.localbest
    def __iter__(self):
        while(self.pointsleft > 0):
            current = min(self.pointsleft, self.settings.LOCALSKIPNUM)
            for i in range(current):
                self.add(self.fabric.get())
            self.pointsleft -= self.settings.LOCALSKIPNUM
            self.pointscontroller.set(self.graph)
            yield self.graph