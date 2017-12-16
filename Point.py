class Point:
    """
    This class represents a point that can be plotted on a graph
    with its coordinates and features
    """
    idcounter = 0
    def __init__(self, c, f):
        """
        Initializes new Point instance with unique id

        :param c (Coordinate): specifies coordinates of the point
        :param f (Features): specifies the features of the point
        """
        self.id = Point.idcounter
        Point.idcounter += 1
        self.coordinate = c
        self.features = f