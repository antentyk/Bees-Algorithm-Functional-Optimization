from math import cos, sin, exp, pi
import numpy as np


def shubert(x, y):
    sum1 = 0
    sum2 = 0
    for i in range(1, 6):
        new1 = i * np.cos((i + 1) * x + i)
        new2 = i * np.cos((i + 1) * y + i)
        sum1 += new1
        sum2 += new2
    return sum1 * sum2

def holder(x, y):
    # Global minimum - 19.2085
    fact1 = np.sin(x) * np.cos(y)
    fact2 = np.exp(abs(1 - (x ** 2 + y ** 2) ** 0.5 / pi))
    return - abs(fact1 * fact2)

def griewank(x, y):
    # Global minimum 0
    sum = x ** 2 / 4000 + y ** 2 / 4000
    prod = np.cos(x) * np.sin(y / 2 ** 0.5)
    return sum - prod + 1

def drop_wave(x, y):
    # Global minimum -1
    f1 = 1 + np.cos(12 * (x ** 2 + y ** 2) ** 0.5)
    f2 = 0.5 * (x ** 2 + y ** 2) + 2
    return -f1 / f2


def cross_in_tray(x, y):
    fact1 = np.sin(x) * np.sin(y)
    fact2 = np.exp(abs(100 - (x ** 2 + y ** 2) ** 0.5 / pi))
    return -0.0001 * (abs(fact1 * fact2) + 1) ** 0.1

def michaelewicz(x, y):
    t1 = np.sin(x) * ((np.sin(x ** 2 / pi)) ** 20)
    t2 = np.sin(y) * ((np.sin(2 * y ** 2 / pi)) ** 20)
    return  - t1 - t2

