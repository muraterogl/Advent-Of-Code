with open("input.txt") as f:
    lines = f.read().split("\n")
    
x=1
willBeAdded=None
state=0 #0 => initial, 1 => during adding
part1=0
screen=[["."for _ in range(40)]for _ in range(6)]

def fillScreen(cycle, x):
    ys = (cycle-1)//40
    xs = (cycle-1)%40
    screen[ys][xs] = "#" if abs(xs-x)<2 else " "
def drawScreen():
    for line in screen:
        print("".join(line))
        
cycle = 0     
while lines:
    cycle += 1
    if state or lines[0]=="noop":
        command = lines.pop(0)
        if command != "noop":
            willBeAdded=int(command.split()[1])
            state=0
    else:
        state=1
    if cycle in [20,60,100,140,180,220]:
        part1+=cycle*x
    fillScreen(cycle,x)
    if willBeAdded:
        x+=willBeAdded
        willBeAdded=None

        
print(f"Part1: {part1}")
drawScreen()
