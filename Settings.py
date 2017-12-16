from pylab import cm
from functions import cross_in_tray
from Point import Point
from Features import Features


class Settings:
    """
    This class represents settings of the graph that
        will be plotted and bees algorithm parameters.
    The graph is in 2d despite that fact that it represents a 3d function
    (color of the point represents a z coordinate of the corresponding point)

    GRAPH SETTINGS:
        - XRANGE (tuple(float or int)):
            tuple of 2 numbers that specifies that minimal and maximal
            x limits respectively
        - YRANGE (tuple(float or int)):
            tuple of 2 numbers that specifies that minimal and maximal
            y limits respectively
        - COLORMAP (matplotlib colormap object):
            it is used to determine the color of the point according to its z
            coordinate
        - LOCALSKIPNUM (int) - number of points that will be plotted in 1 frame
            while exploring the neighbourhood of the point
        - BIGGESTOBSERVED (float) - benchmark - biggest function value z that was observed in
            xrange and yrange
                (it is needed to determine the color of the point plotted)
        - LOWESTOBSERVED (float) - benchmark - smallest function value z that was observed in
            xrange and yrange
                (it is needed to determine the color of the point plotted)

        POINTS SETTINGS:
            there are 4 types of points that can be plotted on the graph
            1) BEST - the best fit of all considered points (global minimum)
                this point has ther biggest size
            2) LOCALBEST - the best point in the neighbourhood
                it is smaller than GLOBALBEST
            3) BAD - point that is neither GLOBALBEST nor LOCALBEST
                it is smaller than LOCALBEST
            4) TOR - a transparent point with solid border
                that represents borders of the neighbourhood
                (it is the biggest one)
            there are settings for each of the 4 types
            they include
                - width of the border (for tor)
                - color of the border (for all)
                - color (fr tor)
                - size (for all)
                - opacity (for all)

            List of all point settings:
                - SIZEBEST (int or float)
                - SIZELOCALBEST (int or float)
                - SIZEBAD (int or float)
                - SIZETOR (int or float)
                - BORDERCOLORBEST - RGBA color
                    (see features documentation for more details)
                - BORDERCOLORLOCALBEST - RGBA color
                - BORDERCOLORBAD - RGBA color
                - BORDERCOLOROR - RGBA color
                - OPACITYBEST - float in range [0; 1]
                - OPACITYLOCALBEST - float in range [0; 1]
                - OPACITYBAD - float in range [0; 1]
                - FILLCOLORTOR - GRBA color
                - BORDERWIDTH - int

        BEES ALGORITHM SETTINGS:
            - FUNC (func(float, float) -> float) - function researched.
                It should return you z coordinate be providing x and y
            - BEESNUM (int) - number of neighbourhoods to consider (scoutbees)
            - ELITE (int) - number of elite neighbourhoods
            - NONELITE (int) - number of nonelite neighbourhood
            - RECRUITEDELITE (int) - number of points to explore in elite neighbourhoods
            - RECRUITEDNONELITE (int) - number of points to explore in nonelite neighbourhoods
            - NGH (int) - size of the neighourhood
    """

    XRANGE = (-10, 10)
    YRANGE = (-10, 10)

    COLORMAP = cm.get_cmap('hot')

    SIZEBEST = 300
    SIZELOCALBEST = 100
    SIZEBAD = 10
    SIZETOR = 100000 / 2.54

    BORDERCOLORBEST = (0, 0, 0, 0)
    BORDERCOLORLOCALBEST = (0, 0, 0, 0)
    BORDERCOLORBAD = (0, 0, 0, 0)
    BORDERCOLORTOR = (0, 0, 0, 1)

    OPACITYBEST = 1
    OPACITYLOCALBEST = 1
    OPACITYBAD = 1

    FILLCOLORTOR = (0, 0, 0, 0)

    BORDERWIDTH = 3

    BIGGESTOBSERVED = 1
    LOWESTOBSERVED = -3

    BEESNUM = 100
    ELITE = 10
    NONELITE = 5
    RECRUITEDELITE = 100
    RECRUITEDNONELITE = 20
    NGH = 2

    LOCALSKIPNUM = 10
    FUNC = cross_in_tray

    @classmethod
    def getrgbcolor(cls, z):
        """
        :param z (float): function value in some point
        :return (list(float)): returns RGB representation of the color
            that corresponds to function value z and colormap given in settings
            (see Features documentation to get more about RGB color)
        """
        percent = (z - cls.LOWESTOBSERVED) / (cls.BIGGESTOBSERVED - cls.LOWESTOBSERVED)
        percent = min(percent, 1 - (1e-9))
        percent = max(percent, 1e-9)
        color = cls.COLORMAP(percent)
        return list(color)[:3]

    @classmethod
    def getbest(cls, coordinate):
        """
        :param coordinate (Coorindate): coordinate of the point in Cartesian space
        :return (Point): BEST point that corresponds to coordinate provided
            (see more in settings documentation)
        """
        color = cls.getrgbcolor(coordinate.z)
        color.append(cls.OPACITYBEST)
        features = Features(cls.SIZEBEST, color, cls.BORDERCOLORBEST)
        res = Point(coordinate, features)
        return res

    @classmethod
    def getlocalbest(cls, coordinate):
        """
        :param coordinate (Coorindate): coordinate of the point in Cartesian space
        :return (Point): LOCALBEST point that corresponds to coordinate provided
            (see more in settings documentation)
        """
        color = cls.getrgbcolor(coordinate.z)
        color.append(cls.OPACITYLOCALBEST)
        features = Features(cls.SIZELOCALBEST, color, cls.BORDERCOLORLOCALBEST)
        res = Point(coordinate, features)
        return res

    @classmethod
    def getbad(cls, coordinate):
        """
        :param coordinate (Coorindate): coordinate of the point in Cartesian space
        :return (Point): LOCALBEST point that corresponds to coordinate provided
            (see more in settings documentation)
        """
        color = cls.getrgbcolor(coordinate.z)
        color.append(cls.OPACITYBAD)
        features = Features(cls.SIZEBAD, color, cls.BORDERCOLORBAD)
        res = Point(coordinate, features)
        return res

    @classmethod
    def gettor(cls, coordinate):
        """
        :param coordinate (Coorindate): coordinate of the point in Cartesian space
        :return (Point): TOR point that corresponds to coordinate provided
            (see more in settings documentation)
        """
        color = cls.FILLCOLORTOR
        features = Features(cls.SIZETOR, color, cls.BORDERCOLORTOR)
        res = Point(coordinate, features)
        return res
