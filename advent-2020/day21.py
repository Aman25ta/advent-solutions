import sys
import regex

s = open('day21.txt').read()

import sys
import math
import re
import numpy as np
import functools as ft
import itertools as its

from copy import deepcopy
from collections import defaultdict

if len(sys.argv) < 2:
    INPUT_FILE = "day21.txt"
else:
    INPUT_FILE = sys.argv[1]


def toFood(line):
    ingr, allerg = line.split(" (contains ")

    ingr = ingr.split(" ")
    allerg = allerg.rstrip(")").split(", ")

    return [set(ingr), allerg]


data = open(INPUT_FILE).read().rstrip()
data = [toFood(line) for line in data.split("\n")]

allergens = {}
allIngr = defaultdict(lambda: 0)

for ingr, allergs in data:
    for ing in ingr:
        allIngr[ing] += 1

    for allerg in allergs:
        if allerg not in allergens:
            allergens[allerg] = ingr.copy()
        else:
            allergens[allerg] = allergens[allerg].intersection(ingr)


notAllerg = set(allIngr.keys())
for allerg in allergens:
    cur = allergens[allerg]

    notAllerg = notAllerg.difference(cur)

count = 0
for nota in notAllerg:
    count += allIngr[nota]

# Part 1:
print(count)

ok = False
while not ok:
    ok = True

    for allerg in allergens:
        cur = allergens[allerg]
        count = len(cur)

        if count > 1:
            ok = False
        else:
            for a2 in allergens:
                if allerg == a2:
                    continue
                allergens[a2] = allergens[a2].difference(cur)

# Part 2:
print(",".join(map(lambda x: next(iter(x[1])), sorted(allergens.items()))))

