with open("input.txt") as f:
    lines = f.read().split("\n")

part1 = part2 = 0
connections = {}
result = []
for line in lines:
    a,b = line.split("-")
    if a not in connections:
        connections[a] = set()
    connections[a].add(b)
    if b not in connections:
        connections[b] = set()
    connections[b].add(a)
    result += tuple(sorted([a,b])),

part2 = []
l = max(map(len,connections.values()))
for i in range(3, l+1):
    new_result = []
    for a in set([c for net in result for c in net]):
    #for a in connections.keys():
        for r in result:
            if all(a in connections[x] for x in r):
                net = tuple(sorted(list(r) + [a]))
                new_result += net,
    result = list(set(new_result)).copy()
    if i==3:
        part1 = sum(any(s[0]=="t" for s in net) for net in result)
    if len(result) == 1:
        break
    print(i)


part2 = ",".join(result[0])
print(part1, part2)
