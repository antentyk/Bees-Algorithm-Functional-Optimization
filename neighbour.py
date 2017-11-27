# improves result of the currentroute by seeking for neighbours

from copy import copy
from random import randint
from fitness import fitness
from constants import NGH

def neighbour(route, neighboursnum):
    result = fitness(route)
    for currentneighbour in range(neighboursnum):
        currentroute = copy(route)
        swapnum = randint(1, NGH)
        for i in range(swapnum):
            a = randint(0, len(currentroute) - 1)
            b = randint(0, len(currentroute) - 1)
            currentroute[a], currentroute[b] = currentroute[b], currentroute[a]
            result = min(result, fitness(currentroute))
    return result