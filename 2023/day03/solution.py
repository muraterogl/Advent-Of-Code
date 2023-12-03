import math

with open("input.txt") as f:
    lines = f.read().split("\n")

h = len(lines)
w = len(lines[0])
numbers = {}
id_to_number = []
part1 = 0
part2 = 0
n = ""
n_id = 0
has_neigh = False
for y in range(h):
    for x in range(w):
        if lines[y][x].isdigit():
            if not has_neigh:
                def check_neigh(yy, xx):
                    return not lines[yy][xx].isdigit() and lines[yy][xx] != "."
                #left part
                if n=="":
                    for i in range(max(0, y-1), min(h,y+2)):
                        for j in range(max(0, x-1), x+1):
                            if check_neigh(i, j):
                                has_neigh = True
                #right part
                if x==w-1 or not lines[y][x+1].isdigit():
                    for i in range(max(0, y-1), min(h,y+2)):
                        for j in range(x, min(w, x+2)):
                            if check_neigh(i, j):
                                has_neigh = True
                #middle
                elif n!="":
                    if check_neigh(max(0, y-1), x) or check_neigh(min(h-1, y+1), x):
                       has_neigh = True
            n += lines[y][x]
            numbers[(y,x)] = n_id

            if x==w-1 or not lines[y][x+1].isdigit():
                id_to_number.append(int(n))
                if has_neigh:
                    part1 += int(n)
                n = ""
                n_id += 1
                has_neigh = False
print(part1)

for y in range(h):
    for x in range(w):
        if lines[y][x] == "*":
            ids = []
            for i in range(max(0, y-1), min(h, y+2)):
                for j in range(max(0, x-1), min(w, x+2)):
                    if (i, j) in numbers:
                        ids.append(numbers[(i, j)])
            ids = [id_to_number[index] for index in {*ids}]
            if len(ids) == 2:
                part2 += math.prod(ids)

print(part2)
