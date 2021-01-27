
with open("day22.txt") as f:
    s = f.read().strip("\n")

s = s.split("\n\n")
p1 = s[0].split("\n")[1:]
p2 = s[1].split("\n")[1:]
p1 = list(map(int,p1))
p2 = list(map(int,p2))

while len(p1)>0 and len(p2)>0:
    p1a = p1.pop(0)
    p2a = p2.pop(0)
    if p1a > p2a:
        p1.extend([p1a,p2a])
    else:
        p2.extend([p2a,p1a])

print(sum((i+1)*v for i,v in enumerate(p1[::-1])))

p1 = s[0].split("\n")[1:]
p2 = s[1].split("\n")[1:]
p1 = list(map(int,p1))
p2 = list(map(int,p2))

# p1 win = True
def combat(p1,p2):
    seen = set()
    while len(p1)>0 and len(p2)>0:
        if (tuple(p1),tuple(p2)) in seen:
            return True
        seen.add((tuple(p1),tuple(p2)))
        p1a = p1.pop(0)
        p2a = p2.pop(0)
        if len(p1) >= p1a and len(p2) >= p2a:
            winner = combat(p1[:p1a], p2[:p2a])
            if winner:
                p1.extend([p1a,p2a])
            else:
                p2.extend([p2a,p1a])
        else:
            if p1a > p2a:
                p1.extend([p1a,p2a])
            else:
                p2.extend([p2a,p1a])
    return len(p1)>0

combat(p1,p2)
print(sum((i+1)*v for i,v in enumerate(p1[::-1])))
'''
pl1 = [24,
22,
26,
6,
14,
19,
27,
17,
39,
34,
40,
41,
23,
30,
36,
11,
28,
3,
10,
21,
9,
50,
32,
25,
8]
pl2 = [48,
49,
47,
15,
42,
44,
5,
4,
13,
7,
20,
43,
12,
37,
29,
18,
45,
16,
1,
46,
38,
35,
2,
33,
31]
x = len(pl1) - 1
while True:
    try:
        if pl1[0] > pl2[0]:
            z = pl1[0]
            pl1.remove(z)
            pl1.append(z)
            y = pl2[0]
            pl2.remove(y)
            pl1.append(y)
        elif len(pl1) == 0 or len(pl2) == 0:
            break
        elif pl1[0] < pl2[0]:
            z = pl2[0]
            pl2.remove(z)
            pl2.append(z)
            y = pl1[0]
            pl1.remove(y)
            pl2.append(y)
        else:
            break
    except IndexError:
        break
print(pl1,'pl2: ',pl2)
print(sum((i+1)*v for i,v in enumerate(pl1[::-1])))'''