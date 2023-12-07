from collections import Counter

with open("input.txt") as f:
    hands = [line.split() for line in f.read().split("\n")]

p = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1]

def hand_ranker(data):
    card, bit = data
    c = list(Counter(card).values())
    if 5 in c:
        type_point = 7
    elif 4 in c:
        type_point = 6
    elif 3 in c and 2 in c:
        type_point = 5
    elif 3 in c:
        type_point = 4
    elif c.count(2) == 2:
        type_point = 3
    elif 2 in c:
        type_point = 2
    else:
        type_point = 1
    return[type_point, sum(p.index(card[i])* 20**(4-i) for i in range(5))]

hands.sort(key=hand_ranker)
part1 = sum(int(hand[1])*-~i for i, hand in enumerate(hands))
print("part 1:", part1)

p2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]

def hand_ranker2(data):
    card, bit = data
    count = Counter(card)
    c = list(count.values())
    c_without_J = [v for k,v in count.items() if k!="J"]
    
    if 5 in c or ("J" in count and count["J"]+max(c_without_J)==5):
        type_point = 7
    elif 4 in c or ("J" in count and count["J"]+max(c_without_J)==4):
        type_point = 6
    elif (3 in c and 2 in c) or ("J" in count and (c_without_J.count(2)==2 or (2 in c_without_J and count["J"]==2))):
        type_point = 5 
    elif 3 in c or ("J" in count and (2 in c_without_J or count["J"]==2)):
        type_point = 4
    elif c.count(2) == 2:
        type_point = 3
    elif 2 in c or "J" in count:
        type_point = 2
    else:
        type_point = 1
    return[type_point, sum(p2.index(card[i])* 20**(4-i) for i in range(5))]

hands.sort(key=hand_ranker2)

part2=sum(int(hand[1])*-~i for i, hand in enumerate(hands))
print("part 2:", part2)
