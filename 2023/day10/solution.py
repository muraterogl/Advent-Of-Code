with open("input.txt") as f:
    lines = f.read().split("\n")

part1=0
x=y=-1
h=len(lines)
w=len(lines[0])
for j, line in enumerate(lines):
    for i, c in enumerate(line):
        if c == "S":
            x=i
            y=j
            break

q = []
seen = set([(y, x)])
horizontal = {}
vertical = {}
minx=miny=1e9
maxx=maxy=-1e9
potential_S = set(["|","-","L","J","7","F"])
# Finding the first coordinates in path
if y!=0 and lines[y-1][x] in "7|F":
    potential_S = potential_S & {"|","L","J"}
    q.append((y-1, x, 1))
if y!=h-1 and lines[y+1][x] in "|LJ":
    potential_S = potential_S & {"|","7","F"}
    q.append((y+1, x, 1))
if x!=0 and lines[y][x-1] in "-LF":
    potential_S = potential_S & {"-","J","7"}
    q.append((y, x-1, 1))
if x!=w-1 and lines[y][x+1] in "-J7":
    potential_S = potential_S & {"-","L","F"}
    q.append((y, x+1, 1))
potential_S = [*potential_S][0]
while q:
    yc, xc, lc = q.pop(0)
    if (yc, xc) not in seen and lines[yc][xc] not in "S.":
        part1 = max(part1, lc)
        seen.add((yc, xc))
        if yc in vertical:
            vertical[yc].append(xc)
        else:
            vertical[yc]=[xc]
        if xc in horizontal:
            horizontal[xc].append(yc)
        else:
            horizontal[xc]=[yc]
        minx = min(minx, xc)
        miny = min(miny, yc)
        maxx = max(maxx, xc)
        maxy = max(maxy, yc)

        if lines[yc][xc] == "|":
            if yc>0 and lines[yc-1][xc] in "|7F":
                q.append((yc-1, xc, lc+1))
            if yc<h-1 and lines[yc+1][xc] in "|LJ":
                q.append((yc+1, xc, lc+1))
        elif lines[yc][xc] == "-":
            if xc>0 and lines[yc][xc-1] in "-LF":
                q.append((yc, xc-1, lc+1))
            if xc<w-1 and lines[yc][xc+1] in "-J7":
                q.append((yc, xc+1, lc+1))
        elif lines[yc][xc] == "L":
            if yc>0 and lines[yc-1][xc] in "|7F":
                q.append((yc-1, xc, lc+1))
            if xc<w-1 and lines[yc][xc+1] in "-J7":
                q.append((yc, xc+1, lc+1))
        elif lines[yc][xc] == "J":
            if yc>0 and lines[yc-1][xc] in "|7F":
                q.append((yc-1, xc, lc+1))
            if xc>0 and lines[yc][xc-1] in "-LF":
                q.append((yc, xc-1, lc+1))
        elif lines[yc][xc] == "7":
            if yc<h-1 and lines[yc+1][xc] in "|LJ":
                q.append((yc+1, xc, lc+1))
            if xc>0 and lines[yc][xc-1] in "-LF":
                q.append((yc, xc-1, lc+1))
        elif lines[yc][xc] == "F":
            if yc<h-1 and lines[yc+1][xc] in "|LJ":
                q.append((yc+1, xc, lc+1))
            if xc<w-1 and lines[yc][xc+1] in "-J7":
                q.append((yc, xc+1, lc+1))
        
print("part 1:", part1)

lines2 = [["."for _ in range(w*3)]for _ in range(h*3)]

for y,x in seen:
    if lines[y][x] == "|" or (lines[y][x]=="S" and potential_S=="|"):
        lines2[3*y][3*x+1] = "#"
        lines2[3*y+1][3*x+1] = "#"
        lines2[3*y+2][3*x+1] = "#"
    elif lines[y][x] == "-" or (lines[y][x]=="S" and potential_S=="-"):
        lines2[3*y+1][3*x] = "#"
        lines2[3*y+1][3*x+1] = "#"
        lines2[3*y+1][3*x+2] = "#"
    elif lines[y][x] == "L" or (lines[y][x]=="S" and potential_S=="L"):
        lines2[3*y][3*x+1] = "#"
        lines2[3*y+1][3*x+1] = "#"
        lines2[3*y+1][3*x+2] = "#"
    elif lines[y][x] == "J" or (lines[y][x]=="S" and potential_S=="J"):
        lines2[3*y][3*x+1] = "#"
        lines2[3*y+1][3*x+1] = "#"
        lines2[3*y+1][3*x] = "#"
    elif lines[y][x] == "7" or (lines[y][x]=="S" and potential_S=="7"):
        lines2[3*y+1][3*x] = "#"
        lines2[3*y+1][3*x+1] = "#"
        lines2[3*y+2][3*x+1] = "#"
    elif lines[y][x] == "F" or (lines[y][x]=="S" and potential_S=="F"):
        lines2[3*y+1][3*x+2] = "#"
        lines2[3*y+1][3*x+1] = "#"
        lines2[3*y+2][3*x+1] = "#"
inside = set()
seen2 = set()
for y, row in enumerate(lines2):
    for x, c in enumerate(row):
        if c != "#" and (y, x) not in seen2:
            touched_outside = False
            q = [(y,x)]
            seen3 = set()
            while q:
                yc, xc = q.pop(0)
                if 0<=yc<3*h and 0<=xc<3*w:
                    if lines2[yc][xc] != "#" and (yc, xc) not in seen2:
                        seen2.add((yc, xc))
                        seen3.add((yc, xc))
                        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                            q.append((yc+dy, xc+dx))
                else:
                    touched_outside = True
            if not touched_outside:
                inside |= seen3

# with open("out.txt", "w") as f:
#     f.write("\n".join(["".join(line) for line in lines2]))

print("part 2:", sum((y,x) not in seen and (3*y, 3*x) in inside for y in range(h) for x in range(w)))
