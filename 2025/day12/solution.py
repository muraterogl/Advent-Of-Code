import re

with open('input.txt') as f:
    lines = f.read().split("\n\n")

result1 = 0

*shapes_raw, regions = lines
shapes = [sum(c=="#"for c in shape)for shape in shapes_raw]

for region in regions.split("\n"):
    x_max, y_max, *counts = map(int, re.findall(r'\d+', region))
    result1 += x_max*y_max >= sum(a*c for a,c in zip(shapes,counts))

print(result1)
