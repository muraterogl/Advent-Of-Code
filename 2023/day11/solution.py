with open("input.txt") as f:
    lines = [list(line) for line in f.read().split("\n")]
h = len(lines)
w = len(lines[0])
empty_rows = [i for i in range(h) if all(c=="." for c in lines[i])]
empty_columns = [i for i in range(w) if all(lines[j][i]=="." for j in range(h))]
#find the galaxies
galaxies = []
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c=="#":
            galaxies.append((y, x))

def calculate_total_distance(empty_scale):
    result = 0
    for y1, x1 in galaxies:
        for y2, x2 in galaxies:
            y11, y22 = sorted([y1, y2])
            x11, x22 = sorted([x1, x2])
            result += y22-y11 + (empty_scale-1) * sum(y11<y<y22 for y in empty_rows) + \
                      x22-x11 + (empty_scale-1) * sum(x11<x<x22 for x in empty_columns)
    return result//2

print("part 1:", calculate_total_distance(2))
print("part 2:", calculate_total_distance(1_000_000))
