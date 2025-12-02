with open('input.txt') as f:
    lines = f.read().split("\n")

position = 50
result1 = 0
result2 = 0
for line in lines:
    direction, num = line[0], int(line[1:])
    if direction == "R":
        laps, position = divmod(position + num, 100)
        result2 += laps
    else:
        target = position - num
        result2 += (position - 1) // 100 - (target - 1) // 100
        position = target % 100
    result1 += position == 0
print(result1, result2)
