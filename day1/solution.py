with open('day1/input.txt') as f:q=f.readlines()
*n,=map(int,q)
print(f"part1: {sum(y>x for x,y in zip(n,n[1:]))}")
print(f"part2: {sum(sum(n[i:i+3])>sum(n[i-1:i+2])for i in range(1,len(n)-2))}")