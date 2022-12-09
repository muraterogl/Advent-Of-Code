with open('input.txt') as f:
    line=f.read()

def findResult(n):
    for start in range(n,len(line)):
        if len(set(line[start-n:start]))==n:
            return start

print(f"Part 1: {findResult(4)}")
print(f"Part 2: {findResult(14)}")
