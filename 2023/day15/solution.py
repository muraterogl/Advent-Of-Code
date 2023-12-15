import re

with open("input.txt") as f:
    steps = f.read().split(",")

part1=0
for step in steps:
    value = 0
    for c in step:
        value += ord(c)
        value = (value * 17) % 256
    part1 += value
print("part 1:", part1)


boxes = [{}for _ in range(256)]
for step in steps:
    box_s, sign, lens = re.findall(r"([a-z]+)([-=])(\d+)?", step)[0]
    box = 0
    for c in box_s:
        box += ord(c)
        box = (box * 17) % 256
    if sign == "=" and not lens in boxes[box]:
        boxes[box][box_s] = lens
    elif sign == "-" and box_s in boxes[box]:
        del boxes[box][box_s]
part2 = 0
for i, box in enumerate(boxes):
    j = 1
    for key, lens in box.items():
        part2 += (i+1) * j * int(lens)
        j += 1
print("part 2:", part2)
