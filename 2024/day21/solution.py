from functools import lru_cache

with open("input.txt") as f:
    lines = f.read().split("\n")
part1 = part2 = 0

keypad = (
    ("7", "8", "9"),
    ("4", "5", "6"),
    ("1", "2", "3"),
    ("ğ", "0", "A")
)

directional = (
    ("ğ", "^", "A"),
    ("<", "v", ">")
)

@lru_cache
def shortest(pad, start, end):
    h = len(pad)
    w = len(pad[0])
    for y in range(h):
        for x in range(w):
            if pad[y][x] == start:
                start = (y, x)
            if pad[y][x] == end:
                end = (y, x)
    q = [(start[0], start[1], "", set())]
    min_len = 9e15
    results = []
    while q:
        cy, cx, cp, seen = q.pop(0)
        if (cy, cx) == end:
            l = len(cp)
            if l < min_len:
                min_len = l
                results = [cp+"A"]
            elif l == min_len:
                results += cp+"A",
            continue
        if (cy, cx) in seen:
            continue
        seen.add((cy, cx))
        for dy, dx in [(-1,0), (1,0), (0,1), (0,-1)]:
            y, x = cy+dy, cx+dx
            if 0<=y<h and 0<=x<w and pad[y][x] != "ğ":
                q += (y, x, cp+{(-1,0):"^",(1,0):"v",(0,1):">",(0,-1):"<"}[(dy,dx)], seen.copy()),
    return tuple(results)

@lru_cache
def select_shortest(press, deep, last, max_deep):
    probs = shortest(directional if deep > 0 else keypad, last, press)
    if deep == max_deep:
        return len(probs[0])
    new_probs = []
    for prob in probs:
        word = 0
        last = "A"
        for c in prob:
            word += select_shortest(c, deep+1, last, max_deep)
            last = c
        new_probs += word,
    return min(new_probs)

for code in lines:
    result = 0
    last = "A"
    for c in code:
        part1 += select_shortest(c, 0, last, 2) * int(code[:-1])
        part2 += select_shortest(c, 0, last, 25) * int(code[:-1])
        last = c

print(part1, part2)
