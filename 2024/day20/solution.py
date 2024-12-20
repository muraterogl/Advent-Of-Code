with open("input.txt") as f:
    lines = f.read().split("\n")
part1 = part2 = 0
h = len(lines)
w = len(lines[0])
start = None
end = None
walls = set()
road = []
for y in range(h):
    for x in range(w):
        if lines[y][x] == "S":
            start = (y, x)
            road.append((y,x))
        elif lines[y][x] == "E":
            end = (y, x)
            road.append((y,x))
        elif lines[y][x] == "#":
            walls.add((y, x))
        else:
            road.append((y,x))

default_finishes = {}

def find_finishes(cheating_allowed, cheating_time=2, limit=99999999999999):
    q = [(start[0], start[1], 0, False)]
    seen = set()
    finishes = []
    while q:
        cy, cx, cs, cheated = q.pop()
        if (cy, cx) in seen:
            continue
        if not cheating_allowed:
            default_finishes[(cy,cx)] = cs
        if (cy, cx) == end:
            finishes += cs,
            continue
        seen.add((cy,cx))
        for dy, dx in [(-1,0),(1,0),(0,1),(0,-1)]:
            y, x = cy+dy, cx+dx
            if 0<=y<h and 0<=x<w and (y,x) not in walls:
                q += (y, x, cs+1, cheated),
        if cheating_allowed and not cheated:
            for ry, rx in road:
                current_cheating_time = abs(ry-cy) + abs(rx-cx)
                ns = cs + current_cheating_time
                if current_cheating_time <= cheating_time and default_finishes[(ry,rx)]-ns >= 100:
                    finishes += limit - (default_finishes[(ry,rx)]-ns),

    return finishes

default = find_finishes(False)[0]
print("default:", default)
part1 = len(find_finishes(True, 2, default))-1
part2 = len(find_finishes(True, 20, default))-1
print(part1, part2)
