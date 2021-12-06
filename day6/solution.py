with open('day6/input.txt') as f:q=f.readlines()

def solve(n):
    fishes = [0,0,0,0,0,0,0,0,0]
    for t in q[0].split(","):
        fishes[int(t)]+=1

    for i in range(n):
        a = fishes[0]
        fishes = fishes[1:] + [a]
        fishes[6] += a

    return sum(fishes)

print(f"part1: {solve(80)}")
print(f"part2: {solve(256)}")