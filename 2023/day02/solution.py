import math

def line_to_numbers(line):
    game, data = line.split(":")
    game = int(game.split()[1])
    data = [{d.split()[1]: int(d.split()[0])for d in s.split(", ")}for s in data.split("; ")]
    return game, data


with open("input.txt") as f:
    lines = f.read().split("\n")

part1 = 0
part2 = 0

for line in lines:
    game, data = line_to_numbers(line)
    possible = True
    min_possible = {"red":0, "green":0, "blue":0}
    for d in data:
        if ("red" in d and d["red"]>12) or ("green" in d and d["green"]>13) or ("blue" in d and d["blue"]>14):
            possible = False
        for k,v in d.items():
            min_possible[k] = max(min_possible[k], v)
    part2 += math.prod(min_possible.values())
    if possible:
        part1 += game

print(part1)
print(part2)
