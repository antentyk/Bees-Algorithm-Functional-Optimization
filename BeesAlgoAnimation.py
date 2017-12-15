import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib.animation import ImageMagickFileWriter


from Settings import Settings
from Controller import Controller


fig = plt.figure()
plt.xlim(Settings.XRANGE[0],
        Settings.XRANGE[1],)
plt.ylim(Settings.YRANGE[0],
        Settings.YRANGE[1],)
graph = plt.scatter([], [], cmap=Settings.COLORMAP)

c = Controller(graph, Settings)

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