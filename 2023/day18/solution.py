with open("input.txt") as f:
    ins = [ins.split() for ins in f.read().split("\n")]
dirs = {"R":1,"L":-1,"U":-1j,"D":1j,"0":1,"1":1j,"2":-1,"3":-1j}
def solve(ins):
    p,a=0,1
    for i in ins:
        p += i.real
        a += i.imag * p + abs(i)/2
    return int(a)

print("part 1:", solve(dirs[d]*int(s) for d,s,_ in ins))
print("part 2:", solve(dirs[c[7]]*int(c[2:7],16) for _,_,c in ins))
