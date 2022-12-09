import re

with open('input.txt') as f:
    cratesRaw, commands=f.read().split("\n\n")

cratesRaw = [[line[i+1]for i in range(0,len(line),4)]for line in cratesRaw.split("\n")]
crates = {}
crates2 = {}
for place in zip(*cratesRaw):
    *stacks, n = place
    crates[n] = []
    crates2[n] = []
    for crate in reversed(stacks):
        if crate != " ":
            crates[n].append(crate)
            crates2[n].append(crate)

for command in commands.split("\n"):
    count, f, d = re.findall(r"\d+",command)
    for _ in range(int(count)):
        crates[d].append(crates[f].pop())
    crates2[d] += crates2[f][-int(count):]
    crates2[f] = crates2[f][:len(crates2[f])-int(count)]


print(f"Part 1: {''.join(l[-1] for l in crates.values())}")
print(f"Part 2: {''.join(l[-1] for l in crates2.values())}")
