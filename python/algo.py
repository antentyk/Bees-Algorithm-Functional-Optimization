import random
import copy
import os

from data import data as samples

scout_bees = 50000
elite = 20
non_elite = 50
recruited_elite = 500
recruited_non_elite = 300
max_delta = 5

def d(coord1, coord2):
    return ((coord2[0] - coord1[0]) ** 2 +
            (coord2[1] - coord1[1]) ** 2)**0.5

def fitness(route):
    result = 0
    for i in range(1, len(route)):
        result += d(route[i], route[i - 1])
    result += d(route[-1], route[0])
    return result

def find(cities):
    answer = float('inf')
    global scout_bees
    counter = 0
    while(scout_bees > 0):
        counter += 1
        itanswer = iteration(copy.copy(cities))
        answer = min(answer, itanswer)
        scout_bees -= (elite + non_elite)
        os.system('cls')
        print("Iteration:", counter)
        print("Current iteration result:", itanswer)
        print("Global minimum:", answer)
    return answer

def iteration(citiesinitial):
    answer = float('inf')
    situation = []
    for i in range(scout_bees):
        cities = copy.copy(citiesinitial)
        random.shuffle(cities)
        situation.append((fitness(cities), copy.copy(cities)))
    situation.sort()
    for i in range(min(elite, len(situation))):
        answer = min(answer, find_best_neighbour(situation[i][1], recruited_elite))
    for i in range(non_elite):
        if(i + elite >= len(situation)):break
        answer = min(answer, find_best_neighbour(situation[i + elite][1], recruited_non_elite))
    return answer

def find_best_neighbour(route, size):
    result = fitness(route)
    for asd in range(size):
        current = copy.copy(route)
        swapnum = max_delta
        for it in range(swapnum):
            i = random.randint(0, len(route) - 1)
            j = random.randint(0, len(route) - 1)
            current[i], current[j] = current[j], current[i]
        result = min(result, fitness(current))
    return result

cities = sorted(list(map(tuple, samples[1]["cities"])))
print(find(cities))
print("Benchmark:", samples[1]["length"])