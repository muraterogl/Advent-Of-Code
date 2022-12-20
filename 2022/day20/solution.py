with open("input.txt") as f:
    lines = f.read().split("\n")

def solve(count, p):
    q = [(int(x)*p, i) for i,x in enumerate(lines)]
    c = q[:]
    l = len(q)
    for _ in range(count):
        for s in c:
            i = q.index(s)
            x = q.pop(i)
            new_index = (i+x[0]-1)%(l-1)+1
            q.insert(new_index, x)
            #print(*q)
        
        
    i0 = 0
    for i,x in enumerate(q):
        if x[0]==0:
            i0=i
            break
    return sum(q[(i0+i*1000)%l][0] for i in range(1,4))

print(f"Part1: {solve(1, 1)}")
print(f"Part2: {solve(10, 811589153)}")
