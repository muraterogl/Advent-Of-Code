with open('input.txt') as f:
    lines = f.read().split("\n")

result1 = 0
result2 = 0

def solve(grid):
    to_be_removed = set()
    result = 0
    for y,x in grid:
        count = 0
        for dy in range(-1,2):
            for dx in range(-1,2):
                if (dy!=0 or dx!=0) and (y+dy,x+dx) in grid:
                    count += 1
        if count < 4:
            to_be_removed.add((y,x))
            result += 1

    return result, grid-to_be_removed

grid = {(y, x) for y, line in enumerate(lines) for x, char in enumerate(line) if char == '@'}
for i in range(999999999):
    result, grid = solve(grid)
    if result == 0: break
    result2 += result
    if i==0: result1 = result

print(result1, result2)
