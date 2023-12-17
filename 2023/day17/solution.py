import heapq

with open("input.txt") as f:
    grid = [[*map(int,line)] for line in f.read().split("\n")]
h = len(grid)
w = len(grid[0])
dir_y={0:0,1:1,2:0,3:-1}
dir_x={0:1,1:0,2:-1,3:0}

def solve(min_l, max_l):
    seen = {}
    q = [(grid[0][1],0,1,0,1), (grid[1][0],1,0,1,1)]
    while q:
        cost, cy, cx, cd, i = heapq.heappop(q)
        if i<max_l and ((cy,cx,cd,i) not in seen or seen[(cy,cx,cd,i)] > cost):
            seen[(cy,cx,cd,i)] = cost
            if cy==h-1 and cx==w-1 and i>min_l-2:
                return cost
            for dd in [-1,0,1]:
                d = (dd + cd) % 4
                y = cy + dir_y[d]
                x = cx + dir_x[d]
                if 0<=y<h and 0<=x<w and (i>min_l-2 or dd==0):
                    heapq.heappush(q, (cost+grid[y][x],y,x,d,[0,i+1][d==cd]))

print("part 1:", solve(0, 3))
print("part 2:", solve(4, 10))
