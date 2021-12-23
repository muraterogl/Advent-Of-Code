from copy import deepcopy
import sys

sys.setrecursionlimit(9**9)

#demo part1
#rooms = [["B","A"],["C","D"],["B","C"],["D","A"]]

#demo part2
#rooms = [["B","D","D","A"],["C","C","B","D"],["B","B","A","C"],["D","A","C","A"]]

#real part1
#rooms = [["C","C"],["B","D"],["A","A"],["D","B"]]
#real part2
rooms = [["C","D","D","C"],["B","C","B","D"],["A","B","A","A"],["D","A","C","B"]]

#final = [["A","A"],["B","B"],["C","C"],["D","D"]]
final = [["A","A","A","A"],["B","B","B","B"],["C","C","C","C"],["D","D","D","D"]]
roomLen = len(rooms[0])
waiting = [".",".",".",".",".",".","."]
finalDest = {"A":0,"B":1,"C":2,"D":3,".":18293}
costs = {"A":1, "B":10, "C":100, "D":1000}
maxCost = 9999999999
seen = {}

def findBetter(roomState, waitingState, cost):
    global maxCost
    hashStr = str(roomState)+str(waitingState)
    if cost>maxCost or hashStr in seen and seen[hashStr]<=cost:
        return 9**9
    if roomState==final:
        if cost < maxCost:
            maxCost = cost
            print("best: ",maxCost)
        return cost
    possibleMoves = []
    for ix, room in enumerate(roomState):
        if all(cell==room[0] for cell in room) and ix==finalDest[room[-1]]:
            continue
        waitingMinIndex = 0
        waitingMaxIndex = ix+1
        for wix, w in enumerate(waitingState):
            if wix<ix+2: #left side of current room
                if w!=".":
                    waitingMinIndex = wix+1
            else:   #right side of current room
                if w!=".":
                    break
                waitingMaxIndex+=1
        if waitingMinIndex <= waitingMaxIndex: #there is a room outside
            currentDepth = 0
            while currentDepth < roomLen:
                if all(cell==room[currentDepth] for cell in room[currentDepth:]) and ix==finalDest[room[-1]]:
                    break
                if room[currentDepth]==".":
                    currentDepth+=1
                else:
                    #check if it can go to destination
                    targetRoomIndex = finalDest[room[currentDepth]]
                    targetRoomCorrectCount = roomState[targetRoomIndex].count(room[currentDepth])
                    if targetRoomCorrectCount<roomLen and  all(cell=="." or cell==room[currentDepth] for cell in roomState[targetRoomIndex]):
                        #check if corridor is empty
                        if (targetRoomIndex < ix and all(waitingState[i]=="." for i in range(targetRoomIndex+2, ix+2))) or (targetRoomIndex > ix and all(waitingState[i]=="." for i in range(ix+2, targetRoomIndex+2))):
                            roadLen = 2*abs(targetRoomIndex - ix) + 1 + currentDepth + roomLen - targetRoomCorrectCount
                            nextRoomState = deepcopy(roomState)
                            nextWaitingState = deepcopy(waitingState)
                            nextCost = cost + costs[room[currentDepth]] * roadLen
                            nextRoomState[ix][currentDepth] = "."
                            nextRoomState[targetRoomIndex][roomLen-targetRoomCorrectCount-1] = room[currentDepth]
                            possibleMoves.append((nextRoomState, nextWaitingState, nextCost))
                            break
                    #left side of waiting
                    for i in range(waitingMinIndex,ix+2):
                        roadLen = currentDepth + 1 + 2*(ix+1-i) + (0 if i==0 else 1)
                        nextRoomState = deepcopy(roomState)
                        nextWaitingState = deepcopy(waitingState)
                        nextCost = cost + costs[room[currentDepth]] * roadLen
                        nextRoomState[ix][currentDepth] = "."
                        nextWaitingState[i] = room[currentDepth]
                        possibleMoves.append((nextRoomState, nextWaitingState, nextCost))
                    #right side of waiting
                    for i in range(ix+2,waitingMaxIndex+1):
                        roadLen = currentDepth + 1 + 2*(i-ix-2) + (0 if i==6 else 1)
                        nextRoomState = deepcopy(roomState)
                        nextWaitingState = deepcopy(waitingState)
                        nextCost = cost + costs[room[currentDepth]] * roadLen
                        nextRoomState[ix][currentDepth] = "."
                        nextWaitingState[i] = room[currentDepth]
                        possibleMoves.append((nextRoomState, nextWaitingState, nextCost))
                    break
    for wix, w in enumerate(waitingState):
        if w!=".":
            targetRoomIndex = finalDest[w]
            targetRoomCorrectCount = roomState[targetRoomIndex].count(w)
            if targetRoomCorrectCount<roomLen and  all(cell=="." or cell==w for cell in roomState[targetRoomIndex]):
                if targetRoomIndex <= wix-2: #right side
                    if targetRoomIndex+2==wix or all(ww=="."for ww in waitingState[targetRoomIndex+2:wix]): #empty road
                        #calculate road
                        roadLen = roomLen-targetRoomCorrectCount+2*(wix-targetRoomIndex-2)+(0 if wix==6 else 1)
                        nextRoomState = deepcopy(roomState)
                        nextWaitingState = deepcopy(waitingState)
                        nextCost = cost + costs[w] * roadLen
                        nextRoomState[targetRoomIndex][roomLen-targetRoomCorrectCount-1] = w
                        nextWaitingState[wix] = "."
                        possibleMoves.append((nextRoomState, nextWaitingState, nextCost))
                else: #left side
                    if targetRoomIndex+1==wix or all(ww=="." for ww in waitingState[wix+1:targetRoomIndex+2]): #empty road
                        roadLen = roomLen-targetRoomCorrectCount+2*(targetRoomIndex+1-wix)+(0 if wix==0 else 1)
                        nextRoomState = deepcopy(roomState)
                        nextWaitingState = deepcopy(waitingState)
                        nextCost = cost + costs[w] * roadLen
                        nextRoomState[targetRoomIndex][roomLen-targetRoomCorrectCount-1] = w
                        nextWaitingState[wix] = "."
                        possibleMoves.append((nextRoomState, nextWaitingState, nextCost))
    if not possibleMoves:
        seen[hashStr] = 0
        return 9**9
    result = min([findBetter(*move) for move in possibleMoves])
    seen[hashStr] = result
    return result


print(findBetter(rooms, waiting, 0))
