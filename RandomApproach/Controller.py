from Features import Features
from ColoredPoint import ColoredPoint

class Controller:
    def __init__(self, holder, settings):
        self.holder = holder
        self.settings = settings
        self.currentbestz = float('inf')
        self.currentbestid = -1

    def add(self, point):
        # ADDS POINT TO THE HOLDER AND UPDATES OTHER POINTS IF NECESSARY
        rgba = self.decideoncolor(point.z)
        if(point.z < self.currentbestz):
            if(self.currentbestid != -1):
                self.holder.changesize(self.currentbestid, self.settings.SIZEBAD)
                self.holder.changeopacity(self.currentbestid, self.settings.OPACITYBAD)
            rgba.append(self.settings.OPACITYGOOD)
            self.currentbestz = point.z
            self.currentbestid = point.id
            features = Features(self.settings.SIZEGOOD, rgba)
        else:
            rgba.append(self.settings.OPACITYBAD)
            features = Features(self.settings.SIZEBAD, rgba)
        self.holder.add(ColoredPoint(point, features))

    def decideoncolor(self, z):
        # RETURNS RGB REPRESENTATION ACCORDING TO COLOR MAP
        percent = (z - self.settings.LOWESTOBSERVED) / (self.settings.BIGGESTOBSERVED - self.settings.LOWESTOBSERVED)
        percent = min(percent, 1 - (1e-9))
        percent = max(percent, 1e-9)
        color = self.settings.COLORMAP(percent)
        return list(color)[:3]