from PointsHolder import PointsHolder


class PointsController:
    """
    This class represents a controller
    of the points storage of Point instances

    In addition to PointsHolder functionality, it can
    - change size of some point in the storage
    - change color of some point in the storage
    - swap 2 arbitrary points in the storage
    - fill the particular graph instance with the points
        in the storage
    """
    def __init__(self):
        """
        Initializes a new PointsController instance with
        an empty storage
        """
        self.holder = PointsHolder()

    def add(self, point):
        """
        see PointsHolder.add() documentation
        """
        self.holder.add(point)

    def getposition(self, pointid):
        """
        see PointsHolder.getposition() documentation
        """
        return self.holder.getposition(pointid)

    def pop(self, num):
        """
        see PointsHolder.pop() documentation
        """
        self.holder.pop(num)

    def clear(self):
        """
        see PointsHolder.clear() documentation
        """
        self.holder.clear()

    def swap(self, pointid1, pointid2):
        """
        Swaps points in the storage.
        Points ids are pointid1 and pointid2 respectively

        :param pointid1 (int): id of the first point
        :param pointid2 (int): id of the second point
        :return: None
        """
        i1 = self.getposition(pointid1)
        i2 = self.getposition(pointid2)
        self.holder.offsets[i1], self.holder.offsets[i2] = self.holder.offsets[i2], self.holder.offsets[i1]
        self.holder.sizes[i1], self.holder.sizes[i2] = self.holder.sizes[i2], self.holder.sizes[i1]
        self.holder.colors[i1], self.holder.colors[i2] = self.holder.colors[i2], self.holder.colors[i1]
        self.holder.borders[i1], self.holder.borders[i2] = self.holder.borders[i2], self.holder.borders[i1]
        self.holder.position[pointid1] = i2
        self.holder.position[pointid2] = i1

    def changesize(self, pointid, newsize):
        """
        Changes size of the Point in the storage
            with id equals to pointid to newsize

        :param pointid (int): id of the point that needs to be changed
        :param newsize (float): new size of the point that needs to be set
        :return: None
        """
        i = self.getposition(pointid)
        self.holder.sizes[i] = newsize

    def changecolor(self, pointid, newcolor):
        """
        Changes color of the Point in the storage
            with id equals to pointid to newcolor

        :param pointid (int): id of the point that needs to be changed
        :param newcolor (list(float) or tuple()): RGBA representation
            of the new color of the point that needs to be set
            (see Features documentation for more details about RGBA)
        :return: None
        """
        i = self.getposition(pointid)
        self.holder.colors[i] = newcolor

    def set(self, graph):
        """
        fill graph with all points available in storage

        :param graph (matplotlib.pyplot.scatter): graph instance that
            needs to be filled with all points in storage
        :return: None
        """
        graph.set_offsets(self.holder.offsets)
        graph.set_sizes(self.holder.sizes)
        graph.set_facecolors(self.holder.colors)
        graph.set_edgecolor(self.holder.borders)
