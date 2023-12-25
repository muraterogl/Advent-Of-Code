import math
import pygraphviz as pvg

with open("input.txt") as f:
    lines = [line.replace(":","").split() for line in f.read().split("\n")]

G = pvg.AGraph()
Graph = {}
for line in lines:
    node, *q = line
    for x in q:
        G.add_edge(node, x),
        if node in Graph:
            Graph[node].add(x)
        else:
            Graph[node] = set([x])
        if x in Graph:
            Graph[x].add(node)
        else:
            Graph[x] = set([node])

#G.layout()
#G.draw("out.png")

G.remove_edge("rfg","jks")
Graph["rfg"].remove("jks")
Graph["jks"].remove("rfg")
G.remove_edge("zjm","zcp")
Graph["zjm"].remove("zcp")
Graph["zcp"].remove("zjm")
G.remove_edge("nsk","rsg")
Graph["nsk"].remove("rsg")
Graph["rsg"].remove("nsk")

seen = set()
area  = []
for n in Graph:
    if n not in seen:
        q = [n]
        a = 0
        while q:
            c = q.pop(0)
            if c not in seen:
                seen.add(c)
                a += 1
                for x in Graph[c]:
                    q += x,
        area += a,
print("part 1:", math.prod(area))
print("part 2:", 0)
