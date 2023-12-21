with open("input.txt") as f:
    lines = f.read().split("\n")

grid = {i + j*1j: c for i,r in enumerate(lines)
                 for j,c in enumerate(r) if c in '.S'}

h = len(lines)

done = []
q = {x for x in grid if grid[x]=='S'}

for s in range(int(2.5*h)+1):
    if s == 64: print("part 1:", len(q))
    if s%h == h//2: done.append(len(q))
    q = {p+d for d in {1,-1,1j,-1j} for p in q
            if (p+d).real%h + (p+d).imag%h*1j in grid}

f = lambda n,a,b,c: a+n*(b-a) +n*(n-1)//2*((c-b)-(b-a))
print("part 2:", f(26501365//h, *done))
