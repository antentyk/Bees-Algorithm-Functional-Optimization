from pylab import cm
from Point import Point

colormap = cm.get_cmap('hot')

p1 = Point(-5, -10)
p2 = Point(5, 10)

badsize = 1
goodsize = 200

goodcolor = (1, 0, 0, 1)
badcolor = (0.1, 0.1, 0.1, 0.2)