with open('input.txt') as f:
    q=f.read()

elves = [sum(map(int,elf.split()))for elf in q.split("\n\n")]

print(f"Part 1: {max(elves)}")
print(f"Part 2: {sum(sorted(elves)[-3:])}")
