with open("input.txt") as f:
    lines = f.read().split("\n")

cubes = {tuple(map(int,l.split(','))) for l in lines}
sides = lambda x,y,z: {(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}

print(f"Part1: {sum((s not in cubes) for c in cubes for s in sides(*c))}")

seen = set()
todo = [(-1,-1,-1)]

while todo:
    here = todo.pop()
    todo += [s for s in (sides(*here) - cubes - seen) if all(-1<=c<=25 for c in s)]
    seen |= {here}

print(f"Part2: {sum((s in seen) for c in cubes for s in sides(*c))}")
