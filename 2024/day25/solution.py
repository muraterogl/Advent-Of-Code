with open("input.txt") as f:
    lines = f.read().split("\n\n")
part1 = part2 = 0

def count_item(item):
    return [("".join(l)).count("#")-1 for l in zip(*item.split("\n"))]

*locks, = map(count_item,[line for line in lines if line[0]=="#"])
*keys, = map(count_item,[line for line in lines if line[0]!="#"])

for lock in locks:
    for key in keys:
        if all(k+l<6 for k,l in zip(key,lock)):
            part1+=1
            
print(part1)
