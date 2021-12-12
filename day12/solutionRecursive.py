with open('day12/input.txt') as f:q=f.readlines()

paths = {}

for line in q:
    a,b = map(str.rstrip, line.split("-"))
    if a in paths:
        paths[a].append(b)
    else:
        paths[a] = [b]
    if b in paths:
        paths[b].append(a)
    else:
        paths[b] = [a]


def count1(before, begin):
    if begin=="end":
        return 1
    if begin[0].islower() and begin in before:
        return 0
    before[begin] = 1
    return sum(count1(dict(before), nei) for nei in paths[begin])

def count2(before, begin):
    if (begin=="start" and "start" in before) or (begin in before and (any(before[i]>1 for i in before) or before[begin]>1)):
        return 0
    if begin=="end":
        return 1
    if begin[0].islower():
        if begin in before:
            before[begin]+=1
        else:
            before[begin]=1
    return sum(count2(dict(before), nei) for nei in paths[begin])
    

print(f"part1: {count1({}, 'start')}")
print(f"part2: {count2({}, 'start')}")
