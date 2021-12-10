from statistics import median

with open('day10/input.txt') as f:q=f.readlines()

part1Points = {")":3, "]":57, "}":1197, ">":25137}
part2Points = {"(":1, "[":2, "{":3, "<":4}
opposites = {"(":")", "[":"]", "{":"}", "<":">"}
part1Score = 0
part2Scores = []
incomplete = []


for line in q:
    s = []
    foundError = False
    for c in line.rstrip():
        if c in "[{(<":
            s.append(c)
        elif opposites[s[-1]] == c:
            s.pop()
        else:
            foundError = True
            part1Score += part1Points[c]
            break
    if not foundError:
        incomplete.append(line)

print(f"part1: {part1Score}")



for line in incomplete:
    s = []
    score = 0
    for c in line.rstrip():
        if c in "[{(<":
            s.append(c)
        elif opposites[s[-1]] == c:
            s.pop()
        else:
            print("error")
    for c in reversed(s):
        score *= 5
        score += part2Points[c]
    part2Scores.append(score)

print(f"part2: {median(part2Scores)}")