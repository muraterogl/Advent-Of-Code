with open("input.txt") as f:
    line = f.read()

part1 = part2 = 0

files = line[::2]
empty = line[1::2]
total_len = sum(map(int,files))
files_with_id = [*zip(range(len(files)), map(int,files))]
result = []
while files_with_id:
    result += files_with_id[0],
    files_with_id = files_with_id[1:]
    c = int(empty[0])
    empty = empty[1:]
    while c>0 and files_with_id:
        if c >= files_with_id[-1][1]:
            c -= files_with_id[-1][1]
            result += files_with_id[-1],
            files_with_id = files_with_id[:-1]
        else:
            result += (files_with_id[-1][0], c),
            files_with_id[-1] = (files_with_id[-1][0], files_with_id[-1][1]-c)
            break
i = 0
for ix, c in result:
    for _ in range(c):
        part1 += i * ix
        i += 1

files_with_id = [*zip(range(len(files)), map(int,files))]
x = 0
empty = [[int(i)] for i in line[1::2]]
moved = 0
for i in range(len(files_with_id)-1, 0, -1):
    for x in range(min(len(empty), i)):
        if files_with_id[i][0]!=0 and empty[x][-1] >= files_with_id[i][1]:
            empty[x].insert(len(empty[x])-1, files_with_id[i])
            files_with_id[i] = (0, files_with_id[i][1])
            empty[x][-1] -= files_with_id[i][1]
        
i=0
for a,b in zip(files_with_id, empty):
    for _ in range(a[1]):
        part2 += i * a[0]
        i += 1
    *x, c = b
    for m in x:
        for _ in range(m[1]):
            part2 += i * m[0]
            i += 1
    i += c
print(part1, part2)
