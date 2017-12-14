import math
import random


bound = (-5, 10)
dimension = 2

def shubert(x):
    res = 1
    for item in x:
        current = sum([i * math.cos((i + 1) * item + i) for i in range(1, 6)])
        res *= current
    return res
def schwefel(x):
    return 418.9829 * dimension - sum([item * math.sin(abs(item) ** 0.5) for item in x])
def zakharov(x):
    res = 0
    res += sum([item**2 for item in x])
    res += sum([(i + 1) * item / 2 for i, item in enumerate(x)]) ** 2
    res += sum([(i + 1) * item / 2 for i, item in enumerate(x)]) ** 4
    return res

def gennumber():
    res = random.randint(bound[0], bound[1])
    res += random.random()
    if(res < bound[0]):res += 1
    if(res > bound[1]):res -= 1
    return res

def genvector():
    return [gennumber() for i in range(dimension)]

currentmin = float('inf')
for i in range(10**5):
    current = zakharov(genvector())
    currentmin = min(currentmin, current)

print(currentmin)
