import re

with open("input.txt") as f:
    lines = f.read().split("\n")

sensors = {}   
beacons = set()
empty = set()
row = 2000000
for line in lines:
    x,y,X,Y=map(int,re.findall(r'-?\d+',line))
    dy = abs(y-Y)
    dx = abs(x-X)
    sensors[(x,y)]=dy+dx
    if Y==row:
        beacons.add(X)
    if y-dx-dy<=row<=y+dx+dy:
        dr = abs(y-row)
        for i in range(x-dx-dy+dr,x+dx+dy-dr+1):
            empty.add(i)

print(f"Part1: {len(empty-beacons)}")
max_limit=4000000
for (x,y),r in sensors.items():
    for Y in range(y-r-1,y+r+2):
        dx=r+1-abs(y-Y)
        for X in [x-dx,x+dx]:
            if 0<=X<=max_limit and 0<=Y<=max_limit:
                intersect=False
                for (x2,y2),r2 in sensors.items():
                    if abs(x2-X)+abs(y2-Y)<=r2:
                        intersect=True
                if not intersect:
                    print(f"Part2: {4000000*X+Y}")
                    exit()
