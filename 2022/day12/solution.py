with open("input.txt") as f:
    m=f.read().split("\n")
length=len(m)
width=len(m[0])

def solve(sx,sy,fx,fy):
    seen=set()        
    queue = [(sx,sy,0)]
    height = lambda x,y:ord(m[y][x].replace("S","a").replace("E","z"))
    max_close = 0
    while queue:
        cx,cy,cl=queue.pop(0)
        if cx==fx and cy==fy:
            return cl
            break
        if not (cx,cy) in seen:
            seen.add((cx,cy))
            for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                if 0<=cx+dx<width and 0<=cy+dy<length and height(cx+dx,cy+dy)<=height(cx,cy)+1:
                    if m[cy+dy][cx+dx]=="a":
                        max_close = cl
                    queue.append((cx+dx,cy+dy,cl+1))
                    
sx=sy=fx=fy=-1
for y in range(length):
    if "S" in m[y]:
        sx=m[y].index("S")
        sy=y
    if "E" in m[y]:
        fx=m[y].index("E")
        fy=y
                    
print(f"Part1: {solve(sx,sy,fx,fy)}")
a = []
for y in range(length):
    for x in range(width):
        if m[y][x]=="a":
            a.append((x,y))
print(f"Part2: {min(solve(x,y,fx,fy) or 1e9 for x,y in a)}")
