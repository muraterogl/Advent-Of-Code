with open("input.txt") as f:
    lines = f.read().split("\n")
part1 = part2 = 0
byte_count = 1024
limit = 70
corrupted = set()
for line in lines[:byte_count]:
    x,y = map(int,line.split(","))
    corrupted.add((y,x))

def find_path(corrupted):
    q = [(0, 0, 0)]
    seen = {}
    while q:
        cy, cx, cl = q.pop(0)
        if (cy, cx) == (limit, limit):
            return cl
        if (cy, cx) in seen and seen[(cy, cx)] <= cl:
            continue
        seen[(cy,cx)] = cl
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            y = cy+dy
            x = cx+dx
            if 0<=y<=limit and 0<=x<=limit and (y,x) not in corrupted:
                q += (y, x, cl+1),
    return None

part1 = find_path(corrupted)

for line in lines[byte_count:]:
    x,y = map(int,line.split(","))
    corrupted.add((y,x))
    path = find_path(corrupted)
    if not path:
        part2 = f"{x},{y}"
        break

print(part1, part2)
