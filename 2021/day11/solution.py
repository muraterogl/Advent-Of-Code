with open('day11/input.txt') as f:q=f.readlines()

octopuses = [[*map(int, list(line.rstrip()))]for line in q]
H = len(octopuses)
W = len(octopuses[0])
totalFlash = 0
step = 1
synchronizingHappened = False
while True:
    flashesInThisStep = set()
    flashQueue = []
    for y in range(H):
        for x in range(W):
            if octopuses[y][x]<9: octopuses[y][x] += 1
            else:
                octopuses[y][x] = 0
                flashQueue.append((y,x))
    while flashQueue:
        y,x = flashQueue[0]
        flashQueue=flashQueue[1:]
        flashesInThisStep.add((y,x))
        for k in range(max(0,y-1), min(H,y+2)):
            for l in range(max(0,x-1), min(W,x+2)):
                if (k!=y or l!=x) and (k,l) not in flashesInThisStep:
                    if octopuses[k][l]==0:
                        continue
                    elif octopuses[k][l]<9: octopuses[k][l] += 1
                    else:
                        octopuses[k][l] = 0
                        flashQueue.append((k,l))
        
    totalFlash += len(flashesInThisStep)
    if step == 100:
        print(f"part1: {totalFlash}")
    if all(all(i==0 for i in y) for y in octopuses):
        print(f"part2: {step}")
        synchronizingHappened = True
    if synchronizingHappened and step>=100:
        break
    step += 1