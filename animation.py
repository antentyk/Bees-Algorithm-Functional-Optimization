import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.arange(10)
y = np.random.random(10)
size = np.random.randint(150, size=10)
colors = np.random.choice(["r", "g", "b"], size=10)

fig = plt.figure()
plt.xlim(0, 10)
plt.ylim(0, 1)
graph = plt.scatter([], [])

def animate(i):
    graph.set_offsets(np.vstack((x[:i+1], y[:i+1])).T)
    graph.set_sizes(size[:i+1])
    graph.set_facecolors(colors[:i+1])
    return graph

ani = FuncAnimation(fig, animate, repeat=False, interval=200)
plt.show()