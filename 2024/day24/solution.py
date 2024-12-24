with open("input.txt") as f:
    lines = f.read().split("\n\n")
part1 = part2 = 0
values = {}
for line in lines[0].split("\n"):
    k, v = line.split(": ")
    values[k] = int(v)

equations = lines[1].split("\n")

def find_whole_number(c, values):
    return int("".join(str(values[k]) for k in sorted((k for k in values.keys() if k[0]==c), reverse=True)), 2)

def p1(eqs, values):
    while eqs:
        new_eqs = []
        for eq in eqs:
            a, o, b, _, r = eq.split()
            if a in values and b in values:
                a = values[a]
                b = values[b]
                values[r] = {"AND":a&b, "OR":a|b, "XOR":a^b}[o]
            else:
                new_eqs.append(eq)
        eqs = new_eqs.copy()
    return find_whole_number("z", values)

def find(a, b, o, eqs):
    for eq in eqs:
        if eq.startswith(f"{a} {o} {b}") or eq.startswith(f"{b} {o} {a}"):
            return eq.split(" -> ").pop()


def p2(eqs):
    swapped = []
    c0 = None
    for i in range(45):
        n = str(i).zfill(2)
        m1 = n1 = r1 = z1 = c1 = None
        m1 = find("x"+n, "y"+n, "XOR", eqs)
        n1 = find("x"+n, "y"+n, "AND", eqs)
        if c0:
            r1 = find(c0, m1, "AND", eqs)
            if not r1:
                m1, n1 = n1, m1
                swapped += [m1, n1]
                r1 = find(c0, m1, "AND", eqs)
            z1 = find(c0, m1, "XOR", eqs)
            if m1 and m1[0]=="z":
                m1, z1 = z1, m1
                swapped += [m1, z1]
            if n1 and n1[0]=="z":
                n1, z1 = z1, n1
                swapped += [n1, z1]
            if r1 and r1[0]=="z":
                r1, z1 = z1, r1
                swapped += [r1, z1]
            c1 = find(r1, n1, "OR", eqs)
        if c1 and c1.startswith("z") and c1 != "z45":
            c1, z1 = z1, c1
            swapped += [c1, z1]
        c0 = c1 if c0 else n1
    return ",".join(sorted(swapped))


part1 = p1(equations.copy(), values.copy())
part2 = p2(equations)
print(part1, part2)
