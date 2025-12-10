import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

with open('input.txt') as f:
    lines = f.read().split("\n")

result1 = 0
result2 = 0

for line in lines:
    goal, *buttons, _ = line.replace(")",",)").split()
    goal = int("".join("0" if c=="." else "1" for c in goal[1:-1]),2)
    *buttons, = map(eval, buttons)
    N = max(max(t) for t in buttons)
    buttons = [sum(1<<(N-i) for i in button)for button in buttons]
    seen = set()
    q = [(0, tuple(0 for _ in range(len(buttons))))]
    while q:
        current, counts = q.pop(0)
        if counts in seen:
            continue
        seen.add(counts)
        if current == goal:
            result1 += sum(counts)
            break
        for i, button in enumerate(buttons):
            q.append((current^button, tuple(count+1 if i==j else count for j,count in enumerate(counts))))

for line in lines:
    _, *buttons, goal = line.replace(")",",)").split()
    goal = eval(goal.replace("{","(").replace("}",")"))
    *buttons, = map(eval, buttons)
    N = max(max(t) for t in buttons)
    buttons = [tuple(1 if i in button else 0 for i in range(N+1)) for button in buttons]
    A = np.array(buttons).transpose()
    b = np.array(goal)
    c = np.ones(len(buttons))
    
    result = milp(
        c=c,
        constraints=[LinearConstraint(A,b,b)],
        bounds=Bounds(0, np.inf),
        integrality=np.ones(len(buttons))
    )
    result2 += sum(np.round(result.x).astype(int))


        
              
print(result1, result2)
