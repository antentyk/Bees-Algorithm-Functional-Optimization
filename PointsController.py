class PointsController:
    def __init__(self):
        self.offsets = []
        self.sizes = []
        self.colors = []
        self.borders = []
        self.position = {}
    def add(self, coloredpoint):
        self.offsets.append([coloredpoint.point.x, coloredpoint.point.y])
        self.sizes.append(coloredpoint.features.size)
        self.colors.append(coloredpoint.features.color)
        self.borders.append(coloredpoint.features.border)
        self.position[coloredpoint.point.id] = len(self.offsets) - 1
    def getposition(self, pointid):
        return self.position[pointid]
    def pop(self, num):
        # print(len(self.offsets))
        self.offsets = self.offsets[:-num]
        # print(len(self.offsets))
        self.sizes = self.sizes[:-num]
        self.colors = self.colors[:-num]
        self.borders = self.borders[:-num]
    def clear(self):
        self.offsets = []
        self.sizes = []
        self.colors = []
        self.borders = []
        self.position = {}
    def swap(self, id1, id2):
        i1 = self.getposition(id1)
        i2 = self.getposition(id2)
        self.offsets[i1], self.offsets[i2] = self.offsets[i2], self.offsets[i1]
        self.sizes[i1], self.sizes[i2] = self.sizes[i2], self.sizes[i1]
        self.colors[i1], self.colors[i2] = self.colors[i2], self.colors[i1]
        self.borders[i1], self.borders[i2] = self.borders[i2], self.borders[i1]
        self.position[id1] = i2
        self.position[id2] = i1
    def changesize(self, pointid, newsize):
        i = self.getposition(pointid)
        self.sizes[i] = newsize
    def changecolor(self, pointid, newcolor):
        i = self.getposition(pointid)
        self.colors[i] = newcolor
    def set(self, graph):
        graph.set_offsets(self.offsets)
        graph.set_sizes(self.sizes)
        graph.set_facecolors(self.colors)
        graph.set_edgecolor(self.borders)