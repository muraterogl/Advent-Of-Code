from collections import defaultdict
from functools import cmp_to_key

with open("input.txt") as f:
    rules_raw, updates = [lines.split("\n") for lines in f.read().split("\n\n")]

part1 = part2 = 0

rules = defaultdict(set)
for rule in rules_raw:
    a,b = map(int,rule.split("|"))
    rules[a].add(b)

for update in updates:
    update = list(map(int, update.split(",")))
    correct_update = sorted(update,key=cmp_to_key(lambda x,y:[-1,1][x in rules[y]]))
    if  update == correct_update:
        part1 += correct_update[len(correct_update)//2]
    else:
        part2 += correct_update[len(correct_update)//2]

print(part1, part2)
