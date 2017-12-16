from CoordinateFabric import CoordinateFabric
from LocalController import LocalController
from Point import Point
from Coordinate import Coordinate
from Features import Features
from PointsController import PointsController


class Controller:
    """
    This class represents a Controller of
    plotting the overall graph - a bunch of local searches
    """

    def __init__(self,
                 graph,
                 settings):
        """
        :param graph (matplotlib.pyplot.scatter): graph instance that
            needs to be filled while exporing the neighbourhood
        :param settings (Settings): settings of the graph to be plotted and
            bees algorithm itself
        Settings that are used here:
            determing elite and nonelite sites:
                - BEESNUM
                - ELITE
                - NONELITE
                - RECRUITEDELITE
                - RECRUITEDNONELITE
            plotting the points on the graph:
                - getbest()
                - getlocalbest()
                - SIZELOCALBEST
                - OPACITYLOCALBEST
                - getrgbcolor()
        """
        self.graph = graph
        self.settings = settings
        self.globalbest = Point(Coordinate(float('inf'), float('inf'), float('inf')),
                                Features(None, None, None))
        self.wasglobalbest = False
        self.fabric = CoordinateFabric(settings)
        self.sites = []
        self.pointscontroller = PointsController()

    def formsites(self):
        """
        This function is used to determine to elite and nonelite
            site.
        It picks random points on a plane and sorts it in
            ascending order of function value
        """
        for i in range(self.settings.BEESNUM):
            self.sites.append(self.fabric.getcoordinate())
        self.sites.sort(key=lambda item: item.z)

    def add(self, coordinate):
        """
        adds Cooordinate to the graph
        coordinate is assumed to be a result of a local search
        hence, function can update the global minimum
        or just add a Point as local best

        :param coordinate (Coordinate): localbest coordinate of performed
            local search
        :return: None
        """
        if (not self.wasglobalbest):
            self.wasglobalbest = True
            self.globalbest = self.settings.getbest(coordinate)
            self.pointscontroller.add(self.globalbest)
            return

        if (coordinate.z < self.globalbest.coordinate.z):
            current = self.settings.getbest(coordinate)
            self.pointscontroller.add(current)

            color = self.settings.getrgbcolor(coordinate.z)
            color.append(self.settings.OPACITYLOCALBEST)
            self.pointscontroller.changecolor(self.globalbest.id,
                                              color)
            self.pointscontroller.changesize(self.globalbest.id,
                                             self.settings.SIZELOCALBEST)

            self.globalbest = current
            return

        self.pointscontroller.add(self.settings.getlocalbest(coordinate))

    def __iter__(self):
        """
        Performs overall plotting of the graph
        Yields frames - a graph representation in particular moment of time

        :return: generator for self.graph while performing bees algorithm
        """
        self.formsites()

        elite = self.sites[:self.settings.ELITE]

        if (len(self.sites) > len(elite)):
            nonelite = self.sites[self.settings.ELITE:self.settings.ELITE + self.settings.NONELITE]
        else:
            nonelite = []

        for elitesite in elite:
            lc = LocalController(True,
                                 self.pointscontroller,
                                 self.settings,
                                 elitesite,
                                 self.graph)
            for state in lc:
                yield state
            lc.clear()
            self.add(lc.getlocalbestcoordinate())
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
            self.add(lc.getlocalbestcoordinate())
            self.pointscontroller.set(self.graph)
            yield self.graph

    def getglobalbest(self):
        """
        :return (Point): Point instance that corresponds to the global minimum
            found at that moment
        """
        return self.globalbest
