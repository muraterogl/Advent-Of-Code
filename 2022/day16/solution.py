# My part 1 solution
# import re

# with open("input.txt") as f:
#     lines = f.read().split("\n")

# paths = {}
# flow_rates = {}
# for line in lines:
#     current, *others = re.findall(r'[A-Z]{2,}',line)
#     flow_rate = int(re.findall(r'\d+',line)[0])
#     paths[current] = others
#     flow_rates[current] = flow_rate

# part1 = 0
# queue = [("AA",0,0,[])]
# seen = set()
# while queue:
#     current_room, passed_minutes, total_flow, open_valves = queue.pop(0)
#     if (current_room, total_flow, len(open_valves)) in seen:
#         continue
#     seen.add((current_room, total_flow, len(open_valves)))
#     if passed_minutes >= 30:
#         part1 = max(part1,total_flow)
#         continue
#     for valve in open_valves:
#         total_flow += flow_rates[valve]
#     if flow_rates[current_room] > 0 and not current_room in open_valves:
#         queue.append((current_room, passed_minutes+1, total_flow, open_valves+[current_room]))
#     for path in paths[current_room]:
#         queue.append((path, passed_minutes+1, total_flow, open_valves))

# print(f"Part1: {part1}")


#I got the answer from https://github.com/juanplopes/advent-of-code-2022/blob/main/day16.py

import re

with open("input.txt") as f:
    lines = [re.split('[\\s=;,]+', x) for x in f.read().splitlines()]


G = {x[1]: set(x[10:]) for x in lines}
F = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
I = {x: 1<<i for i, x in enumerate(F)}
T = {x: {y: 1 if y in G[x] else float('+inf') for y in G} for x in G}
for k in T:
    for i in T:
        for j in T:
            T[i][j] = min(T[i][j], T[i][k]+T[k][j])

def visit(v, budget, state, value, answer):
    answer[state] = max(answer.get(state, 0), value)
    for u in F:
        newbudget = budget - T[v][u] - 1
        if I[u] & state or newbudget < 0: continue
        visit(u, newbudget, state | I[u], value + newbudget * F[u], answer)
    return answer    

total1 = max(visit('AA', 30, 0, 0, {}).values())
visited2 = visit('AA', 26, 0, 0, {})
total2 = max(v1+v2 for k1, v1 in visited2.items() 
                   for k2, v2 in visited2.items() if not k1 & k2)
print(total1, total2)
