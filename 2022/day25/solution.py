with open("input.txt") as f:
    lines= f.read().split("\n")

def five_to_ten(s):
    l = len(s)
    n = 0
    for i,x in enumerate(s):
        x = -2 if x=="=" else -1 if x=="-" else eval(x)
        n += 5 ** (l-i-1) * x
    return n

def ten_to_five(n):
    s = ""
    while n>0:
        n += 2
        s = "=-012"[n%5] + s
        n //= 5
    return s

def part1():
    return ten_to_five(sum(five_to_ten(line) for line in lines))


print(f"Part1: {part1()}")
