import math
with open('day09/input.txt') as f:q=f.readlines()
m = [[*map(int, list(i.rstrip("\n")))] for i in q]
l=[]
for y in range(len(m)):
    for x in range(len(m[y])):
        if y<1 or m[y-1][x] > m[y][x]:
            if y>len(m)-2 or m[y+1][x] > m[y][x]:
                if x<1 or m[y][x-1] > m[y][x]:
                    if x>len(m[0])-2 or m[y][x+1] > m[y][x]:
                        l.append((y,x))
            
print(f"part1: {sum(m[y][x]+1 for y,x in l)}")


l = []
seen = [[0 for _ in range(len(m[0]))]for _ in range(len(m))]
for i in range(len(m)):
    for j in range(len(m[0])):
        if seen[i][j]==0 and m[i][j]!=9:
            area = 0
            q = [(i,j)]
            while q:
                y,x = q[0]
                q = q[1:]
                if y>=0 and y<len(m) and x>=0 and x<len(m[0]) and seen[y][x]==0 and m[y][x]!=9:
                    area+=1
                    seen[y][x]=1
                    q.append((y+1,x))
                    q.append((y-1,x))
                    q.append((y,x-1))
                    q.append((y,x+1))
            l.append(area)


print(f"part2: {math.prod(sorted(l, reverse=True)[:3])}")