from PointFabric import PointFabric
from LocalController import LocalController
from ColoredPoint import ColoredPoint
from Point import Point
from Features import Features
from PointsController import PointsController

class Controller:
    def __init__(self,
                 graph,
                 settings):
        self.graph = graph
        self.settings = settings
        self.wasglobalbest = False
        self.fabric = PointFabric(self.settings.XRANGE,
                                  self.settings.YRANGE,
                                  self.settings.FUNC)
        self.sites = []
        self.pointscontroller = PointsController()
    def formsites(self):
        for i in range(self.settings.BEESNUM):
            self.sites.append(self.fabric.get())
        self.sites.sort(key = lambda item: item.z, reverse=True)
    def update(self, coloredpoint):
        self.pointscontroller.add(coloredpoint)
        if(not self.wasglobalbest):
            self.wasglobalbest = True
            newpoint = self.settings.getbest(coloredpoint.point)
            self.pointscontroller.changecolor(coloredpoint.point.id,
                                              newpoint.features.color)
            self.pointscontroller.changesize(coloredpoint.point.id,
                                              newpoint.features.size)
            self.globalbest = newpoint
            return
        if(coloredpoint.point.z < self.globalbest.point.z):
            newglobalpoint = self.settings.getbest(coloredpoint.point)
            self.pointscontroller.changecolor(coloredpoint.point.id,
                                              newglobalpoint.features.color)
            self.pointscontroller.changesize(coloredpoint.point.id,
                                             newglobalpoint.features.size)

            newlocalbestpoint = self.settings.getlocalbest(coloredpoint.point)
            self.pointscontroller.changecolor(self.globalbest.point.id,
                                              newlocalbestpoint.features.color)
            self.pointscontroller.changesize(self.globalbest.point.id,
                                             newlocalbestpoint.features.size)

            self.pointscontroller.swap(self.globalbest.point.id,
                                       newglobalpoint.point.id)
            self.globalbest = newglobalpoint
            return
    def __iter__(self):
        self.formsites()
        elite = self.sites[:self.settings.ELITE]
        if(len(self.sites) > len(elite)):
            nonelite = self.sites[self.settings.ELITE:self.settings.ELITE + self.settings.NONELITE]
        else: nonelite = []
        for elitesite in elite:
            lc = LocalController(True,
                                 self.pointscontroller,
                                 self.settings,
                                 elitesite,
                                 self.graph)
            for state in lc:
                yield state
            lc.clear()
            self.update(lc.getlocalbest())
            self.pointscontroller.set(self.graph)
            yield self.graph
        for nonelitesite in nonelite:
            lc = LocalController(False,
                                 self.pointscontroller,
                                 self.settings,
                                 nonelitesite,
                                 self.graph)
            for state in lc:
                yield state
            lc.clear()
            self.update(lc.getlocalbest())
            self.pointscontroller.set(self.graph)
            yield self.graph
    def getglobalbest(self):
        return self.globalbest