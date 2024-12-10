from utils import print_result, input_file, test


def parse_map(antenna_map):
    antennas = dict()

    for i, j in [(i, j) for i in range(len(antenna_map)) for j in range(len(antenna_map))]:
        if antenna_map[i][j] != '.':
            antennas.get(antenna_map[i][j]).append((i, j))
    
    return antennas

@print_result
def solve(input_file: str) -> int:
    input = open(input_file, "r").read().split("\n")
    antennas = parse_map(input)

    return 0


test(solve, 8, 14)
solve(input_file(8))