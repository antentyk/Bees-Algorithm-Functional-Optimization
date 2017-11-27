# returns kth permutations of sequence of numbers from
# 0 to n - 1 inclusive
# (k is in range[0; n! - 1])

from math import factorial
from copy import copy

def getkthpermutation(n, k):
    global result
    global seq
    result = []
    seq = list(range(n))
    get(copy(seq), k)
    return copy(result)

def get(currentlist, k):
    if (len(currentlist) == 0): return
    prev = factorial(len(currentlist) - 1)
    current = 0
    while (current * prev <= k):
        current += 1
    current -= 1
    global result
    result.append(currentlist[current])
    currentlist.remove(currentlist[current])
    k -= current * prev
    get(currentlist, k)
