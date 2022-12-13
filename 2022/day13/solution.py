from functools import cmp_to_key

with open("input.txt") as f:
    lines = f.read().split("\n")

def compare(left, right):
    a = isinstance(left,int)
    b = isinstance(right,int)
    if a and b:
        return left-right
    elif a:
        left = [left]
    elif b:
        right = [right]
    
    for l,r in zip(left, right):
        x = compare(l, r)
        if x == 0:
            continue
        return x
    return len(left)-len(right)
    

part1=0
packets=[[[2]],[[6]]]

for i in range(0,len(lines),3):
    left = eval(lines[i])
    right = eval(lines[i+1])
    packets.append(left)
    packets.append(right)
    if compare(left, right)<0:
        part1 += i//3+1

packets.sort(key=cmp_to_key(compare))
print(f"Part1: {part1}")
print(f"Part2: {-~packets.index([[2]])*-~packets.index([[6]])}")
