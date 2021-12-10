with open('day05/input.txt') as f:q=f.readlines()

lines = [[(int(n.split(",")[0]),int(n.split(",")[1])) for n in line.split(" -> ")]for line in q]
board = [[0 for _ in range(1000)]for _ in range(1000)]

for p1,p2 in lines:
    x,y = p1
    X,Y = p2
    if y==Y: #straight line
        x,X = sorted((x,X))
        for i in range(x, X+1):
            board[y][i] += 1
    elif x==X: #straight line
        y,Y = sorted((y,Y))
        for i in range(y, Y+1):
            board[i][x] += 1

print(f"part1: {sum(board[i][j]>1 for j in range(1000)for i in range(1000))}")

board = [[0 for _ in range(1000)]for _ in range(1000)]

for p1,p2 in lines:
    x,y = p1
    X,Y = p2
    if y==Y: #straight line
        x,X = sorted((x,X))
        for i in range(x, X+1):
            board[y][i] += 1
    elif x==X: #straight line
        y,Y = sorted((y,Y))
        for i in range(y, Y+1):
            board[i][x] += 1
    elif abs(Y-y)==abs(X-x): #diagonal line
        if x>X and y>Y:
            for i in range(x,X-1,-1):
                board[y+i-x][i] += 1
                    
        elif x>X and y<Y:
            for i in range(x,X-1,-1):
                board[y+x-i][i] += 1
                    
        elif x<X and y>Y:
            for i in range(x,X+1):
                board[y+x-i][i] += 1
                    
        else:
            for i in range(x,X+1):
                board[y+i-x][i] += 1
                    


print(f"part2: {sum(board[i][j]>1 for j in range(1000)for i in range(1000))}")