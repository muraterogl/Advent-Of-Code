with open("input.txt") as f:
    grid = f.read().split("\n")
h = len(grid)
w = len(grid[0])
dirs = {".":{0:[(0,1,0)],1:[(1,0,1)],2:[(0,-1,2)],3:[(-1,0,3)]},
        "|":{0:[(1,0,1),(-1,0,3)],1:[(1,0,1)],2:[(1,0,1),(-1,0,3)],3:[(-1,0,3)]},
        "-":{0:[(0,1,0)],1:[(0,1,0),(0,-1,2)],2:[(0,-1,2)],3:[(0,1,0),(0,-1,2)]},
        "/":{0:[(-1,0,3)],1:[(0,-1,2)],2:[(1,0,1)],3:[(0,1,0)]},
        "\\":{0:[(1,0,1)],1:[(0,1,0)],2:[(-1,0,3)],3:[(0,-1,2)]}}

def solve(initial=(0,0,0)):
    seen = set()
    q = [initial]
    while q:
        cy, cx, cd = q.pop(0)
        if 0<=cy<h and 0<=cx<w and (cy, cx, cd) not in seen:
            seen.add((cy, cx, cd))
            for dy, dx, nd in dirs[grid[cy][cx]][cd]:
                q.append((cy+dy, cx+dx, nd))
    return len(set([(y, x) for y,x,_ in seen]))


part1=solve((0,0,0))
print("part 1:", part1)
initials=[(i,0,0)for i in range(h)]+[(i,w-1,2)for i in range(h)]+\
[(0,i,1)for i in range(w)]+[(h-1,i,3)for i in range(w)]
part2=max([solve(initial) for initial in initials])
print("part 2:", part2)
