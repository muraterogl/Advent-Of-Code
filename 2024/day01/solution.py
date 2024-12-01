from collections import Counter

with open("input.txt") as f:
    l1, l2 = list(zip(*[list(map(int,line.split())) for line in f.read().split("\n")]))
    part1 = sum([abs(a-b) for a,b in zip(*[sorted(list(l)) for l in [l1,l2]])])
    c = Counter(l2)
    part2 = sum(x*c[x] for x in l1)

print(part1, part2)
