from os import path
from copy import deepcopy

def printB(im):
    print(*[''.join(x).replace("1","#").replace("0",".") for x in im],sep="\n")
    print("------------------")

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ref, im = f.read().replace(".","0").replace("#","1").split("\n\n")
    im = [list(x)for x in im.splitlines()]
    #printB(im)

    for step in range(50):
        im2 = []
        for y in range(-1,len(im)+1):
            row = []
            for x in range(-1,len(im[0])+1):
                b = ""
                for k in range(y-1,y+2):
                    for l in range(x-1, x+2):
                        if 0<=k<len(im) and 0<=l<len(im[0]):
                            b+=im[k][l]
                        else:
                            b+= "1" if ref[0]=="1" and step%2==1 else "0"
                b = int(b, 2)
                row.append(ref[b])
            im2.append(row)
        im = deepcopy(im2)
        #printB(im)
        if step==1:
            print("Part 1:", sum(x.count("1")for x in im))
    print("Part 2:", sum(x.count("1")for x in im))