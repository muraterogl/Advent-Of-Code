with open("input.txt") as f:
    patterns = [shape.split("\n") for shape in f.read().split("\n\n")]

def solve(diff):
    result = 0
    for pattern in patterns:
        h = len(pattern)
        w = len(pattern[0])
        # Check if horizontally mirrored
        for i in range(h-1):
            if sum(sum(pattern[i-j][k] != pattern[i+1+j][k] for k in range(w))
                                            for j in range(min(i+1, h-i-1)))==diff:
                result += 100 * (i+1)
                break
        
        # Check if vertically mirrored
        for i in range(w-1):
            if sum(sum(pattern[k][i-j] != pattern[k][i+1+j] for k in range(h))
                                            for j in range(min(i+1, w-i-1)))==diff:
                result += i+1
                break
    return result

print("part 1:", solve(0))
print("part 2:", solve(1))
