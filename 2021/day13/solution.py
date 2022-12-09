with open('day13/input.txt') as f:q=f.readlines()


def countDots(paper):
    total = 0
    for y in range(len(paper)):
        for x in range(len(paper[0])):
            if paper[y][x]=="#":
                total+=1
    return total


def printPaper(paper):
    for line in paper:
        print("".join(line))

#Reading input and forming a paper
dotsEnded = False
foldingLines = []
dots = []
xMax = -1
yMax = -1
for line in q:
    if line == "\n":
        dotsEnded = True
    elif dotsEnded:
        a,b = line.split("along ")[1].split("=")
        foldingLines.append((a,int(b)))
    else:
        x,y = map(int, line.split(","))
        dots.append((x,y))
        xMax=max(x,xMax)
        yMax=max(y,yMax)

paper = [[" "for _ in range(xMax+1)]for _ in range(yMax+1)]
for x,y in dots:
    paper[y][x] = "#"


#Folding
for i,fold in enumerate(foldingLines):
    if fold[0] == "y":
        yf = fold[1]
        tempPaper = paper[:yf]
        for y in range(yf+1, len(paper)):
            for x in range(len(paper[0])):
                if paper[y][x] == "#":
                    tempPaper[2*yf-y][x] = "#"
    else:
        xf = fold[1]
        tempPaper = [y[:xf]for y in paper]
        for y in range(len(paper)):
            for x in range(xf+1, len(paper[0])):
                if paper[y][x] == "#":
                    tempPaper[y][2*xf-x] = "#"
    paper = tempPaper[:]
    if i==0:
        print(f"part1: {countDots(paper)}")
        
print(f"part2:")
printPaper(paper)