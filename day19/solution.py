from os import path
from collections import Counter
from itertools import permutations, product
import numpy as np

#https://github.com/ilalex/aoc2021/blob/master/day19.py

AXES = [np.array(a) for a in permutations([1, 2, 3])]
DIRS = [np.array(d) for d in product([-1, 1], [-1, 1], [-1, 1])]
ALL = [(ax, d) for ax, d in product(AXES, DIRS)]

class Scanner:
    def __init__(self, data):
        self.points = np.array([[*map(int, l.split(","))]for l in data.split("\n")[1:]], dtype="int16")
        self.pos = None

    def make_shift(self, scanner2):
        p1 = self.points
        for ax, d in ALL:
            p2 = scanner2.points[:, ax - 1] * d
            d = p1[np.newaxis, :] - p2[:, np.newaxis]
            uns = [np.unique(d[..., i], return_counts=True) for i in range(3)]
            if all([un[1].max() >= 12 for un in uns]):
                scanner2.points = p2
                scanner2.pos = np.array([u[0][u[1] >= 12][0] for u in uns], dtype='int16')
                scanner2.pos += self.pos
                return True
        return False

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    scanners = [Scanner(d) for d in f.read().split("\n\n")]
    scanners[0].pos = np.array([0, 0, 0])

    while any(scanner.pos is None for scanner in scanners):
        for scanner1 in scanners:
            if scanner1.pos is None:
                for scanner2 in scanners:
                    if scanner2.pos is not None and scanner2.make_shift(scanner1):
                        break
    
    beacons = set()
    for s in scanners:
        for p in (s.points + s.pos):
            beacons.add(tuple(p))
    
    mx = 0
    for s1, s2 in permutations(scanners, 2):
        d = np.abs(s1.pos - s2.pos).sum()
        mx = max(mx, d)

    print("Part 1:", len(beacons))
    print("Part 2:", mx)