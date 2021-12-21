from os import path
from collections import Counter
from itertools import product
import functools

allDices = Counter([sum(p) for p in product([1, 2, 3], repeat=3)])

def part1(player1Score, player2Score, player1Position, player2Position, diceCurrent, diceRolled):
    if player2Score >= 1000:
        return [player1Score, player2Score, diceRolled]
    roll = diceCurrent + diceCurrent+1 + diceCurrent+2
    diceCurrent += 3
    diceRolled += 3
    player1Position = (player1Position - 1 + roll) % 10 + 1
    a,b,c = part1(player2Score, player1Score+player1Position, player2Position, player1Position, diceCurrent, diceRolled)
    return b,a,c

@functools.lru_cache(maxsize=None)
def part2(player1Score, player2Score, player1Position, player2Position):
    if player2Score >= 21:
        return 0, 1
    player1Wins = 0
    player2Wins = 0
    for key, val in allDices.items():
            newPosition = (player1Position-1+key)%10+1
            a = part2(player2Score, player1Score + newPosition, player2Position, newPosition)
            player1Wins += val * a[1]
            player2Wins += val * a[0]
    return player1Wins, player2Wins


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    player1Position, player2Position = [int(line.split()[-1]) for line in f.read().splitlines()]
    p1 = part1(0, 0, player1Position, player2Position, 1, 0)
    print("Part 1:", min(p1[:2])* p1[-1])
    print("Part 2:", max(part2(0, 0, player1Position, player2Position)))

