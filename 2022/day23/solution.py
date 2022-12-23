from collections import Counter

with open("input.txt") as f:
    lines= f.read().split("\n")

elves = set()

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            elves.add((y,x))

way = [([(-1,0),(-1,-1),(-1,1)],(-1,0)), ([(1,0),(1,-1),(1,1)],(1,0)), ([(1,-1),(0,-1),(-1,-1)],(0,-1)), ([(1,1),(0,1),(-1,1)],(0,1))]

for round in range(10**12):
    moves = {}
    for ey,ex in elves:
        if all((ey+dy,ex+dx) not in elves for dy,dx in [(-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)]):
            continue
        if all((ey+dy,ex+dx) not in elves for dy,dx in way[0][0]):
            moves[(ey,ex)] = ey+way[0][1][0],ex+way[0][1][1]
        elif all((ey+dy,ex+dx) not in elves for dy,dx in way[1][0]):
            moves[(ey,ex)] = ey+way[1][1][0],ex+way[1][1][1]
        elif all((ey+dy,ex+dx) not in elves for dy,dx in way[2][0]):
            moves[(ey,ex)] = ey+way[2][1][0],ex+way[2][1][1]
        elif all((ey+dy,ex+dx) not in elves for dy,dx in way[3][0]):
            moves[(ey,ex)] = ey+way[3][1][0],ex+way[3][1][1]
    dests = Counter(moves.values())
    for elf, d in moves.items():
        if dests[d] == 1:
            elves -= {elf}
            elves |= {d}

    way = way[1:] + [way[0]]
    if round == 10:
        max_y = max(y for y,_ in elves)
        max_x = max(x for _,x in elves)
        min_y = min(y for y,_ in elves)
        min_x = min(x for _,x in elves)
        result = 0
        for y in range(min_y, max_y+1):
            for x in range(min_x, max_x+1):
                if not (y,x) in elves:
                    result += 1 
        print(f"Part1: {result}")
    if moves == {}:
        print(f"Part2: {round+1}")
        break
