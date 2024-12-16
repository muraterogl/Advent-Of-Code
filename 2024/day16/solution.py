with open("input.txt") as f:
    lines = f.read().split("\n")
part1 = 999999999
part2 = set()
h = len(lines)
w = len(lines[0])
S = (-1, -1)
E = (-1, -1)
for y in range(h):
    for x in range(w):
        if lines[y][x] == "S":
            S = (y, x)
        elif lines[y][x] == "E":
            E = (y, x)
seen = {}
q = [(S[0], S[1], 0, 0, [S])]
while q:
    cy, cx, cw, cs, cc = q.pop()
    if (cy, cx) == E:
        if cs < part1:
            part1 = cs
            part2 = set(cc)
        elif cs == part1:
            part2 |= set(cc)
        continue
        
    if (cy, cx, cw) in seen and seen[(cy, cx, cw)] < cs:
        continue

    seen[cy,cx,cw] = cs

    if cw != 2 and cx < w-1 and lines[cy][cx+1] != "#":
        if cw == 0:
            q += (cy, cx+1, 0, cs+1, cc+[(cy, cx+1)]),
        else:
            q = [(cy, cx+1, 0, cs+1001, cc+[(cy, cx+1)])] + q
    if cw != 3 and cy < h-1 and lines[cy+1][cx] != "#":
        if cw == 1:
            q += (cy+1, cx, 1, cs+1, cc+[(cy+1, cx)]),
        else:
            q = [(cy+1, cx, 1, cs+1001, cc+[(cy+1, cx)])] + q
    if cw != 0 and cx > 0 and lines[cy][cx-1] != "#":
        if cw == 2:
            q += (cy, cx-1, 2, cs+1, cc+[(cy, cx-1)]),
        else:
            q = [(cy, cx-1, 2, cs+1001, cc+[(cy, cx-1)])] + q
    if cw != 1 and cy > 0 and lines[cy-1][cx] != "#":
        if cw == 3:
            q += (cy-1, cx, 3, cs+1, cc+[(cy-1, cx)]),
        else:
            q = [(cy-1, cx, 3, cs+1001, cc+[(cy-1, cx)])] + q

for y in range(h):
    print("".join(["O" if (y,x) in part2 else lines[y][x]for x in range(w)]))
part2 = len(part2)
print(part1, part2)
