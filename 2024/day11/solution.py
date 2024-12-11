with open("input.txt") as f:
    line = f.read()
part1 = part2 = 0

l = list(map(int, line.split()))
c = {}

def solve(times, n):
    if n in c and times in c[n]:
        return c[n][times]
    if not n in c:
            c[n] = {}
    l = len(str(n))
    if n==0:
        c[n][times] = 1 if times==1 else solve(times-1, 1)
    elif l%2==0:
        c[n][times] = 2 if times==1 else solve(times-1, int(str(n)[:l//2])) + solve(times-1, int(str(n)[l//2:]))
    else:
        c[n][times] = 1 if times==1 else solve(times-1, n*2024)
    return c[n][times]

part1 = sum(solve(25, n) for n in l)
part2 = sum(solve(75, n) for n in l)
print(part1, part2)
