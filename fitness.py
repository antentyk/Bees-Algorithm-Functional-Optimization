# evaluates fitness of the population

from distance import distance as d

def fitness(route):
    result = 0
    for i in range(1, len(route)):
        result += d(route[i], route[i - 1])
    result += d(route[0], route[-1])
    return result