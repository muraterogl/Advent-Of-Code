with open("input.txt") as f:
    room, moves = f.read().split("\n\n")
part1 = part2 = 0

moves = "".join(moves.split("\n"))
room = room.split("\n")
h = len(room)
w = len(room[0])
walls = set()
boxes = set()
robot = (-1, -1)
for y in range(h):
    for x in range(w):
        if room[y][x] == "#":
            walls.add((y,x))
        elif room[y][x] == "O":
            boxes.add((y,x))
        elif room[y][x] == "@":
            robot = (y, x)

def can_move(x, y, dx, dy):
    global boxes
    global walls
    if (y+dy,x+dx) in walls:
        return False
    if (y+dy,x+dx) in boxes:
        return can_move(x+dx, y+dy, dx, dy)
    else:
        return True
def move_element(x,y,dx,dy):
    global boxes
    global robot
    if (y+dy, x+dx) in boxes:
        move_element(x+dx, y+dy, dx, dy)
    if (y,x) in boxes:
        boxes.remove((y,x))
        boxes.add((y+dy, x+dx))
    elif (y, x) == robot:
        robot = (robot[0]+dy, robot[1]+dx)
    

def print_room():
    print("**"*w)
    for y in range(h):
        print("".join(["#"if (y,x) in walls else "O" if (y,x) in boxes else "@" if (y,x)==robot else "."for x in range(w)]))
    print("**"*w)
    
for move in moves:
    dy, dx = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}[move]
    if can_move(robot[1], robot[0], dx, dy):
        move_element(robot[1], robot[0], dx, dy)
    # print(move)
    # print_room()

for y,x in boxes:
    part1 += 100*y + x

walls = set()
boxes = set()
right_boxes = set()
robot = (-1, -1)
for y in range(h):
    for x in range(w):
        if room[y][x] == "#":
            walls.add((y,2*x))
            walls.add((y,2*x+1))
        elif room[y][x] == "O":
            boxes.add((y,2*x))
            right_boxes.add((y,2*x+1))
        elif room[y][x] == "@":
            robot = (y, 2*x)

def can_move2(x, y, dx, dy):
    global boxes
    global walls
    if (y+dy,x+dx) in walls:
        return False
    elif (y+dy,x+dx) in boxes:
        return can_move2(x+dx, y+dy, dx, dy) and (dx!=0 or can_move2(x+1+dx, y+dy, dx, dy))
    elif (y+dy,x+dx) in right_boxes:
        return can_move2(x+dx, y+dy, dx, dy) and (dx!=0 or can_move2(x-1+dx, y+dy, dx, dy))
    else:
        return True
def move_element2(x,y,dx,dy):
    global boxes
    global robot
    if (y+dy, x+dx) in boxes:
        move_element2(x+dx, y+dy, dx, dy)
        if dx==0:
            move_element2(x+1+dx, y+dy, dx, dy)
    elif (y+dy, x+dx) in right_boxes:
        move_element2(x+dx, y+dy, dx, dy)
        if dx==0:
            move_element2(x-1+dx, y+dy, dx, dy) 
    if (y,x) in boxes:
        boxes.remove((y,x))
        boxes.add((y+dy, x+dx))
    if (y,x) in right_boxes:
        right_boxes.remove((y,x))
        right_boxes.add((y+dy, x+dx))
    elif (y, x) == robot:
        robot = (robot[0]+dy, robot[1]+dx)
    

def print_room2():
    print("**"*(2*w))
    for y in range(h):
        print("".join(["#"if (y,x) in walls else "[" if (y,x) in boxes else "]" if (y,x) in right_boxes else "@" if (y,x)==robot else "."for x in range(2*w)]))
    print("**"*(2*w))
    
for move in moves:
    dy, dx = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}[move]
    if can_move2(robot[1], robot[0], dx, dy):
        move_element2(robot[1], robot[0], dx, dy)
    #print(move)
    #print_room2()

for y,x in boxes:
    part2 += 100*y + x

print(part1, part2)
