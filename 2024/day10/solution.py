with open("input.txt") as f:
    lines = f.read().split("\n")

part1 = part2 = 0
h = len(lines)
w = len(lines[0])

for y in range(h):
    for x in range(w):
        if lines[y][x] == "0":
            score = 0
            rating = 0
            seen = set()
            q = [(y,x,0)]
            while q:
                (cy, cx, ch), *q = q
                if ch == 9 and (cy, cx) not in seen:
                    score += 1
                    rating += 1
                    seen.add((cy,cx))
                elif ch == 9:
                    rating += 1
                else:
                    for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0<=cx+dx<w and 0<=cy+dy<h and lines[cy+dy][cx+dx]==str(ch+1):
                            q += (cy+dy,cx+dx,ch+1),
            part1 += score
            part2 += rating

print(part1, part2)
