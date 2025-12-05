with open('input.txt') as f:
    ranges, ings = map(str.split, f.read().split("\n\n"))

result1 = 0
result2 = 0
ranges = {tuple(map(int, ran.split("-"))) for ran in ranges}
for ing in ings:
    ing = int(ing)
    for l,h  in ranges:
        if l<=ing<=h:
            result1 += 1
            break

while True:
    new_ranges = set()
    no_change = True
    for l,h in ranges:
        found = False
        for ll, hh in new_ranges:
            if not (h < ll or l > hh):
                found = True
                no_change = False
                new_ranges.remove((ll, hh))
                new_ranges.add((min(ll,l), max(hh, h)))
        if not found:
            new_ranges.add((l,h))
    if no_change:
        break
    ranges = new_ranges

for l,h in ranges:
    result2 += h-l+1

print(result1, result2)
