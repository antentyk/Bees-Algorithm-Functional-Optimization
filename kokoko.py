import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

n = 5000
x = [random.random() for i in range(n)]
y = [random.random() for i in range(n)]
offsets = [[x[item], y[item]] for item in range(n)]
size = [20 for i in range(n)]
colors = [(random.random(), 0, 0) for i in range(n)]

fig = plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)
graph = plt.scatter([], [])

def animate(i):
    graph.set_offsets(offsets[:i+1])
    graph.set_sizes(size[:i+1])
    graph.set_facecolors(colors[:i+1])
    return graph

ani = FuncAnimation(fig, animate, repeat=False, interval=2)
plt.show()