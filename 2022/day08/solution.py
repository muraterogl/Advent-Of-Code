with open("input.txt") as f:
    lines = f.read().split("\n")

trees = [[int(tree) for tree in line]for line in lines]
visible = [[False for _ in range(len(trees[i]))]for i in range(len(trees))]
#top to bottom
maxTrees = trees[0]
for i in range(1,len(trees)-1):
    for j in range(1,len(trees[i])-1):
        if maxTrees[j] < trees[i][j]:
            visible[i][j] = True
            maxTrees[j] = trees[i][j]
            
#bottom to top
maxTrees = trees[-1]
for i in range(len(trees)-2,0,-1):
    for j in range(1,len(trees[i])-1):
        if maxTrees[j] < trees[i][j]:
            visible[i][j] = True
            maxTrees[j] = trees[i][j]
            
#left to right
maxTrees = [trees[i][0] for i in range(len(trees))]
for i in range(1,len(trees)-1):
    for j in range(1,len(trees[i])-1):
        if maxTrees[i] < trees[i][j]:
            visible[i][j] = True
            maxTrees[i] = trees[i][j]
            
#right to left
maxTrees = [trees[i][-1] for i in range(len(trees))]
for i in range(1,len(trees)-1):
    for j in range(len(trees[i])-2,0,-1):
        if maxTrees[i] < trees[i][j]:
            visible[i][j] = True
            maxTrees[i] = trees[i][j]

inside_visible = sum(sum(visible[i][j]for j in range(len(visible[i])))for i in range(len(visible)))
outside_visible = 2*(len(trees)+len(trees[0])-2)
print(f"Part1: {inside_visible+outside_visible}")



#I'm sorry for this mess
max_multiplier = 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[i])-1):
        multiplier = 1
        for k in range(i+1,len(trees)):
            if trees[k][j] >= trees[i][j] or k==len(trees)-1:
                multiplier *= k-i
                break
        for k in range(i-1,-1,-1):
            if trees[k][j] >= trees[i][j] or k==0:
                multiplier *= i-k
                break
        for k in range(j+1,len(trees[i])):
            if trees[i][k] >= trees[i][j] or k==len(trees[i])-1:
                multiplier *= k-j
                break
        for k in range(j-1,-1,-1):
            if trees[i][k] >= trees[i][j] or k==0:
                multiplier *= j-k
                break
        max_multiplier = max(max_multiplier, multiplier)

print(f"Part2: {max_multiplier}")
