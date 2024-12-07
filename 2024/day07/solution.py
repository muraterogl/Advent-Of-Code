import re

with open("input.txt") as f:
    lines = f.read().split("\n")

part1 = part2 = 0

def is_possible(r, q):
    try:
        q[1]
        return is_possible(r-q[-1],q[:-1]) or (r%q[-1]==0 and is_possible(r//q[-1], q[:-1]))
    except:
        return r == q[0]

def is_possible2(r, q):
    try:
        q[1]
        return is_possible2(r-q[-1],q[:-1]) or (r%q[-1]==0 and is_possible2(r//q[-1], q[:-1])) \
               or (str(r).endswith(str(q[-1])) and is_possible2((r-q[-1])//(10**len(str(q[-1]))), q[:-1]))
    except:
        return r == q[0]


for line in lines:
    r, *q = map(int, re.findall(r'\d+',line))
    if is_possible(r, q):
        part1 += r
        part2 += r
    elif is_possible2(r, q):
        part2 += r


print(part1, part2)
