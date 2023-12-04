import math

with open("input.txt") as f:
    lines = f.read().split("\n")

part1 = 0
winning_counts = {}
for i, line in enumerate(lines):
    winning, mycards = line.split(" | ")
    winning = winning.split()[2:]
    mycards = mycards.split()
    same = len({*winning} & {*mycards})
    winning_counts[i+1] = same
    part1 += 2**~-same if same>0 else 0

print(part1)


won_cards = [1 for _ in range(len(lines))]

for i, count in enumerate(won_cards):
    won = winning_counts[i+1]
    for j in range(i+1, i+won+1):
        won_cards[j] += count

print(sum(won_cards))
