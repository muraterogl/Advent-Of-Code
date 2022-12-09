with open('input.txt') as f:
    lines=f.read().splitlines()

score = 0
score2 = 0

for line in lines:
    op, me = line.split()
    if op=="A" and me=="X":
        score += 1+3
        score2 += 3
    elif op=="A" and me=="Y":
        score += 2+6
        score2 += 1+3
    elif op=="A" and me=="Z":
        score += 3
        score2 += 2+6
    elif op=="B" and me=="X":
        score += 1
        score2 += 1
    elif op=="B" and me=="Y":
        score += 2+3
        score2 += 2+3
    elif op=="B" and me=="Z":
        score += 3+6
        score2 += 3+6
    elif op=="C" and me=="X":
        score += 1+6
        score2 += 2
    elif op=="C" and me=="Y":
        score += 2
        score2 += 3+3
    else:
        score += 3+3
        score2 += 1+6


print(f"Part 1: {score}")
print(f"Part 2: {score2}")
