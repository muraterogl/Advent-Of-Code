with open('input.txt') as f:
    lines = f.read().split("\n")

result1 = 0
result2 = 0

beam = None
splitters = set()
height = len(lines)
width = len(lines[0])
for y in range(height):
    for x in range(width):
        if lines[y][x] == "S":
            beam = (y, x)
        elif lines[y][x] == "^":
            splitters.add((y,x))

splitters_used = set()
results = {}
def solve(y, x):
    if y > height:
        return 1
    y += 1
    if (y, x) in splitters:
        splitters_used.add((y,x))
        right = results[(y, x+1)] if (y, x+1) in results else solve(y, x+1)
        results[(y, x+1)] = right
        left = results[(y, x-1)] if (y, x-1) in results else solve(y, x-1)
        results[(y, x-1)] = left
        return left + right
    else:
        result = results[(y, x)] if (y, x) in results else solve(y, x)
        results[(y, x)] = result
        return result

result2 = solve(*beam)
result1 = len(splitters_used)

print(result1, result2)
