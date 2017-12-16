class PointsHolder:
    """
    This class represents a storage for the
        Points that will be plotted on the graph
    """

    def __init__(self):
        """
        Initializes an empty storage
        It includes:
            offsets (list(list(float, float))): x and y coordinates
                of plotted points
            sizes (list(float)): sizes of the plotted points
            colors (list(list(float))): RGBA colors of the potted points
                (see more about RGBA color in Features documentation)
            borders (list(list(float))): RGBA colors of the borders
                of the plotted points
                (see more about RGBA color in Features documentation)
            position (dict(int: int)): index of the particular Point
                instance in all the lists mentioned above
        """
        self.offsets = []
        self.sizes = []
        self.colors = []
        self.borders = []
        self.position = {}

    def clear(self):
        """
        deletes all points from the storage
        """
        self.offsets = []
        self.sizes = []
        self.colors = []
        self.borders = []
        self.position = {}

    def pop(self, num):
        """
        deletes last num points from the storage

        precondition: num >= 1
        :param num (int): number of points to be deleted from the storage
        """
        self.offsets = self.offsets[:-num]
        self.sizes = self.sizes[:-num]
        self.colors = self.colors[:-num]
        self.borders = self.borders[:-num]

    def add(self, point):
        """
        adds Point instance to the storage

        :param point (Point): a point that needs to be added
        """
        self.offsets.append([point.coordinate.x, point.coordinate.y])
        self.sizes.append(point.features.size)
        self.colors.append(point.features.color)
        self.borders.append(point.features.border)
        self.position[point.id] = len(self.offsets) - 1

    def getposition(self, pointid):
        """
        precondition: Point with pointid is in the storage
        :param pointid (int):
        :return (int): index of the particular Point instance
        """
        return self.position[pointid]
