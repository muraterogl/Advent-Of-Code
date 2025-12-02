with open('input.txt') as f:
    values = f.read().split(",")

result1 = 0
result2 = 0

for value in values:
    low, high = map(int, value.split("-"))
    i = 1
    l = len(str(high))
    counted = set()
    while True:
        for j in range(l, 1, -1):
            k = int(str(i)*j)
            if low<=k<=high and k not in counted:
                counted.add(k)
                result2 += k
            if low<=k<=high and j==2:
                result1 += k
        i += 1
        if int(str(i)*2)>high:
            break
print(result1, result2)
