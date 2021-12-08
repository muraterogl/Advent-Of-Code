with open('day8/input.txt') as f:q=f.readlines()

o = [x.split(" | ")[1].split() for x in q]

p1 = len([y for x in o for y in x  if len(y) in [2,3,4,7]])

print(f"part1: {p1}")

def sortedString(x):
    return "".join(sorted([i for i in x]))

result = 0

for line in q:
    outputs = line.split(" | ")[1].split()
    inputs = line.split(" | ")[0].split()
    d = {}
    d2 = {}

    def saveNumber(letters, n):
        d[n] = letters
        d2[sortedString(d[n])] = str(n)

    saveNumber([n for n in inputs if len(n)==2][0], 1)
    saveNumber([n for n in inputs if len(n)==3][0], 7)
    saveNumber([n for n in inputs if len(n)==4][0], 4)
    saveNumber([n for n in inputs if len(n)==7][0], 8)

    saveNumber([n for n in inputs if len(n)==6 and not all(i in n for i in d[1])][0], 6)
    saveNumber([n for n in inputs if len(n)==6 and all(i in n for i in d[4]) and n!=d[6]][0], 9)
    saveNumber([n for n in inputs if len(n)==6 and n not in [d[9], d[6]]][0], 0)

    saveNumber([n for n in inputs if len(n)==5 and all(i in n for i in d[1])][0], 3)

    #Possible 2 and 5
    a,b = [n for n in inputs if len(n)==5 and n != d[3]]
    x = {*a}-{*b}
    y = {*b}-{*a}
    if all(i in d[4] for i in x):
        saveNumber(a, 5)
        saveNumber(b, 2)
        
    else:
        saveNumber(a, 2)
        saveNumber(b, 5)

    result += int("".join(d2[sortedString(i)] for i in outputs))

print(f"part2: {result}")