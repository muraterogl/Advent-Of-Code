with open("input.txt") as f:
    lines = f.read().split("\n")

class Position:
    def __init__(self):
        self.x=0
        self.y=0
    def dist(self, p2):
        return max(abs(self.x-p2.x), abs(self.y-p2.y))
    def follow(self, p2):
        if self.dist(p2)>1:
            if self.x < p2.x:
                self.x += 1
            elif self.x > p2.x:
                self.x -= 1
            if self.y < p2.y:
                self.y += 1
            elif self.y > p2.y:
                self.y -= 1

def solver(n):
    positions = [Position() for i in range(n)]
    visited=set([(0,0)])
    
    for line in lines:
        direction, count = line.split()
        for _ in range(int(count)):
            if direction in "UD":
                m = 1 if direction=="D" else -1
                positions[0].y+=m
                for i in range(1,n):
                    positions[i].follow(positions[i-1])

            else:
                m = 1 if direction=="R" else -1
                positions[0].x+=m
                for i in range(1,n):
                    positions[i].follow(positions[i-1])
                        
            visited.add((positions[-1].y,positions[-1].x))
    return len(visited)
        
print(f"Part1: {solver(2)}")
print(f"Part2: {solver(10)}")
