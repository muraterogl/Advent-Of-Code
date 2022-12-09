with open('day07/input.txt') as f:q=f.readlines()

*positions, = map(int, q[0].split(","))

p1 = min(sum(abs(i-positions[j])for j in range(len(positions)))for i in range(max(positions)))
print(f"part1: {p1}")

p2 = int(min(sum(((u:=abs(i-positions[j]))*(u+1)/2)for j in range(len(positions)))for i in range(max(positions))))
print(f"part2: {p2}")