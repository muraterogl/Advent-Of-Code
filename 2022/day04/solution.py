import re

with open('input.txt') as f:
    lines=f.read().splitlines()

count = 0
count2 = 0
for pairs in lines:
    a,b,A,B = map(int,re.findall(r"\d+",pairs))
    if (a<=A and b>=B) or (A<=a and B>=b):
        count += 1
    if (A<=b and a<=B) or (a<=B and A<=b):
        count2 += 1

print(f"Part 1: {count}")
print(f"Part 2: {count2}")
