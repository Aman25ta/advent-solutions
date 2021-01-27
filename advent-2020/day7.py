import collections
import math
import re
import fileinput

lines = list(fileinput.input('day7.txt'))

contin = collections.defaultdict(set)
contains = collections.defaultdict(list)
for line in lines:
    color = re.match(r'(.+?) bags contain', line)[1]
    for ct, innercolor in re.findall(r'(\d+) (.+?) bags?[,.]', line):
        ct = int(ct)
        contin[innercolor].add(color)
        contains[color].append((ct, innercolor))
hg = set()
def check(color):
    for c in contin[color]:
        hg.add(c)
        check(c)
check('shiny gold')
print('Part 1: ' , len(hg))
def cost(color):
    total = 0
    for ct, inner in contains[color]:
        total += ct
        total += ct * cost(inner)
    return total
print('Part 2: ' , cost('shiny gold'))