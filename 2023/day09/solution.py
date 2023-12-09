with open("input.txt") as f:
    lines = f.read().split("\n")

part1=0
part2=0
for line in lines:
    *numbers, = map(int, line.split())
    numbers_copy = numbers.copy()
    last_numbers = []
    first_numbers = []
    while len({*numbers}) != 1:
        last_numbers.append(numbers[-1])
        first_numbers.append(numbers[0])
        numbers = [y-x for x,y in zip(numbers[:-1], numbers[1:])]
    result1 = numbers[-1]
    result2 = numbers[0]
    for x,y in zip(last_numbers[::-1], first_numbers[::-1]):
        result1 += x
        result2 = y - result2
    part1 += result1
    part2 += result2

print("part 1:", part1)
print("part 2:", part2)
