import math

with open("input.txt") as f:
    ins, p = f.read().split("\n\n")

length = len(ins)
l = {}
r = {}
for line in p.split("\n"):
    x, _, y, z = line.split()
    l[x] = y[1:-1]
    r[x] = z[:-1]

current = "AAA"
steps = 0
while current != "ZZZ":
    if ins[steps%length] == "R":
        current = r[current]
    else:
        current = l[current]
    steps += 1

part1=steps
print("part 1:", part1)

current = [k for k in l.keys() if k[-1]=="A"]
steps = [0 for _ in current]
for i in range(len(steps)):
    while current[i][-1] != "Z":
        if ins[steps[i]%length] == "R":
            current[i] = r[current[i]]
        else:
            current[i] = l[current[i]]
        steps[i] += 1

part2 = math.lcm(*steps)
print("part 2:", part2)
