from math import factorial
from getkthpermutation import getkthpermutation

def formlineardeviation(n, step):
    f = factorial(n)
    current = 0
    while(current <= 1):
        currentk = current * (f - 1)
        print(getkthpermutation(n, currentk))
        current += step

# formlineardeviation(100, 0.0001)