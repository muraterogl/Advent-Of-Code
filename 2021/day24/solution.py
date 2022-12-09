from os import path
from sys import setrecursionlimit
from copy import deepcopy
from collections import Counter
import numpy as np
import functools

setrecursionlimit(9**9)
#with open(path.join(path.dirname(__file__), "input.txt")) as f:
with open("./input.txt") as f:    
    ins = [x.split() for x in f.read().splitlines()]

insLen = len(ins)
part1 = True
def rrange(): 
    return range(9,0,-1) if part1 else (1,10)
@functools.lru_cache(maxsize=None)
def find(ins_ix, x, y, z, w):
    #print(ins_ix, x,y,z,w)
    if z>10**7:
        return False,''
    if ins_ix >= insLen:
        return z==0, ''

    values = {"x":x, "y":y, "z":z, "w":w}

    op, *params = ins[ins_ix]

    if op=="inp":
        for n in rrange():
            values[params[0]]=n
            ok, rest = find(ins_ix+1, *values.values())
            if ok:
                return True, str(n)+rest
        return False, ''
    param1 = params[0]
    param2 = values[params[1]] if params[1] in values else int(params[1])

    if op=="add":
        values[param1] += param2
    elif op=="mul":
        values[param1] *= param2
    elif op=="div":
        if param2==0:
            return False, ''
        values[param1] //= param2
    elif op=="mod":
        if values[param1]<0 or param2<=0:
            return False, ''
        values[param1] %= param2
    else:
        values[param1] = 1 if values[param1] == param2 else 0
    #print("here")
    return find(ins_ix+1, *values.values())

print("part1: ", find(0,0,0,0,0))
part1 = False
print("part2: ", find(0,0,0,0,0))
