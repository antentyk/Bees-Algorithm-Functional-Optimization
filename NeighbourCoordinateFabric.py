from random import random
from Coordinate import Coordinate
from math import pi, sin, cos


class NeighbourCoordinateFabric:
    """
    This class represents a Fabric of neighbours of some coordinate
        (z coordinate is not counted)
    it returns random coordinates that are not further than
        described in settings of the graph and in valid ranges at the same time
    see __init__() documentation for more details
    """

    def __init__(self, center, settings):
        """
        :param center (Coordinate): center of the neighbourhood
        :param settings (Settings): settings of the graph and bees algorithm itself
            the following settings are used:
                - XRANGE - minimum and maximmu value of x coordinate
                    that will be plotted on the graph
                - YRANGE - minimum and maximmu value of y coordinate
                    that will be plotted on the graph
                - FUNC - function researched. Gives you z coordinate by
                    providing x and y
                - NGH - size of neighbourhood (i.e maximal distance between the center of the
                    neighbourhood and the point that can be returned by a fabric in XY plane)
        """
        self.xrange = settings.XRANGE
        self.yrange = settings.YRANGE
        self.func = settings.FUNC
        self.center = center
        self.ngh = settings.NGH

    def getcoordinate(self):
        """
        Returns random neighbour coordinates

        :return (Coordinate): random coordinate that is
            not further than ngh from center in XY plane
            this coordinate is also in proper range that is specified
            by XRANGE and YRANGE (see __init__() documentation)
            z coordinate is a function valid in a corresponding x and y
            (function is provided in graph settings (see __init__() documentation))
        """
        while (True):
            d = self.ngh * random()
            angle = (pi * 2) * random()

            x = d * cos(angle) + self.center.x
            y = d * sin(angle) + self.center.y

            coordinate = Coordinate(x, y, 0)
            if (coordinate.x < self.xrange[0] or coordinate.x > self.xrange[1]): continue
            if (coordinate.y < self.yrange[0] or coordinate.y > self.yrange[1]): continue
            coordinate.z = self.func(coordinate.x, coordinate.y)

            return coordinate
