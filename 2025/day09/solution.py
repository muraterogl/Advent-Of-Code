with open('input.txt') as f:
    lines = f.read().split("\n")

result1 = 0
result2 = 0

reds = [tuple(map(int, line.split(",")))for line in lines]

result1 = max([(abs(red1[0]-red2[0])+1)*(abs(red1[1]-red2[1])+1)for red1 in reds for red2 in reds])
for red1 in reds:
    for red2 in reds:
        area = (abs(red1[0]-red2[0])+1)*(abs(red1[1]-red2[1])+1)
        if area > result2:
            x1,x2 = sorted([red1[0],red2[0]])
            y1,y2 = sorted([red1[1],red2[1]])
            failed = False
            for g1, g2 in zip(reds, reds[1:]+[reds[0]]):
                xx1,xx2 = sorted([g1[0],g2[0]])
                yy1,yy2 = sorted([g1[1],g2[1]])
                if x2>xx1 and x1<xx2 and y2>yy1 and y1<yy2:
                    failed = True
                    break
            if not failed:
                result2 = area
                
print(result1, result2)
