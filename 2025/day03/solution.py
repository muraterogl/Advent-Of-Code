with open('input.txt') as f:
    lines = f.read().split("\n")

result1 = 0
result2 = 0

def solve(values, count):
    max_indexes = list(range(count))
    for i in range(count, len(values)):
        for j in range(count):
            if values[i-count+j+1] > values[max_indexes[j]]:
                for k in range(j, count):
                    max_indexes[k] = i-count+1+k
    result = 0
    for i in range(count):
        result = result*10 + values[max_indexes[i]]
    return result

for line in lines:
    *values, = map(int, line)
    result1 += solve(values, 2)
    result2 += solve(values, 12)
    
print(result1, result2)
