with open("input.txt") as f:
    lines = f.read()
part1 = part2 = 0
A,B,C,*program = map(int, re.findall(r'\d+',lines))
    
def run_program(A,B,C,program):
    A_ = A
    B_ = B
    C_ = C

    def combo_op(v):
        if 0 <= v < 4:
            return v
        elif v == 4:
            return A_
        elif v == 5:
            return B_
        elif v == 6:
            return C_
        else:
            raise KeyError
    ipointer = 0
    output = []
    l = len(program)
    while ipointer < l-1:
        ins, op = program[ipointer], program[ipointer+1]
        if ins == 0:
            A_ //= (2**combo_op(op))
        elif ins == 1:
            B_ ^= op
        elif ins == 2:
            B_ = combo_op(op) % 8
        elif ins == 3:
            if A_ != 0:
                ipointer = op - 2
        elif ins == 4:
            B_ ^= C_
        elif ins == 5:
            output += combo_op(op) % 8,
        elif ins == 6:
            B_ = A_ // (2**combo_op(op))
        elif ins == 7:
            C_ = A_ // (2**combo_op(op))
        ipointer += 2
    return output

part1 = ",".join(map(str, run_program(A,B,C, program)))

todo = [(len(program)-1, 0)]
possible = []
for pos, val in todo:
    for a in range(val*8, val*8+8):
        if run_program(a, 0, 0, program) == program[pos:]:
            todo += [(pos-1, a)]
            if pos == 0:
                possible += a,
part2 = min(possible)

print(part1, part2)
