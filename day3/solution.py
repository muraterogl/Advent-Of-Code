with open('day3/input.txt') as f:q=f.readlines()

gamma = ""
epsilon = ""
l = [list(i.rstrip('\n'))for i in q]
for i in zip(*l):
    if i.count("0")>i.count("1"):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(f"part1: {gamma*epsilon}")


oxygenList = l[:]
co2List = l[:]
currentIndex = 0
while len(oxygenList)>1:
    currentList = list(zip(*oxygenList))[currentIndex]
    if currentList.count("0")>currentList.count("1"):
        oxygenList = [o for o in oxygenList if o[currentIndex]=="0"]
    else:
        oxygenList = [o for o in oxygenList if o[currentIndex]=="1"]
    currentIndex += 1

oxygenNumber = int("".join(oxygenList[0]),2)

currentIndex = 0
while len(co2List)>1:
    currentList = list(zip(*co2List))[currentIndex]
    if currentList.count("1")<currentList.count("0"):
        co2List = [c for c in co2List if c[currentIndex]=="1"]
    else:
        co2List = [c for c in co2List if c[currentIndex]=="0"]
    currentIndex += 1

co2Number = int("".join(co2List[0]),2)

print(f"part2: {oxygenNumber*co2Number}")
