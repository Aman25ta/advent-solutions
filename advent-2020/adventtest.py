import datetime as dt
start_time = dt.datetime.now()
info = []
x = 0
tree = 0
rows = 323
y = 31


data = open("day3.txt", "r")
for r in range(rows):
    text = data.readline()
    entry = text.replace("\n","")
    info.append(entry)


for i in range(rows):
    x = (x+3)
    if i == 0:
        x = 0
    if x >= y:
        x = x-y
    current = info[i]
    #print(i)
    #print(current)
    #print(x)
    if x < y:
        if current[x] == "#":
            tree += 1
    if x == y:
        temp = x-1
        if current[temp] == "#":
            tree += 1
print(tree)    




end_time = dt.datetime.now()
time_diff = end_time - start_time
print(f'Duration:{time_diff}')