from itertools import combinations

with open("input.txt") as f:
    lines = f.read().split("\n")
h = len(lines)
w = len(lines[0])
part1 = part2 = 0
antennas = defaultdict(set)
antinodes = set()
antinodes2 = set()
for y in range(h):
    for x in range(w):
        if lines[y][x] != ".":
            antennas[lines[y][x]].add((y,x))

for _, locations in antennas.items():
    for ((y1,x1), (y2,x2)) in combinations(locations, 2):
        dy = y1-y2
        dx = x1-x2
        for i in range(50):
            for y,x in (y1+i*dy, x1+i*dx), (y2-i*dy, x2-i*dx):
                if 0 <= y < h and 0 <= x < w:
                    if i==1:
                        antinodes.add((y,x))
                    antinodes2.add((y,x))
part1 = len(antinodes)
part2 = len(antinodes2)
print(part1, part2)
