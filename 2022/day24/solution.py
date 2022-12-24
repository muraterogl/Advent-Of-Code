from collections import defaultdict
from copy import deepcopy

with open("input.txt") as f:
    lines= f.read().split("\n")

h = len(lines)-2
w = len(lines[1])-2
next_bstate = {}
bstate_to_blizzard = {}

def bstate(blizzards):
    d = {(0,1):">",(0,-1):"<",(1,0):"v",(-1,0):"^"}
    result = ""
    for i in range(w):
        if (0,i) in blizzards:
            if len(blizzards[(0,i)])<2:
                result += d[blizzards[(0,i)][0]]
            else:
                result += str(len(blizzards[(0,i)]))
        else:
            result += "."
    return result

def draw(position, blizzard):
    r = ""
    for y in range(h):
        for x in range(w):
            if (y,x) in blizzard:
                if len(blizzard[(y,x)])>1:
                    r += str(len(blizzard[(y,x)]))
                else:
                    r += {(0,1):">",(0,-1):"<",(1,0):"v",(-1,0):"^"}[blizzard[(y,x)][0]]
            elif (y,x)==position:
                r += "E"
            else:
                r += "."
        r += "\n"
    return r

def shortest_time(position, destination, b):
    queue = [(position, b, 0)]
    seen = set()
    while queue:
        p, b, step = queue.pop(0)
        if p == destination:
            return b, step
        if (p,b) in seen:
            continue
        seen.add((p,b))
        blizzard = bstate_to_blizzard[next_bstate[b]]
        for dy,dx in (0,0),(-1,0),(1,0),(0,1),(0,-1):
            y,x = p
            if not ((y+dy,x+dx),next_bstate[b]) in seen:
                if (0<=y+dy<h and 0<=x+dx<=w and (y+dy,x+dx) not in blizzard) or (y+dy,x+dx) in ((-1,0),(h,w-1)):
                    queue.append(((y+dy,x+dx),next_bstate[b],step+1))



blizzards = defaultdict(list)
for y in range(h+2):
    for x in range(w+2):
        if lines[y][x] == ">":
            blizzards[(y-1,x-1)].append((0,1))
        elif lines[y][x] == "v":
            blizzards[(y-1,x-1)].append((1,0))
        elif lines[y][x] == "<":
            blizzards[(y-1,x-1)].append((0,-1))
        elif lines[y][x] == "^":
            blizzards[(y-1,x-1)].append((-1,0))
init_bstate = bstate(blizzards)

while not bstate(blizzards) in next_bstate:
    b = defaultdict(list)
    bstate_to_blizzard[bstate(blizzards)] = deepcopy(blizzards)
    for (y,x),d in blizzards.items():
        for dy,dx in d:
            b[((y+dy)%h,(x+dx)%w)].append((dy,dx))
    next_bstate[bstate(blizzards)] = bstate(b)
    blizzards = deepcopy(b)


b, step = shortest_time((-1,0), (h,w-1), init_bstate)
print(f"Part1: {step}")
part2 = step
b, step = shortest_time((h,w-1),(-1,0),b)
part2 += step
b, step = shortest_time((-1,0),(h,w-1),b)
part2 += step
print(f"Part2: {part2}")
