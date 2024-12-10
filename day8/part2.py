from utils import print_result, input_file, test
from itertools import combinations

def parse_map(antenna_map):
    antennas = dict()

    for i, j in [(i, j) for i in range(len(antenna_map)) for j in range(len(antenna_map))]:
        if antenna_map[i][j] != '.':

            if antenna_map[i][j] not in antennas:
                antennas[antenna_map[i][j]] = []

            antennas[antenna_map[i][j]].append((i, j))

    return antennas

def get_antinodes(antenna1, antenna2, antinodes, size):
    antinodes.add(antenna1)
    antinodes.add(antenna2)

    i_change = antenna1[0] - antenna2[0]
    j_change = antenna1[1] - antenna2[1]

    last_node = antenna1
    while True:
        node = last_node[0] + i_change, last_node[1] + j_change

        if node[0] < 0 or node[1] < 0 or node[0] >= size or node[1] >= size:
            break
        
        antinodes.add(node)
        last_node = node
    
    last_node = antenna2
    while True:
        node = last_node[0] - i_change, last_node[1] - j_change

        if node[0] < 0 or node[1] < 0 or node[0] >= size or node[1] >= size:
            break
        
        antinodes.add(node)
        last_node = node

    return antinodes

@print_result
def solve(input_file: str) -> int:
    input = open(input_file, "r").read().split("\n")
    antennas = parse_map(input)

    antinodes = set()
    for antenna_type in antennas:
        for combination in combinations(antennas[antenna_type], 2):
            antinodes = get_antinodes(*combination, antinodes, len(input))

    return len(antinodes)


test(solve, 8, 34)
solve(input_file(8))