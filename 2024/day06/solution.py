with open("input.txt") as f:
    lines = f.read().split("\n")
obstacles = set()
guard_start_x = guard_start_y = guard_start_dir = guard_x = guard_y = guard_dir = -1
part1 = part2 = 0
visited = set()
potential_points = set()
h = len(lines)
w = len(lines[0])
for y in range(h):
    for x in range(w):
        if lines[y][x] == "#":
            obstacles.add((y,x))
        elif lines[y][x] == "^":
            guard_start_x = guard_x = x
            guard_start_y = guard_y = y
            guard_start_dir = guard_dir = 0
            visited.add((y,x))

while 0 <= guard_y < h and 0 <= guard_x < w:
    dy, dx = [(-1,0),(0,1),(1,0),(0,-1)][guard_dir]
    if (dy+guard_y, dx+guard_x) in obstacles:
        guard_dir = (guard_dir+1)%4
    else:
        guard_y += dy
        guard_x += dx
        visited.add((guard_y, guard_x))
visited.remove((guard_y, guard_x))

for y, x in visited:
    for yy, xx in [(-1,0),(0,1),(1,0),(0,-1)]:
        if 0 <= y+yy < h and 0 <= x+xx < w and lines[y+yy][x+xx] != "#" and (y+yy, x+xx) not in potential_points:
            t_y, t_x = y+yy, x+xx
            guard_y, guard_x, guard_dir = guard_start_y, guard_start_x, guard_start_dir
            current_visited = set()
            while 0 <= guard_y < h and 0 <= guard_x < w:
                dy, dx = [(-1,0),(0,1),(1,0),(0,-1)][guard_dir]
                if (dy+guard_y, dx+guard_x) in obstacles or (dy+guard_y==t_y and dx+guard_x==t_x):
                    guard_dir = (guard_dir+1)%4
                else:
                    guard_y += dy
                    guard_x += dx
                if (guard_y, guard_x, guard_dir) in current_visited:
                    potential_points.add((t_y, t_x))
                    break
                current_visited.add((guard_y, guard_x, guard_dir))

part1 = len(visited)
part2 = len(potential_points)
print(part1, part2)
