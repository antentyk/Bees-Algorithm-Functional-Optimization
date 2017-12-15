import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib.animation import ImageMagickFileWriter


from functions import cross_in_tray
from Settings import Settings
from LocalController import LocalController
from PointsController import PointsController
from Point import Point


fig = plt.figure()
plt.xlim(Settings.XRANGE[0],
        Settings.XRANGE[1],)
plt.ylim(Settings.YRANGE[0],
        Settings.YRANGE[1],)
graph = plt.scatter([], [], cmap=Settings.COLORMAP)

c = LocalController(True,
                    PointsController(),
                    Settings,
                    Point(0, 0, cross_in_tray(0, 0)),
                    graph)


it = c.__iter__()

def animate(i):
    try:
        return it.__next__()
    except:
        return

# ___________
# SHOWING ANIMATION
# ___________

ani = FuncAnimation(fig, animate, repeat=False, interval=200)
plt.show()