with open('input.txt') as f:
    lines = f.read().split("\n")

result1 = 0
result2 = 0

result1 = sum(eval(n_line[-1].join(n_line[:-1]))for n_line in zip(*[line.split() for line in lines]))
lines[-1] = lines[-1] + " "
sign = None
currentResult = "0"
for n_line in zip(*lines):
    if sign == None:
        sign = n_line[-1]
        if sign=="*":
            currentResult = "1"
    if all(x==' ' for x in n_line):
        result2 += int(currentResult)
        currentResult = "0"
        sign = None
    else:
        currentResult = str(eval(currentResult + sign + "".join(n_line[:-1])))
result2 += int(currentResult)   

print(result1, result2)
