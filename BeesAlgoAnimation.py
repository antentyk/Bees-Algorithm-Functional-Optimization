import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
from matplotlib.animation import ImageMagickFileWriter


from Settings import Settings
from Controller import Controller

# _____________
# WON'T WORK ON YOUR MACHINE UNLESS YOU INSTALL ImageMagick
# _____________

matplotlib.verbose.set_level("helpful")
plt.rcParams['animation.convert_path'] = 'C:\\Program Files\\ImageMagick-7.0.7-Q16\\magick.exe'
matplotlib.rcParams['animation.ffmpeg_path'] = 'C:\\ffmpeg\\bin\\ffmpeg.exe'

# _____________
# _____________
# _____________


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

if (__name__ != '__main__'):
    ani = FuncAnimation(fig, animate, repeat=False, interval=10, frames=500)
    plt.show()

# ___________
# SAVING TO GIF
# ___________

else:
    ani = FuncAnimation(fig, animate, repeat=False, interval=2, frames=100)
    ani.save('line.gif', writer=ImageMagickFileWriter())
