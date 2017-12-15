class Point:
    idcounter = 0
    def __init__(self, x, y, z):
        self.id = Point.idcounter
        Point.idcounter += 1
        self.x = x
        self.y = y
        self.z = z