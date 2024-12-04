with open("input.txt") as f:
    lines = f.read().split("\n")
width, height = len(lines[0]), len(lines)
part1 = part2 = 0

for h in range(height):
    for w in range(width):
        if lines[h][w] == "X":
            if w < width-3 and lines[h][w:w+4] == "XMAS":
                part1 += 1
            if w > 2 and lines[h][w-3:w+1] == "SAMX":
                part1 += 1
            if h < height-3 and lines[h+1][w] == "M" and lines[h+2][w] == "A" and lines[h+3][w] == "S":
                part1 += 1
            if h > 2 and lines[h-1][w] == "M" and lines[h-2][w] == "A" and lines[h-3][w] == "S":
                part1 += 1
            if w < width-3 and h < height-3 and lines[h+1][w+1] == "M" and lines[h+2][w+2] == "A" and lines[h+3][w+3] == "S":
                part1 += 1
            if w > 2 and h < height-3 and lines[h+1][w-1] == "M" and lines[h+2][w-2] == "A" and lines[h+3][w-3] == "S":
                part1 += 1
            if w < width-3 and h > 2 and lines[h-1][w+1] == "M" and lines[h-2][w+2] == "A" and lines[h-3][w+3] == "S":
                part1 += 1
            if w > 2 and h > 2 and lines[h-1][w-1] == "M" and lines[h-2][w-2] == "A" and lines[h-3][w-3] == "S":
                part1 += 1

for h in range(1, height-1):
    for w in range(1, width-1):
        if lines[h][w] == "A" and ((lines[h-1][w-1] == "S" and lines[h+1][w+1] == "M") or (lines[h-1][w-1] == "M" and lines[h+1][w+1] == "S")) \
                              and ((lines[h+1][w-1] == "S" and lines[h-1][w+1] == "M") or (lines[h+1][w-1] == "M" and lines[h-1][w+1] == "S")):
            part2 += 1
print(part1, part2)
