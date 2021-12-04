with open('day4/input.txt') as f:q=f.readlines()

*numbers, = map(int, q[0].split(","))
q = q[1:]
boards = []
winners = []
for i in range(0, len(q), 6):
    board = [[*map(int, x)]for x in map(str.split,q[i+1:i+6])]
    emptyBoard = [[0 for _ in range(5)]for _ in range(5)]
    boards.append((board, emptyBoard))
    winners.append(False)

for n in numbers:
    for i in range(len(boards)):
        for x in range(5):
            for y in range(5):
                if boards[i][0][x][y] == n:
                    boards[i][1][x][y] = 1
                    if sum(boards[i][1][x]) == 5 or sum(m[y] for m in boards[i][1]) == 5:
                        #Bingo
                        board = boards[i][0]
                        emptyBoard = boards[i][1]
                        s = sum([boards[i][0][k][l]for l in range(5) for k in range(5) if boards[i][1][k][l]==0])
                        if all(not k for k in winners):
                            #first time
                            print(f"part1: {s*n}")
                        elif all(winners[k] or k==i for k in range(len(boards))):
                            #last time
                            print(f"part2: {s*n}")
                            exit()
                        winners[i] = True
