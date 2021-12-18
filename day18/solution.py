from collections import Counter
from math import floor, ceil
with open('day18/input.txt') as f:q=f.readlines()

class Number:
    def __init__(self,number, depth):
        self.number = number
        self.depth = depth
    def copy(self):
        return Number(self.number, self.depth)


numbers = []
for line in q:
    currentDepth = -1
    number = []
    for c in line.rstrip():
        if c=="[":
            currentDepth += 1
        elif c=="]":
            currentDepth -= 1
        elif c==",":
            pass
        else:
            number.append(Number(int(c), currentDepth))
    numbers.append(number)

def reduceNumber(x):
    n = [i.copy() for i in x]
    while True:
        foundToReduce = False
        for i in range(len(n)):
            if n[i].depth >= 4:
                if i!=0:
                    n[i-1].number += n[i].number
                if i!=len(n)-2:
                    n[i+2].number += n[i+1].number
                n = n[:i] + [Number(0, 3)] + n[i+2:]
                foundToReduce = True
                break
        if foundToReduce:
            continue

        for i in range(len(n)):
            if n[i].number>9:
                x = n[i].number
                d = n[i].depth
                n = n[:i] + [Number(floor(x/2), d+1), Number(ceil(x/2), d+1)] + n[i+1:]
                foundToReduce = True
                break
        if not foundToReduce:
            break
    return n

def sumNumbers(x1, x2):
    n1=[i.copy() for i in x1]
    n2=[i.copy() for i in x2]
    result = []
    for i in range(len(n1)):
        n1[i].depth += 1
        result.append(n1[i])
    for i in range(len(n2)):
        n2[i].depth += 1
        result.append(n2[i])
    return result

def magnitude(x):
    n = x.copy()
    while len(n)!=1:
        lowestDepth = -999
        for i in range(len(n)):
            lowestDepth = max(n[i].depth, lowestDepth)
        for i in range(len(n)):
            if n[i].depth==lowestDepth and i==len(n)-1:
                n = n[:i] + [Number(n[i].number, lowestDepth-1)] + n[i+2:]
                break
            elif n[i].depth==lowestDepth and n[i+1].depth==lowestDepth:
                n = n[:i] + [Number(3*n[i].number+2*n[i+1].number, lowestDepth-1)] + n[i+2:]
                break
        
    return n[0].number


part1Result = numbers[0].copy()
for i in range(1, len(numbers)):
    x = sumNumbers(part1Result, numbers[i])
    part1Result = reduceNumber(x)

print(f"part1: {magnitude(part1Result)}")

mSum = -9999
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i!=j:
            x = sumNumbers(numbers[i], numbers[j])
            y = reduceNumber(x)
            mSum = max(mSum, magnitude(y))


print(f"part2: {mSum}")