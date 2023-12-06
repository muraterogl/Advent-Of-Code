with open("input.txt") as f:
    times, distances = [[*map(int, line.split()[1:])]for line in f.read().split("\n")]

part1 = 1
for time, distance_record in zip(times, distances):
    # x * (time - x) > distance_record
    # x**2 - x*time + distance_record < 0
    found = 0
    for x in range(time+1):
        if x**2 - x*time + distance_record < 0:
            found += 1
    part1 *= found

part2 = 0

time = int("".join(map(str, times)))
distance = int("".join(map(str, distances)))
for x in range(time+1):
    if x**2 - x*time + distance < 0:
        part2 += 1


print("part 1:", part1)
print("part 2:", part2)
