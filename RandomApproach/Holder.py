class Holder:
    def __init__(self):
        self.offsets = []
        self.sizes = []
        self.colors = []
    def add(self, coloredpoint):
        self.offsets.append([coloredpoint.point.x,
                             coloredpoint.point.y])
        self.sizes.append(coloredpoint.features.size)
        self.colors.append(coloredpoint.features.color)
    def changesize(self, pointid, newsize):
        self.sizes[pointid] = newsize
    def changeopacity(self, pointid, newopacity):
        self.colors[pointid][-1] = newopacity