with open("input.txt") as f:
    lines = f.read().split("\n")

monkeys = {}
for line in lines:
    name, op = line.split(": ")
    monkeys[name] = op

def find_op(var):
    result = []
    for x in var.split():
        if x.isdigit() or x in "+-*/ğ==":
            result.append(x.replace("/","//"))
        else:
            inside = f"({find_op(monkeys[x])})"
            try:
                inside = str(eval(inside))
            except:
                pass
            result.append(inside)
    return " ".join(result)

print(f"Part1: {eval(find_op(monkeys['root']))}")

monkeys["root"] = monkeys["root"].replace("+","==")
monkeys["humn"] = "ğ"

op = find_op(monkeys['root'])

exp, result = op.split(" == ")
result = int(result)
exp = exp[1:-1]
while exp != "ğ":
    if exp[0]=="(":
        a,b = exp.rsplit(")",1)
        a += ")"
        op, b = b[1:].split()
    else:
        a,b = exp.split("(",1)
        b = "("+b
        a, op = a[:-1].split()
    if a[0]=="(":
        if op=="+":
            result -= int(b)
        elif op=="-":
            result += int(b)
        elif op=="*":
            result //= int(b)
        else:
            result *= int(b)
        exp = a[1:-1]
    else:
        if op=="+":
            result -= int(a)
        elif op=="-":
            result = int(a)-result
        elif op=="*":
            result //= int(a)
        else:
            result = int(a)//result
        exp = b[1:-1]

print(f"Part2: {result}")
