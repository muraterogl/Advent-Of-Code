import re

with open("input.txt") as f:
    line = f.read()

part1 = part2 = 0
do = 1
for a,b in re.findall(r"do(n't)?|mul\((\d+,\d+)\)", line):
    if b:
        b,c = eval(b)
        part1 += b*c
        part2 += b*c*do
    else:
        do = a==''

print(part1, part2)
