with open('input.txt') as f:
    lines = f.read().split("\n")

result1 = 0
result2 = 0

junctions = [tuple(map(int, line.split(","))) for line in lines]

distances = []
used = set()

def dumb_hash(j1 , j2):
    return tuple([*sorted([j1[0], j2[0]]),*sorted([j1[1], j2[1]]),*sorted([j1[2], j2[2]])])

for index1, j1 in enumerate(junctions):
    for index2, j2 in enumerate(junctions):
        if index1 != index2 and not dumb_hash(j1,j2) in used:
            distance = ((j1[0]-j2[0])**2 + (j1[1]-j2[1])**2 + (j1[2]-j2[2])**2)**0.5
            distances.append((distance, j1, j2))
            used.add(dumb_hash(j1,j2))

distances.sort(key=lambda x:x[0])
connections = [set([junction]) for junction in junctions]
count = 0
for distance, j1, j2 in distances:
    i1 = -1
    i2 = -1
    for i, connection in enumerate(connections):
        if j1 in connection:
            i1 = i
        if j2 in connection:
            i2 = i
    if i1 == i2:
        pass
        #count -= 1
    else:
        c1 = connections[i1]
        c2 = connections[i2]
        connections = [connection for i, connection in enumerate(connections) if i!=i1 and i!=i2] + [c1|c2]
    count += 1
    if count == 1000:
        connections_dist = sorted(map(len, connections), reverse=True)
        connections_dist += [1]*(len(junctions)-sum(connections_dist))
        result1 = eval("*".join(map(str,connections_dist[:3])))
    if len(connections)==1:
        result2 = j1[0] * j2[0]
        break

print(result1, result2)
