import random
import string

with open("input.txt") as f:
    lines = f.read().split("\n")
    
fs = {"/":{}}
currentPath = []
part1 = 0
allFolderSizes = {}

def randomString():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(20))

def folderSize(f):
    global part1
    size = 0
    for x in f:
        if isinstance(f[x], int):
            size += f[x]
        else:
            selectedFolderSize = folderSize(f[x])
            allFolderSizes[x+randomString()] = selectedFolderSize
            size += selectedFolderSize
    if size <= 100000:
        part1 += size
        #print(size)
    return size
            
    
for line in lines:
    if line[0] == "$":
        _, *command = line.split()
        if command[0] == "cd":
            if command[1] == "/":
                currentPath = ["/"]
            elif command[1] == "..":
                currentPath.pop()
            else:
                currentPath.append(command[1])
        elif command[0] == "ls":
            pass
    else:
        currentFs = "fs"
        for path in currentPath:
            currentFs += "[\"" + path + "\"]"
        d, name = line.split()
        if not exec(f"'{name}' in {currentFs}"):
            if d=="dir":
                exec(f"{currentFs}['{name}']="+"{}")
            else:
                exec(f"{currentFs}['{name}']={d}")
            
usedSpace = folderSize(fs)
freeSpace = 70000000 - usedSpace
requiredSpace = max(0, 30000000-freeSpace)
part2 = min([allFolderSizes[folder] for folder in allFolderSizes if allFolderSizes[folder]>=requiredSpace])
print(f"Part1: {part1}")
print(f"Part2: {part2}")
