from collections import Counter
with open('day14/input.txt') as f:q=f.readlines()

template, _ , *q = q

template = template.rstrip()
rules = {}
for l in q:
    a,b = l.split(" -> ")
    rules[a] = b.rstrip()

letters = Counter(template)
pairs = Counter([template[i-1]+template[i] for i in range(1, len(template))])


for step in range(40):
    pairsCopy = pairs.copy()
    for rule in rules:
        c = pairsCopy[rule]
        pairs[rule] -= c
        pairs[rule[0]+rules[rule]] += c
        pairs[rules[rule]+rule[1]] += c
        letters[rules[rule]] += c
    if step==9:
        x = letters.most_common()
        print(f"part1: {x[0][1]-x[-1][1]}")

x = letters.most_common()
print(f"part2: {x[0][1]-x[-1][1]}")