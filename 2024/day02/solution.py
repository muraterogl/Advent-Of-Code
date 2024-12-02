with open("input.txt") as f:
    lines = [list(map(int, line.split())) for line in f.read().split("\n")]


def is_safe(line):
    decreasing = False
    if line[0] > line[1]:
        decreasing = True
    for i in range(len(line)-1):
        if decreasing:
            if 1 <= line[i] - line[i+1] <= 3:
                pass
            else:
                return False
        else:
            if 1 <= line[i+1] - line[i] <= 3:
                pass
            else:
                return False
    return True

part1 = sum(is_safe(line) for line in lines)
part2 = 0
for line in lines:
    if is_safe(line):
        part2 += 1
    else:
        for i in range(len(line)):
            if is_safe(line[:i] + line[i+1:]):
                part2+=1
                break


print(part1, part2)
