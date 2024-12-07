from utils import print_result, input_file, test

N = (0, 1)
E = (1, 0)
S = (0, -1)
W = (-1, 0)

turn = {
    N: E,
    E: S,
    S: W,
    W: N,
}

class Map:
    def __init__(self, map_):
        self.lines = dict()
        self.columns = dict()
        self.guard_position = ()
        self.parse_map(map_)

    def parse_map(self, map_):
        width = len(map_)
        height = len(map_[0])

        for (line, column) in [(a, b) for a in range(width) for b in range(height)]:
            if map_[line][column] == '^':
                self.guard_position = (line, column)

            elif map_[line][column] == '#':
                self.lines.get(line, []).append(column)
                self.columns.get(column, []).append(line)
    

class Guard:
    def __init__(self, position):
        self.direction = N
        self.position = position
        self.distance_walked = 1
        self.hit_edge = False
    
    def turn(self):
        self.direction = turn[self.direction]
    
    def isInFront(self, obstacle):
        position = self.position[abs(self.direction[0])]
        direction = sum(self.direction)

        return direction * obstacle >  direction * position
        
    def obstacles(self, map_):
        # handle reversed stuff
        if self.direction in [N, S]:
            return map_.columns[self.position[1]]
        if self.direction in [E, W]:
            return map_.lines[self.position[0]]

    def find_destination(self, map_):
        obstacles = self.obstacles(map_)

        hitObstacle = False

        for obstacle in obstacles:
            if self.isInFront(obstacle):
                final_line = self.position[0] + (self.direction[0] * obstacle)
                final_column = self.position[1] = (self.direction[1] * obstacle)
                hitObstacle = True
                break
        
        if not hitObstacle:
            # then we hit the edge of the map
            self.hit_edge = True
            final_line = self.position[0]
            final_column = self.positionp[1]

        return final_line, final_column

    def walk(self, map_):
        self.turn()
        destination = self.find_destination(map_)

        distance_traveled = abs((self.position[0] - destination[0]) + (self.position[1] - destination[1]))
        self.position = destination

        self.distance_walked += distance_traveled

        return distance_traveled


@print_result
def solve(input_file: str) -> int:
    obstacle_map = [ line.split('') for line in  open(input_file, "r").read().split("\n") ]
    map_ = Map(obstacle_map)
    guard = Guard(map_.guard_position)

    while not guard.hit_edge:
        guard.walk(map_)

    return guard.distance_walked

test(solve, 6, 41)
solve(input_file(6))