import math

with open("input.txt") as f:
    times, distances = [[*map(int, line.split()[1:])]for line in f.read().split("\n")]

def find_roots_int(a, b, c):
    d = b**2 - 4*a*c
    # d is positive for all cases in this problem
    r1 = (-b + d**0.5)/2/a
    r2 = (-b - d**0.5)/2/a
    r1, r2 = sorted([r1, r2])
    if r1%1 == 0: r1 += 1
    if r2%1 == 0: r2 -= 1
    return math.ceil(r1), math.floor(r2)


part1 = 1
for time, distance_record in zip(times, distances):
    # x * (time - x) > distance_record
    # x**2 - x*time + distance_record < 0
    r1, r2 = find_roots_int(1, -time, distance_record)
    part1 *= r2 - r1 + 1

time = int("".join(map(str, times)))
distance = int("".join(map(str, distances)))
r1, r2 = find_roots_int(1, -time, distance)
part2 = r2 - r1 + 1



print("part 1:", part1)
print("part 2:", part2)
