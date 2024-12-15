from utils import print_result, input_file, test

N = ("col", -1)
E = ("row", 1)
S = ("col", 1)
W = ("row", -1)

TURN = { N: E, E: S, S: W, W: N }

def isInFront(position, obstacle, dir):
    # a < b => -a > -b
    return obstacle * dir > position * dir

def isCloser(obstacle, next_obstacle, dir):
    if next_obstacle is None:
        return True
    # a > b => -a < -b
    return obstacle * dir < next_obstacle * dir

def update(position, end, direction):
    return (end, position[1]) if direction[0] == 'col' \
                else (position[0], end) \
                , TURN[direction]

def parse_map(map_):
    size = len(map_)
    col = dict(); row = dict()

    for i, j in [ (x, y) for x in range(size) for y in range(size) ]:
        if map_[i][j] == '#':
            if i not in row:
                row[i] = []
            if j not in col:
                col[j] = []
            
            row[i].append(j)
            col[j].append(i)
        elif map_[i][j] == '^':
            position = (i, j)

    return row, col, position, N

@print_result
def solve(input_file: str) -> int:
    map_ = open(input_file, "r").read().split("\n")
    row, col, position, direction = parse_map(map_)
    size = len(map_)

    visited = { position }

    while True:
        next_obstacle = None
        if direction[0] == "col": # N or S
            obstacles = col.get(position[1], [])
            pos = position[0]; dir = direction[1]
        else: # E or W
            obstacles = row.get(position[0], [])
            pos = position[1]; dir = direction[1]

        for obstacle in obstacles:
            if isInFront(pos, obstacle, dir) and isCloser(obstacle, next_obstacle, dir):
                next_obstacle = obstacle

        end = size - dir * 1 if next_obstacle is None else next_obstacle - dir * 1
        
        for i in range(pos, end + dir * 1, dir):
            if direction[0] == 'col':
                visited.add((i, position[1]))
            else:
                visited.add((position[0], i))

        position, direction = update(position, end, direction)

        if next_obstacle is None: break

    return len(visited)

test(solve, 6, 41)
solve(input_file(6))
# 5233 too low