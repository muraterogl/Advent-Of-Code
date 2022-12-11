import re
import numpy as np

with open('input.txt') as f:
    lines=f.read().split("\n")

class Monkey:
    def __init__(self, lines, relief):
        *self.items, = map(int, re.findall(r'\d+',lines[1]))
        self.op = eval("lambda old:"+lines[2].split("=")[1][1:])
        self.modulo = int(re.findall(r'\d+',lines[3])[0])
        self.throws = [int(re.findall(r'\d+',lines[5])[0]), int(re.findall(r'\d+',lines[4])[0])]
        self.inspected = 0
        self.relief = relief
    def throw(self, global_modulo):
        self.inspected += 1
        new = self.op(self.items.pop(0)) // self.relief
        return self.throws[(new%self.modulo)<1], (new%global_modulo if self.relief < 3 else new)

def solve(count, relief):
    monkeys = [Monkey(lines[i:i+7], relief) for i in range(0, len(lines), 7)]
    global_modulo = int(np.lcm.reduce([monkey.modulo for monkey in monkeys]))

    for _ in range(count):
        for monkey in monkeys:
            while monkey.items:
                who, item = monkey.throw(global_modulo)
                monkeys[who].items.append(item)

    *_,a,b=sorted([monkey.inspected for monkey in monkeys])
    return a*b


print(f"Part 1: {solve(20,3)}")
print(f"Part 2: {solve(10000,1)}")
