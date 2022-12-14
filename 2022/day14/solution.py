from copy import deepcopy

with open("input.txt") as f:
    lines = f.read().split("\n")

rocks = set()
max_y = 0
for line in lines:
    points = line.split(" -> ")
    for a,b in zip(points,points[1:]):
        x,y = map(int,a.split(","))
        X,Y = map(int,b.split(","))
        x,X = sorted([x,X])
        y,Y = sorted([y,Y])
        max_y = max(max_y,Y)
        for i in range(y,Y+1):
            for j in range(x,X+1):
                rocks.add((j,i))
max_y+=2
part1 = 0
finished = False
rocks2 = deepcopy(rocks)
while not finished:
    sx, sy = 500, 0
    for i in range(1000):
        if i==999:
            finished = True
            break
        if not (sx,sy+1) in rocks:
            sy+=1
        elif not (sx-1,sy+1) in rocks:
            sx-=1
            sy+=1
        elif not (sx+1,sy+1) in rocks:
            sx+=1
            sy+=1
        else:
            part1+=1
            rocks.add((sx,sy))
            break
print(f"Part1: {part1}")
part2 = 0
finished = False
while not finished:
    sx, sy = 500, 0
    while True:
        if not (sx,sy+1) in rocks2 and sy+1!=max_y:
            sy+=1
        elif not (sx-1,sy+1) in rocks2 and sy+1!=max_y:
            sx-=1
            sy+=1
        elif not (sx+1,sy+1) in rocks2 and sy+1!=max_y:
            sx+=1
            sy+=1
        else:
            part2+=1
            rocks2.add((sx,sy))
            if sx==500 and sy==0:
                finished = True
            break
print(f"Part2: {part2}")
