from PIL import Image

with open("input.txt") as f:
    lines = f.read().split("\n")
part1 = part2 = 0
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Robot:
    def __init__(self, line):
        x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
        self.position = Vector(x,y)
        self.velocity = Vector(vx,vy)

class Room:
    def __init__(self, lines):
        self.robots = [Robot(line) for line in lines]
        self.max_x = 101#11 # 101
        self.max_y = 103#7 # 103

    def simulate(self, times):
        for robot in self.robots:
            robot.position.x = (robot.position.x + robot.velocity.x * times) % self.max_x
            robot.position.y = (robot.position.y + robot.velocity.y * times) % self.max_y
    
    def count_quadrants(self):
        result = [0, 0, 0, 0] # NW, NE, SW, SE
        for robot in self.robots:
            if robot.position.x < self.max_x // 2 and robot.position.y < self.max_y //2:
                result[0] += 1
            elif robot.position.x > self.max_x // 2 and robot.position.y < self.max_y //2:
                result[1] += 1
            elif robot.position.x < self.max_x // 2 and robot.position.y > self.max_y //2:
                result[2] += 1
            elif robot.position.x > self.max_x // 2 and robot.position.y > self.max_y //2:
                result[3] += 1
            
        return result
    
    def safety_factor(self):
        return eval("*".join(map(str,self.count_quadrants())))
    
    def print(self):
        room_map = [[0 for _ in range(self.max_x)] for _ in range(self.max_y)]
        for robot in self.robots:
            room_map[robot.position.y][robot.position.x] += 1
        print("#"*self.max_x)
        for line in room_map:
            print(("".join(map(str,line))).replace("0","."))
        print("#"*self.max_x)
    
    def print_to_file(self, filename):
        room_map = [[0 for _ in range(self.max_x)] for _ in range(self.max_y)]
        for robot in self.robots:
            room_map[robot.position.y][robot.position.x] += 1
        width = self.max_x * 10
        height = self.max_y * 10 

        img = Image.new('RGB', (width, height), color='white')

        colors = {
            0: (0, 0, 0),       # Black for zero
            1: (255, 0, 0),     # Red for one
            2: (0, 255, 0),     # Green for two
            3: (0, 0, 255),     # Blue for three
            4: (255, 255, 0),   # Yellow for four
            5: (255, 165, 0),   # Orange for five
            6: (165, 42, 42),    # Brown for six
            7: (128, 128, 128), # Grey for seven
            8: (255, 0, 255),   # Magenta for eight
            9: (0, 255, 255)    # Cyan for nine
        }

        for i in range(self.max_y):
            for j in range(self.max_x):
                char = room_map[i][j]
                color = colors.get(char, (0, 0, 0))

                x1 = j * 10
                y1 = i * 10
                x2 = x1 + 10
                y2 = y1 + 10
                img.paste(color, (x1, y1, x2, y2))
        img.save(filename)


room = Room(lines)
room.simulate(100)
part1 = room.safety_factor()
print(part1, part2)

# By printing out the first 1000 steps and checking them out I've realized that a not so random structure is appearing in 23rd step and it repeats with small changes every 101 (width) steps.
room = Room(lines)
room.print_to_file("outputs\\0.jpg")
room.simulate(23)
room.print_to_file("outputs\\23.jpg")
for i in range(1000):
    room.simulate(101)
    room.print_to_file(f"outputs\\{23+101*(i+1)}.jpg")
