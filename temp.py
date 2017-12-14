import matplotlib
import matplotlib.pyplot as plt
import random


fig, ax = plt.subplots()

ax.set_facecolor('black')

for i in range(300):
    x = random.random()
    y = random.random()
    c = random.random()
    color = (c, 0, 0)
    ax.plot(x, y, 'o-', color=color, ms=3)
plt.show()