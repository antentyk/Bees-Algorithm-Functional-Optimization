from numpy import exp, arange
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from functions import *

global FIGURE_ID
FIGURE_ID = 0


def get_figure_id():
    global FIGURE_ID
    FIGURE_ID += 1
    return FIGURE_ID


def get_XYZ(name, xrange, yrange, precision):
    xstart = xrange[0]
    xstop = xrange[1]
    xstep = 1 / precision
    ystart = yrange[0]
    ystop = yrange[1]
    ystep = 1 / precision
    x = arange(xstart, xstop, xstep)
    y = arange(ystart, ystop, ystep)
    X, Y = meshgrid(x, y)
    Z = name(X, Y)
    return X, Y, Z


def plot_3d(name, xrange, yrange, precision):
    fig = plt.figure(get_figure_id())
    ax = fig.gca(projection='3d')
    X, Y, Z = get_XYZ(name, xrange, yrange, precision)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot, linewidth=0)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    title(name.__name__.capitalize() + " function")


def plot2d_up(name, xrange, yrange, precision):
    fig1 = plt.figure(get_figure_id())
    X, Y, Z = get_XYZ(name, xrange, yrange, precision)
    im = imshow(Z, cmap=cm.hot)
    colorbar(im)
    title(name.__name__.capitalize() + " function")


def show_all_static(name, xrange, yrange, precision):
    plot2d_up(name, xrange, yrange, precision)
    plot_3d(name, xrange, yrange, precision)
    plt.show()

show_all_static(cross_in_tray, [-5, 5], [-10, 10], 10)
