class Coordinate:
    """
    This class represents a point in 3d space
    with float x, y, and z
    """
    def __init__(self, x, y, z):
        """
        Initializes a new coordinate instance

        :param x (float): x coordinate of the point in Cartesian coordinate system
        :param y (float): y coordinate of the point in Cartesian coordinate system
        :param z (float): z coordinate of the point in Cartesian coordinate system
        """
        self.x = x
        self.y = y
        self.z = z