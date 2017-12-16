from random import random
from Coordinate import Coordinate


class CoordinateFabric:
    """
    This class represents a fabric of random coordinates
    in ranges that are specified by settings of the graph
    see __init__() documentation for more details
    """

    def __init__(self, settings):
        """
        Initializes new fabric instance

        :param settings (Settings): represents settings of the graph
            the following settings are used:
                - XRANGE - minimum and maximmu value of x coordinate
                    that will be plotted on the graph
                - YRANGE - minimum and maximmu value of y coordinate
                    that will be plotted on the graph
                - FUNC - function researched. Gives you z coordinate by
                    providing x and y
        """
        self.xrange = settings.XRANGE
        self.yrange = settings.YRANGE
        self.func = settings.FUNC

    def getcoordinate(self):
        """
        :return (Coordinate): random coordinate in 3d space
            x and y are picked randomly according to the XRANGE and YRANGE
            that are specified in graph settings (see __init__() documentation)
            z coordinate is a function value in a corresponding coordinate
            (3d function is taken from settings specification (see __init__() documentation))
        """
        x = self.xrange[0] + random() * (self.xrange[1] - self.xrange[0])
        y = self.yrange[0] + random() * (self.yrange[1] - self.yrange[0])
        z = self.func(x, y)
        return Coordinate(x, y, z)
