with open("input.txt") as f:
    lines = f.read().split("\n")
h=len(lines)
w=len(lines[0])
grid = {y+x*1j:c for y,r in enumerate(lines)
                 for x,c in enumerate(r) if c in ".<^>v"}
# q = [(1j,0,set([1j]))]
# maxl=0
# while q:
#     c,l,s=q.pop(0)
#     if c==h-1+(w-2)*1j:
#         maxl=max(maxl,l)
#         continue
#     for d in [(1,-1,1j,-1j),(-1j,),(-1,),(1j,),(1,)][".<^>v".index(grid[c])]:
#         if c+d in grid and c+d not in s:
#             q += (c+d,l+1,s|set([c+d])),
# print("part 1:", maxl)

grid2 = {*[c for c in grid if len([d for d in (1,-1,1j,-1j) if c+d in grid])>2] + [1j, h-1+(w-2)*1j]}
graph={}
for c in grid2:
    seen=set()
    q=[(c,0)]
    while q:
        p, l = q.pop(0)
        if p!=c and p in grid2:
            if c in graph:
                graph[c] += (p, l),
            else:
                graph[c] = [(p, l)]
        else:
            for d in (1,-1,1j,-1j):
                if p+d in grid and p+d not in seen:
                    seen.add(p+d)
                    q += (p+d, l+1),
maxl=0
q=[(1j, 0, set([1j]))]
while q:
    c, l, s = q.pop(0)
    if c == h-1+(w-2)*1j:
        if l > maxl:
            maxl = l
            print(maxl)
        continue
    for d, ll in graph[c]:
        if d not in s:
            q += (d, l+ll, s|set([d])),
            
print("part 2:", maxl)
