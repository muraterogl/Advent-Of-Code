from functools import cache

with open("input.txt") as f:
    lines = f.read().split("\n")

@cache
def solve(block, numbers):
    if block == "":
        return 0 if numbers else 1
    block = block.strip(".")
    if block[0] == "?":
        return solve("#"+block[1:], numbers) + solve(block[1:], numbers)
    
    if not numbers or numbers[0] > len(block) or "." in block[:numbers[0]]:
        return 0
    if len(numbers) > 1:
        if len(block) < sum(numbers) or block[numbers[0]] == "#":
            return 0
        return solve(block[numbers[0]+1:], numbers[1:])
    else:
        return solve(block[numbers[0]:], ())



part1 = 0
part2 = 0
for line in lines:
    block, numbers = line.split()
    *numbers, = map(int, numbers.split(","))
    part1 += solve(block, tuple(numbers))
    part2 += solve("?".join([block]*5), tuple(numbers*5))

print("part 1:", part1)
print("part 2:", part2)
