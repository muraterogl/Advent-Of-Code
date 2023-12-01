import re

def text_to_number(x):
    return x if x.isdigit() else str(["zero","one","two","three","four","five","six","seven","eight","nine"].index(x))

with open("input.txt") as f:
    lines = f.read().split("\n")

result = 0

for line in lines:
    f = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)[0]
    l = re.findall(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1])[0][::-1]
    number = int(text_to_number(f) + text_to_number(l))
    result += number

print(result)
