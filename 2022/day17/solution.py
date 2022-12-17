with open("input.txt") as f:
    commands = list(f.read())

max_h = 0
c = 0
l = len(commands)
board = set()
cache = {}
done1 = done2 = False
def get_shape(i):
    return [
    [(2,max_h+3),(3,max_h+3),(4,max_h+3),(5,max_h+3)],
    [(2,max_h+4),(3,max_h+3),(4,max_h+4),(3,max_h+5)],
    [(2,max_h+3),(3,max_h+3),(4,max_h+3),(4,max_h+4),(4,max_h+5)],
    [(2,max_h+3),(2,max_h+4),(2,max_h+5),(2,max_h+6)],
    [(2,max_h+3),(2,max_h+4),(3,max_h+3),(3,max_h+4)]
    ][i%5]

def shift(shape, dir):
    dx = -1 if dir=="<" else 1 if dir==">" else 0
    dy = -1 if dir=="v" else 0
    stuck = False
    if all((x+dx,y+dy) not in board and
           0<=x+dx<7                and
           0<=y+dy         
                                    for x,y in shape):
        shape = [(x+dx, y+dy) for x,y in shape]
    else:
        stuck = True
    return shape, stuck

for i in range(10**12):
    if i==2022:
        print(f"Part1: {max_h}")
        done1 = True
    s = get_shape(i)

    key = i%5, c%l
    if key in cache:
        prev_i, prev_h = cache[key]
        if not done2 and (10**12-i)%(i-prev_i)<1:
            print(f"Part2: {max_h+(max_h-prev_h) * (10**12-i)//(i-prev_i)}")
            done2 = True
    else:
        cache[key] = i, max_h

    if done1 and done2:
        exit()

    while True:
        s, _ = shift(s, commands[c%l])
        c+=1
        s, stuck = shift(s, "v")
        if stuck:
            board |= set((x,y) for x,y in s)
            max_h = max(max_h, max(y for _,y in s)+1)
            break
