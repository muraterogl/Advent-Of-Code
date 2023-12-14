with open("input.txt") as f:
    grid = [list(line) for line in f.read().split("\n")]

h = len(grid)
w = len(grid[0])
# Sliding to north
for y in range(1, h):
    for x in range(w):
        if grid[y][x] == "O":
            for yy in range(y-1, -2, -1):
                if yy==-1 or grid[yy][x] in "O#":
                    grid[yy+1][x], grid[y][x] = grid[y][x], grid[yy+1][x]
                    break
# Count the load
part1 = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == "O":
            part1 += h-y

print("part 1:", part1)

with open("input.txt") as f:
    grid = [list(line) for line in f.read().split("\n")]
n = 0
shapes = {}
while n < 1_000_000_000:
    for k in range(2):
        for y in range(h):
            for x in range(w):
                if grid[y][x] == "O":
                    if k==0:
                        for yy in range(y-1, -2, -1):
                            if yy==-1 or grid[yy][x] in "O#":
                                grid[yy+1][x], grid[y][x] = grid[y][x], grid[yy+1][x]
                                break
                    else:
                        for xx in range(x-1, -2, -1):
                            if xx==-1 or grid[y][xx] in "O#":
                                grid[y][xx+1], grid[y][x] = grid[y][x], grid[y][xx+1]
                                break
    for k in range(2):
        for y in range(h-1, -1, -1):
            for x in range(w-1, -1, -1):
                if grid[y][x] == "O":
                    if k==0:
                        for yy in range(y+1, h+1):
                            if yy==h or grid[yy][x] in "O#":
                                grid[yy-1][x], grid[y][x] = grid[y][x], grid[yy-1][x]
                                break
                    else:
                        for xx in range(x+1, w+1):
                            if xx==w or grid[y][xx] in "O#":
                                grid[y][xx-1], grid[y][x] = grid[y][x], grid[y][xx-1]
                                break
    shape = "".join(["".join(line)for line in grid])
    if shape in shapes:
        prev_n = shapes[shape]
        diff = n - prev_n
        n = 1_000_000_000 - (1_000_000_000-n)%diff
    else:
        shapes[shape] = n
    n += 1
# Count the load
part2 = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == "O":
            part2 += h-y
print("part 2:", part2)
