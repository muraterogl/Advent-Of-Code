import math

with open("input.txt") as f:
    seeds, *transformations = f.read().split("\n\n")

*seeds, = map(int, seeds.split()[1:])
seeds_range = [[seeds[i], seeds[i+1]+seeds[i]-1]for i in range(0, len(seeds), 2)]

for transformation in transformations:
    transformation = transformation.split("\n")[1:]
    transformation = [[*map(int, line.split())]for line in transformation]
    for i, seed in enumerate(seeds):    
        for target, source, rrange in transformation:
            if source <= seed < source+rrange:
                diff = target - source
                seeds[i] = seed + diff
                break

print("part 1:", min(seeds))


for transformation in transformations:
    transformation = transformation.split("\n")[1:]
    transformation = [[*map(int, line.split())]for line in transformation]
    new_seed_range = []
    while seeds_range:
        seed_range_start, seed_range_end = seeds_range[0]
        for target, source, rrange in transformation:
            diff = target - source
            if seed_range_start >= source and seed_range_end < source+rrange:
                new_seed_range.append([seed_range_start+diff, seed_range_end+diff])
                seeds_range.pop(0)
                break
            elif seed_range_start >= source and seed_range_start < source+rrange and seed_range_end >= source+rrange:
                new_seed_range.append([seed_range_start+diff, source+rrange-1+diff])
                seeds_range[0][0] = source+rrange
                break
            elif seed_range_start < source and seed_range_end >= source and seed_range_end < source+rrange:
                new_seed_range.append([source+diff, seed_range_end+diff])
                seeds_range[0][1] = source-1
                break
            elif seed_range_start < source and seed_range_end >= source+rrange:
                new_seed_range.append([source+diff, source+rrange-1+diff])
                seeds_range[0][0] = source+rrange
                seeds_range.append([seed_range_start, source-1])
                break

        if seeds_range and seeds_range[0][0] == seed_range_start and seeds_range[0][1] == seed_range_end:
            new_seed_range.append(seeds_range.pop(0))
    seeds_range = new_seed_range.copy()

print("part 2:", min(start for start, end in seeds_range))

