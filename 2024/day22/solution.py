with open("input.txt") as f:
    lines = f.read().split("\n")
part1 = part2 = 0

def next_sn(n):
    n = (n^(n*64)) % 16777216
    n = (n^(n//32)) % 16777216
    n = (n^(n*2048)) % 16777216
    return n

l = []
for i, line in enumerate(lines):
    n = int(line)
    l.append([(n%10, 0)])
    for j in range(1999):
        n = next_sn(n)
        l[i].append((n%10, (n%10)-l[i][-1][0]))
    part1 += n

sequences = {}

for ll in l:
    for i in range(1, len(ll)-3):
        sequence = (ll[i][1],  ll[i+1][1], ll[i+2][1], ll[i+3][1])
        sequences[sequence] = 0


for ll in l:
    seen = set()
    for i in range(1, len(ll)-3):
        sequence = (ll[i][1],  ll[i+1][1], ll[i+2][1], ll[i+3][1])
        if sequence not in seen:
            seen.add(sequence)
            sequences[sequence] += ll[i+3][0]

        
part2 = max(sequences.items(), key=lambda s: s[1])

print(part1, part2)
