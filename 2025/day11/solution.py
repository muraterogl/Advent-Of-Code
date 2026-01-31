from functools import cache

with open('input.txt') as f:
    lines = f.read().split("\n")

result1 = 0
result2 = 0

paths = {}
for line in lines:
    a, b = line.split(": ")
    b = b.split()
    paths[a] = b

@cache
def solve(n, dac, fft):
    if n == "out" and dac and fft:
        return 1
    return sum(solve(path, dac or n=="dac", fft or n=="fft")for path in paths.get(n, []))

result1 = solve("you", True, True)
result2 = solve("svr", False, False)
print(result1, result2)
