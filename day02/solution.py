with open('day02/input.txt') as f:q=f.readlines()
x=y=0
for i in q:
    a,b = i.split()
    if a=="forward":
        x += int(b)
    elif a=="up":
        y -= int(b)
    else:
        y += int(b)
print(f"part1: {x*y}")

x=y=aim=0
for i in q:
    a,b = i.split()
    if a=="forward":
        x += int(b)
        y += aim * int(b)
    elif a=="up":
        aim -= int(b)
    else:
        aim += int(b)
print(f"part2: {x*y}")