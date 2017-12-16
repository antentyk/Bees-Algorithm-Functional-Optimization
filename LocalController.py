from NeighbourCoordinateFabric import NeighbourCoordinateFabric


class LocalController:
    """
    This class represents a Controller of
    plotting the graph while performing
    the local search
    """

    def __init__(self,
                 iselite,
                 pointscontroller,
                 settings,
                 center,
                 graph):
        """
        Initializes new LocalController instance
        adds center and tor to the point controller

        :param iselite(bool): determines if the neighbourhood is elite
        :param pointscontroller(PointsController): PoinsController instance
        :param settings (Settings): settings of the graph to be plotted and
            bees algorithm itself
        :param center (Coordinate): represents a center of the neihjbourhood
            to explore
        :param graph (matplotlib.pyplot.scatter): graph instance that
            needs to be filled while exporing the neighbourhood
        """
        if (iselite):
            self.pointsleft = settings.RECRUITEDELITE
        else:
            self.pointsleft = settings.RECRUITEDNONELITE

        self.pointscontroller = pointscontroller
        self.settings = settings
        self.center = center
        self.fabric = NeighbourCoordinateFabric(center, settings)
        self.graph = graph

        self.currentlyadded = 2
        self.localbest = self.settings.getlocalbest(center)  # point
        self.pointscontroller.add(self.localbest)
        self.pointscontroller.add(self.settings.gettor(center))

    def add(self, coordinate):
        """
        Adds a coordinate to the graph
        If a new coordinate is better than local minimum,
        Changes that Features of affected points

        :param coordinate (Coordinate): coordinate that needs to be added
        :return: None
        """
        self.currentlyadded += 1

        if (coordinate.z >= self.localbest.coordinate.z):
            self.pointscontroller.add(self.settings.getbad(coordinate))
            return

        oldbestid = self.localbest.id

        self.pointscontroller.changesize(oldbestid, self.settings.SIZEBAD)

        newcolor = self.settings.getrgbcolor(self.localbest.coordinate.z)
        newcolor.append(self.settings.OPACITYBAD)
        self.pointscontroller.changecolor(oldbestid, newcolor)

        current = self.settings.getlocalbest(coordinate)
        self.pointscontroller.add(current)

        self.localbest = current

        self.pointscontroller.swap(self.localbest.id, oldbestid)

    def clear(self):
        """
        Deletes all the points that were added during the neighbourhood
        exploration
        """
        self.pointscontroller.pop(self.currentlyadded)

    def getlocalbestcoordinate(self):
        """
        Returns a coordinate of the local best point
        in this neighbourhood

        :return (Coordinate): local minimum coordinate in this neighbourhood
        """
        return self.localbest.coordinate

    def __iter__(self):
        """
        Performs local search by adding points
        Yields frames - a graph representation in particular moment of time

        :return: generator for self.graph while exploring the neighbourhood
        """
        while (self.pointsleft > 0):
            current = min(self.pointsleft, self.settings.LOCALSKIPNUM)
            for i in range(current):
                self.add(self.fabric.getcoordinate())
            self.pointsleft -= self.settings.LOCALSKIPNUM
            self.pointscontroller.set(self.graph)
            yield self.graph
