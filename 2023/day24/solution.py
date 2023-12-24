import numpy as np
import sympy

with open("input.txt") as f:
    lines = [[*map(int,line.replace("@ ","").replace(",","").split())]for line in f.read().split("\n")]

mi, ma = (7, 27) if len(lines)==5 else (200000000000000, 400000000000000)
part1 = 0
for i, line1 in enumerate(lines):
    for j, line2 in enumerate(lines):
        if i!=j:
            x1,y1,z1,vx1,vy1,vz1 = line1
            x2,y2,z2,vx2,vy2,vz2 = line2
            # t1 * vx1 + x1 = t2 * vx2 + x2
            # t1 * vx1 - t2 * vx2 + x1 - x2 = 0
            # t1 * vy1 - t2 * vy2 + y1 - y2 = 0    
            try:
                t1, t2 = np.linalg.solve(np.array([[vx1, -vx2],[vy1, -vy2]]), np.array([x2-x1,y2-y1]))
                x = t1 * vx1 + x1
                y = t1 * vy1 + y1
                if 0 <= t1 and 0 <= t2 and mi <= x <= ma and mi <= y <= ma:
                    part1 += 1
            except:
                pass
print("part 1:", part1//2)

# t1 * vx1 + x1 = t1 * vx + x
# t1 * vy1 + y1 = t1 * vy + y
# t1 * vz1 + z1 = t1 * vz + z
(x1,y1,z1,vx1,vy1,vz1),(x2,y2,z2,vx2,vy2,vz2),(x3,y3,z3,vx3,vy3,vz3),*_ = lines
x, y, z, vx, vy, vz, t1, t2, t3 = sympy.symbols("x y z vx vy vz t1 t2 t3", real=True)
equations = [
    sympy.Eq(x + vx * t1, x1 + vx1 * t1),
    sympy.Eq(y + vy * t1, y1 + vy1 * t1),
    sympy.Eq(z + vz * t1, z1 + vz1 * t1),
    sympy.Eq(x + vx * t2, x2 + vx2 * t2),
    sympy.Eq(y + vy * t2, y2 + vy2 * t2),
    sympy.Eq(z + vz * t2, z2 + vz2 * t2),
    sympy.Eq(x + vx * t3, x3 + vx3 * t3),
    sympy.Eq(y + vy * t3, y3 + vy3 * t3),
    sympy.Eq(z + vz * t3, z3 + vz3 * t3),
]
sol = sympy.solve(equations)[0]
print("part 2:", sol[x]+sol[y]+sol[z])
