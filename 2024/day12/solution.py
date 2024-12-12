from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().split("\n")
part1 = part2 = 0

h = len(lines)
w = len(lines[0])
seen = set()
for y in range(h):
    for x in range(w):
        if (y,x) not in seen:
            perimeter = 0
            area = 0
            sides = defaultdict(list)
            side_count = 0
            q = [(y,x)]
            while q:
                cy,cx = q.pop(0)
                if (cy,cx) not in seen:
                    seen.add((cy,cx))
                    area += 1
                    p = 4
                    possible_sides = set([*'NESW'])
                    if cy>0 and lines[y][x] == lines[cy-1][cx]:
                        if (cy-1, cx) not in seen: q += (cy-1, cx),
                        p -= 1
                        possible_sides.remove('N')
                    if cy<h-1 and lines[y][x] == lines[cy+1][cx]:
                        if (cy+1, cx) not in seen: q += (cy+1, cx),
                        p -= 1
                        possible_sides.remove('S')
                    if cx>0 and lines[y][x] == lines[cy][cx-1]:
                        if (cy, cx-1) not in seen: q += (cy, cx-1),
                        p -= 1
                        possible_sides.remove('W')
                    if cx<w-1 and lines[y][x] == lines[cy][cx+1]:
                        if (cy, cx+1) not in seen: q += (cy, cx+1),
                        p -= 1
                        possible_sides.remove('E')
                    for side in possible_sides:
                        sides[side].append((cy,cx))
                    perimeter += p
            for s in "SN":
                sides[s].sort(key=lambda x: [x[0],x[1]])
                groups = []
                for cy, cx in sides[s]:
                    not_found = True
                    for group in groups:
                        if (cy,cx+1) in group or (cy,cx-1) in group:
                            group.append((cy,cx))
                            not_found = False
                    if not_found:
                        groups.append([(cy,cx)])
                side_count += len(groups)
            for s in "WE":
                sides[s].sort(key=lambda x: [x[1],x[0]])
                groups = []
                for cy, cx in sides[s]:
                    not_found = True
                    for group in groups:
                        if (cy+1,cx) in group or (cy-1,cx) in group:
                            group.append((cy,cx))
                            not_found = False
                    if not_found:
                        groups.append([(cy,cx)])
                side_count += len(groups)
            part1 += area * perimeter
            part2 += area * side_count


print(part1, part2)
