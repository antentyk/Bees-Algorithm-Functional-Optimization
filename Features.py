class Features:
    """
    This class represents Feautes of the point
    that will be plotted on the graph
    """
    def __init__(self, size, color, border):
        """
        Initializes new Feaures instance by given values

        :param size (float): determines the size of the point

        :param color (list(float) or tuple(float)): color representation of the point
            you should pass 4 floats in that tuple that will represent(RGBA):
                - R - red intensity in range [0; 1]
                - G - green intensity in range [0; 1]
                - B - blue intensity in range [0; 1]
                - A - opacity in range [0; 1]
            hence point (1, 0, 0, 1) will be red
                  point (0, 0, 0, 1) will be black
                  point (0, 0, 0, 0) will be transparent

        :param border (list(float) or tuple(float)): representation of
            the color of the border of the point
            read color parameter documentation for more specifications
            (width of the border is not included here)
        """
        self.size = size
        self.color = color
        self.border = border