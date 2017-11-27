from copy import copy
from random import shuffle
from os import system

from constants import *
from data import data as samples
from fitness import fitness
from neighbour import neighbour

cities = samples[0]["cities"]
n = len(cities)

result = float('inf')

iterationcounter = 0

while(SCOUTBEES > 0):
    iterationcounter += 1
    situation = []
    for fly in range(SCOUTBEES):
        route = copy(cities)
        situation.append((fitness(route), route))
    situation.sort(key=lambda x: x[0])
    for i in range(min(len(situation), ELITE)):
        result = min(result, neighbour(situation[i][1], RECRUITEDELITE))
    for j in range(NONELITE):
        i = ELITE + j
        if(i >= len(situation)):break
        result = min(result, neighbour(situation[i][1], RECRUITEDNONELITE))
    SCOUTBEES -= (ELITE + NONELITE)
    system('cls')
    print("iteration", iterationcounter)
    print(result)

print("Result", result)