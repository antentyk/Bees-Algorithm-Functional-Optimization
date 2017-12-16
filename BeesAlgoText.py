from Coordinate import Coordinate
from CoordinateFabric import CoordinateFabric
from NeighbourCoordinateFabric import NeighbourCoordinateFabric
from Settings import Settings


class BeesAlgoText:
    """
    This class is responsible for performing the bees
    algorithm withoute plotting the graph
    """
    def __init__(self, settings):
        """
        Initializes a new instance of BeesAlgoText

        :param settings (Settings): settingsof the bees algorithm
        Settings that are used here:
                - BEESNUM
                - ELITE
                - NONELITE
                - RECRUITEDELITE
                - RECRUITEDNONELITE
        """
        self.settings = settings
        self.fabric = CoordinateFabric(settings)
        self.best = Coordinate(float('inf'),
                               float('inf'),
                               float('inf'))

    def get(self):
        """
        Performs the bees algorithm itself

        :return (Coordinate): Coordinate instance that represents a global minimum
          after performing the bees algorithm
        """
        points = []
        for i in range(self.settings.BEESNUM):
            points.append(self.fabric.getcoordinate())
        points.sort(key=lambda item: item.z)

        for i in range(min(self.settings.ELITE, len(points))):
            current = self.neighbourhoodsearch(points[i], True)
            if (current.z < self.best.z): self.best = current

        for i in range(self.settings.NONELITE):
            if (i + self.settings.ELITE >= len(points)): break
            current = self.neighbourhoodsearch(points[i + self.settings.ELITE], False)
            if (current.z < self.best.z): self.best = current
        return self.best

    def neighbourhoodsearch(self, center, iselite):
        """
        Performs a local search and returns ocal minimum

        :param center (Coordinate): coordinate of the center of the neighbourhood
        :param iselite(bool): determines whether the neighbourhood
            is elite
        :return (Coordinate): Coordinate instance that represents
            a local minimum found while performing local search
        """
        result = center
        neighbourfabric = NeighbourCoordinateFabric(center,
                                               self.settings)

        if (iselite): itnum = self.settings.RECRUITEDELITE
        else: itnum = self.settings.RECRUITEDNONELITE

        for i in range(itnum):
            current = neighbourfabric.getcoordinate()
            if (current.z < result.z): result = current
        return result

    def formreport(self):
        """
        Returns a string representation of the report
        that contains that following information;
            - number of points that were evaluated during
                performing the bees algorithm
            - coordinates of the global minimum found

        :return (str):
        """
        pointsnum = self.settings.RECRUITEDELITE * self.settings.ELITE
        pointsnum += self.settings.RECRUITEDNONELITE * self.settings.NONELITE
        result = ""
        result += "Points analyzed: {}\n".format(pointsnum)
        result += "Best fit: z = {} for x = {} and y = {}".format(self.best.z,
                                                                  self.best.x,
                                                                  self.best.y)
        return result


if __name__ == '__main__':
    b = BeesAlgoText(Settings)
    b.get()
    print(b.formreport())
