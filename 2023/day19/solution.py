import math

with open("input.txt") as f:
    wfs, parts = f.read().split("\n\n")

parts=[eval(part.replace("=","':").replace(",",",'").replace("{","{'"))for part in parts.split("\n")]
wfd ={}
for wf in wfs.split("\n"):
    name, rest = wf.split("{")
    conditions = rest[:-1].split(",")
    conditions = [c.split(":")for c in conditions]
    wfd[name]=conditions

p1=0
for p in parts:
    cn = "in"
    while True:
        for c in wfd[cn]:
            if len(c)==1: cn =c[0]
            else:
                ch=c[0][0]
                s,n=c[0][1],int(c[0][2:])
                if s=="<" and p[ch]< n:
                    cn=c[1]
                    break
                elif s==">" and p[ch]>n:
                    cn=c[1]
                    break
        if cn=="A":
            p1 += sum(v for k,v in p.items())
            break
        elif cn=="R":
            break
print("part 1:", p1)
p = {c:[1,4000] for c in "xmas"}
def part2(cn, p):
    result = []
    for c in wfd[cn]:
        if len(c)==1:
            if c[0]=="R":
                return result
            elif c[0]=="A":
                return result + [p]
            else:
                return result + part2(c[0], p)
        else:
            ch = c[0][0]
            s,n=c[0][1],int(c[0][2:])
            if s=="<" and p[ch][0] < n:
                if c[1]=="A":
                    result += [{k:([v[0], n-1] if k==ch else v) for k,v in p.items()}]
                elif c[1] != "R":
                    result += part2(c[1], {k:([v[0], n-1] if k==ch else v) for k,v in p.items()})
                p = {k:([n, v[1]] if k==ch else v) for k,v in p.items()}
            elif s==">" and p[ch][1] > n:
                if c[1]=="A":
                    result += [{k:([n+1, v[1]] if k==ch else v) for k,v in p.items()}]
                elif c[1]!="R":
                    result += part2(c[1], {k:([n+1, v[1]] if k==ch else v) for k,v in p.items()})
                p = {k:([v[0], n] if k==ch else v) for k,v in p.items()}
p2 = part2("in", p)

print("part 2:", sum([math.prod([v[1]-v[0]+1 for _,v in p.items()]) for p in p2]))
