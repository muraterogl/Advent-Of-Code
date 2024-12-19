from functools import lru_cache

with open("input.txt") as f:
    patterns, designs = f.read().split("\n\n")
part1 = part2 = 0
patterns = set(patterns.split(", "))
designs = designs.split("\n")

@lru_cache
def possible(design):
    l = len(design)
    if l==1:
        return 1 if design in patterns else 0
    count = 0
    for i in range(1, l+1):
        if design[:i] in patterns:
            c = possible(design[i:]) if i<l else 1
            count += c
    return count

part1 = sum(1 if possible(design) else 0 for design in designs)
part2 = sum(possible(design) for design in designs)
print(part1, part2)
