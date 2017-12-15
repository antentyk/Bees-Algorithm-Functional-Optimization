from PointFabric import PointFabric
from Controller import Controller
from Holder import Holder

import matplotlib.pyplot as plt

class RandomApproach:
    def __init__(self,
                 func,
                 settings,
                 pointsnum,
                 skipnum,
                 figurenum=100):
        self.fabric = PointFabric(settings.XRANGE,
                                  settings.YRANGE,
                                  func)
        self.holder = Holder()
        self.controller = Controller(self.holder, settings)
        self.pointsleft = pointsnum
        self.skipnum = skipnum

        self.fig = plt.figure(figurenum)
        plt.xlim(settings.XRANGE[0],
                 settings.XRANGE[1],)
        plt.ylim(settings.YRANGE[0],
                 settings.YRANGE[1],)
        self.graph = plt.scatter([], [], cmap=settings.COLORMAP)

    def __iter__(self):
        while(self.pointsleft):
            for i in range(min(self.pointsleft, self.skipnum)):
                self.controller.add(self.fabric.get())
            self.pointsleft -= self.skipnum
            self.graph.set_offsets(self.holder.offsets)
            self.graph.set_sizes(self.holder.sizes)
            self.graph.set_facecolors(self.holder.colors)
            yield self.graph