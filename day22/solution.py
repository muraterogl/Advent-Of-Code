from os import path
from collections import Counter
import numpy as np
import re

def part1(commands):
    core = np.zeros([101,101,101],dtype="ubyte")   
    for command in commands:
        a, (x1, x2, y1, y2, z1, z2) = command
        x1 = max(-50, x1)
        x2 = min(50, x2)
        y1 = max(-50, y1)
        y2 = min(50, y2)
        z1 = max(-50, z1)
        z2 = min(50, z2)
        core[x1+50:x2+51, y1+50:y2+51, z1+50:z2+51] = 1 if a==True else 0
    return np.sum(core)

def part2(commands):
    cubes = Counter()
    for command in commands:
        a, (x1, x2, y1, y2, z1, z2) = command
        update = Counter()
        for cube in cubes.items():
            (ox1, ox2, oy1, oy2, oz1, oz2), count = cube
            ix1 = max(ox1, x1)
            ix2 = min(ox2, x2)
            iy1 = max(oy1, y1)
            iy2 = min(oy2, y2)
            iz1 = max(oz1, z1)
            iz2 = min(oz2, z2)
            if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2:
                update[(ix1, ix2, iy1, iy2, iz1, iz2)] -= count
        if a:
            update[(x1, x2, y1, y2, z1, z2)] += 1
        cubes.update(update)
    
    volume = sum((x2-x1+1)*(y2-y1+1)*(z2-z1+1)*count for (x1, x2, y1, y2, z1, z2),count in cubes.items())
    return volume


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    commands = []
    for line in f.read().split("\n"):
        c, l= line.split()
        l = [*map(int, re.findall(r"-?\d+", l))]
        commands.append((c=="on", l))
    print("Part 1:", part1(commands))
    print("Part 2:", part2(commands))