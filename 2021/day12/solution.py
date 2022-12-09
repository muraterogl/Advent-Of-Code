from collections import Counter
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


stack = [["start"]]
result = []
while stack:
    currentPath = stack.pop()
    if currentPath[-1] == "end":
        result.append(currentPath)
        continue
    elif any(cave[0].islower() and currentPath.count(cave)>1 for cave in currentPath):
        continue
    for neighbor in paths[currentPath[-1]]:
        stack.append(currentPath+[neighbor])


    

print(f"part1: {len(result)}")

stack = [["start"]]
result = []
while stack:
    currentPath = stack.pop()
    if currentPath[-1] == "end":
        result.append(currentPath)
        continue
    counts = Counter([cave for cave in currentPath if cave[0].islower()])
    if counts["start"]>1 or counts["end"]>1 or len([cave for cave in counts if counts[cave]>1])>1 or any(counts[cave]>2 for cave in counts):
        continue
    for neighbor in paths[currentPath[-1]]:
        stack.append(currentPath+[neighbor])

print(f"part2: {len(result)}")
