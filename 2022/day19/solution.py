import re

with open("input.txt") as f:
    lines = f.read().split("\n")
part1=0
part2=1

def solve(line,count):
    blueprint,oc,cc,ooc,occ,goc,gobc=map(int, re.findall(r'\d+', line))
    costs = (oc,0,0,0),(cc,0,0,0),(ooc,occ,0,0),(goc,0,gobc,0)
    mask = (1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)
    seen = {}
    initial_robots = 1,0,0,0
    initial_res = 0,0,0,0
    minute_passed = 0
    stack = [(initial_robots, initial_res, minute_passed)]
    max_geode = 0
    while stack:
        robots, res, m = stack.pop()
        if (robots, res) in seen and seen[(robots, res)] <= m:
            continue
        seen[(robots, res)] = m
        if m==count:
            max_geode = max(max_geode, res[3])
            continue
        if (count-m) * robots[3] + res[3] + (count-m)*(count-1-m)/2 < max_geode:
            continue 
        stack.append((robots, tuple(r+rs for r,rs in zip(robots, res)), m+1))
        for i in range(4):
            if i!=3 and robots[i]>=max(cost[i] for cost in costs):
                continue
            if all(r>=c for c,r in zip(costs[i],res)):
                stack.append((tuple(r+m for r,m in zip(robots,mask[i])), tuple(r+rs-c for r,rs,c in zip(robots, res, costs[i])), m+1))
    print(f"{max_geode} {blueprint}")
    return max_geode, blueprint

for line in lines:
    max_geode, blueprint = solve(line, 24)
    part1 += max_geode * blueprint
    if blueprint < 4:
        max_geode, _ = solve(line, 32)
        part2 *= max_geode

print(f"Part1: {part1}")
print(f"Part2: {part2}")
