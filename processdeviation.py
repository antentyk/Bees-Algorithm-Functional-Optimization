from neighbour import neighbour
from os import system
from constants import RECRUITEDELITE
from data import data as samples
from sys import exit

cities = samples[0]["cities"]

result = float('inf')

try:
    iterationcounter = 0
    while(True):
        route = eval(input())
        route = [cities[item] for item in route]
        result = int(min(result, neighbour(route, RECRUITEDELITE)))
        system('cls')
        iterationcounter += 1
        print('Iteration', iterationcounter)
        print(result)
except Exception as e:
    pass

print("Result", result)