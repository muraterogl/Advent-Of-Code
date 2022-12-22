#kanser

import re

with open("input.txt") as f:
    lines, inss = f.read().split("\n\n")

max_l = max(map(len,lines.split("\n")))
board = [line.ljust(max_l) for line in lines.split("\n")]
h = len(board)
w = len(board[0])

class Player:
    def __init__(self, x):
        self.y = 0
        self.x = x
        self.dir = 0

    def change_dir(self, d):
        if d == "R":
            self.dir = (self.dir + 1) % 4
        else:
            self.dir = (self.dir - 1) % 4

    def region(self):
        return {(0,1):5,(0,2):6,(1,1):4,(2,1):3,(2,0):2,(3,0):1}[(self.y//50,self.x//50)]

    def next(self):
        dy,dx = [(0,1), (1,0), (0,-1), (-1,0)][self.dir]
        r = self.region()
        if 0<=self.y+dy<h and 0<=self.x+dx<w:
            self.y += dy
            self.x += dx
        elif self.dir == 0:
            self.y = {1:149,3:149-self.y,4:49,6:149-self.y}[r]
            self.x = {1:self.y-100,3:149,4:50+self.y,6:99}[r]
            self.dir = {1:3,3:2,4:3,6:2}[r]
        elif self.dir == 1:
            self.y = {1:0,3:100+self.x,6:self.x-50}[r]
            self.x = {1:100+self.x,3:49,6:99}[r]
            self.dir = {1:1,3:2,6:2}[r]
        elif self.dir == 2:
            self.y = {1:0,2:149-self.y,4:100,5:149-self.y}[r]
            self.x = {1:self.y-100,2:50,4:self.y-50,5:0}[r]
            self.dir = {1:1,2:0,4:1,5:0}[r]
        else:
            self.y = {2:50+self.x,5:100+self.x,6:199}[r]
            self.x = {2:50,5:0,6:self.x-100}[r]
            self.dir = {2:0,5:0,6:3}[r]

    def move(self, count):
        dy,dx = [(0,1), (1,0), (0,-1), (-1,0)][self.dir]
        for _ in range(count):
            py, px = self.y, self.x
            self.y += dy
            self.x += dx
            self.y %= h
            self.x %= w
            while board[self.y][self.x] == " ":
                self.y += dy
                self.x += dx
                self.y %= h
                self.x %= w
            if board[self.y][self.x] == "#":
                self.y = py
                self.x = px
                break

    def move2(self, count):
        for _ in range(count):
            py, px = self.y, self.x
            self.next()
            if board[self.y][self.x] == "#":
                self.y = py
                self.x = px
                break

    def play(self, part):
        for ins in re.findall(r'\d+|\D+',inss):
            if ins in "RL":
                self.change_dir(ins)
            elif part == 1:
                self.move(int(ins))
            else:
                self.move2(int(ins))

    def password(self):
        return 1000*-~self.y + 4*-~self.x + self.dir

player = Player(board[0].index("."))  
player.play(1)
print(f"Part1: {player.password()}")
player = Player(board[0].index("."))  
player.play(2)
print(f"Part2: {player.password()}")
