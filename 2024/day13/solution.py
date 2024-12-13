with open("input.txt") as f:
    buttons_list = f.read().split("\n\n")
part1 = part2 = 0

def solve(ax, bx, ay, by, px, py):
    # [ax bx] [a] [px]
    # [ay by] [b] [py]
    d_ = ax*by-bx*ay
    a = px*by/d_ - py*bx/d_
    b = -px*ay/d_ + py*ax/d_
    def is_close(a1, a2):
        return abs(a1-a2) < 0.0001
    if is_close(a, round(a)) and is_close(b, round(b)):
        return 3*round(a) + round(b)
    else:
        return 0


for buttons in buttons_list:
    ax, ay, bx, by, px, py = map(int, re.findall(r'\d+', buttons))
    part1 += solve(ax, bx, ay, by, px, py)
    part2 += solve(ax, bx, ay, by, 10000000000000+px, 10000000000000+py)

print(part1, part2)
