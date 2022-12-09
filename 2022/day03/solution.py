with open('input.txt') as f:
    lines=f.read().splitlines()

total = 0
total2 = 0

priority = lambda letter: ord(letter)%32 + 26*letter.isupper()

for line in lines:
    f, s = line[:len(line)//2], line[len(line)//2:]
    common = [*{*f}&{*s}][0]
    total += priority(common)

for i in range(0,len(lines),3):
    common = [*{*lines[i]}&{*lines[i+1]}&{*lines[i+2]}][0]
    total2 += priority(common)



print(f"Part 1: {total}")
print(f"Part 2: {total2}")
