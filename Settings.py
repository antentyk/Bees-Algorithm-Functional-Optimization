from pylab import cm
from functions import cross_in_tray
from Point import Point
from Features import Features
from ColoredPoint import ColoredPoint

class Settings:
    XRANGE = (-10, 10)
    YRANGE = (-10, 10)

    COLORMAP = cm.get_cmap('hot')

    SIZEBEST = 300
    SIZELOCALBEST = 100
    SIZEBAD = 10
    SIZETOR = 100000/2.54

    BORDERCOLORBEST = (0,0,0,0)
    BORDERCOLORLOCALBEST = (0,0,0,0)
    BORDERCOLORBAD = (0,0,0,0)
    BORDERCOLORTOR = (0,0,0,1)

    OPACITYBEST = 1
    OPACITYLOCALBEST = 1
    OPACITYBAD = 1

    FILLCOLORTOR = (0,0,0,0)

    BORDERWIDTH = 3

    BIGGESTOBSERVED = 1
    LOWESTOBSERVED = -3

    BEESNUM = 100
    ELITE = 10
    NONELITE = 5
    RECRUITEDELITE = 100
    RECRUITEDNONELITE = 20
    NGH = 1

    LOCALSKIPNUM = 10
    FUNC = cross_in_tray

    @classmethod
    def decideoncolor(cls, z):
        # returns RGB representation of the color
        percent = (z - cls.LOWESTOBSERVED) / (cls.BIGGESTOBSERVED - cls.LOWESTOBSERVED)
        percent = min(percent, 1 - (1e-9))
        percent = max(percent, 1e-9)
        color = cls.COLORMAP(percent)
        return list(color)[:3]

    @classmethod
    def getbest(cls, point):
        color = cls.decideoncolor(point.z)
        color.append(cls.OPACITYBEST)
        res = ColoredPoint(point, Features(cls.SIZEBEST,
                                           color,
                                           cls.BORDERCOLORBEST))
        return res

    @classmethod
    def getlocalbest(cls, point):
        color = cls.decideoncolor(point.z)
        color.append(cls.OPACITYLOCALBEST)
        res = ColoredPoint(point, Features(cls.SIZELOCALBEST,
                                           color,
                                           cls.BORDERCOLORLOCALBEST))
        return res

    @classmethod
    def getbad(cls, point):
        color = cls.decideoncolor(point.z)
        color.append(cls.OPACITYBAD)
        res = ColoredPoint(point, Features(cls.SIZEBAD,
                                           color,
                                           cls.BORDERCOLORBAD))
        return res

    @classmethod
    def gettor(cls, point):
        color = cls.FILLCOLORTOR
        res = ColoredPoint(point, Features(cls.SIZETOR,
                                           color,
                                           cls.BORDERCOLORTOR))
        return res