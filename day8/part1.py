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

def find_antinode(antenna1, antenna2):
    i_change = antenna1[0] - antenna2[0]
    j_change = antenna1[1] - antenna2[1]

    node1 = antenna1[0] + i_change, antenna1[1] + j_change
    node2 = antenna2[0] - i_change, antenna2[1] - j_change

    return node1, node2

@print_result
def solve(input_file: str) -> int:
    input = open(input_file, "r").read().split("\n")
    antennas = parse_map(input)

    antinodes = set()

    for antenna_type in antennas:
        for combination in combinations(antennas[antenna_type], 2):
            node1, node2 = find_antinode(*combination)
            
            if node1[0] >= 0 and node1[1] >= 0 and node1[0] < len(input) and node1[1] < len(input):
                antinodes.add(node1)
            if node2[0] >= 0 and node2[1] >= 0 and node2[0] < len(input) and node2[1] < len(input):
                antinodes.add(node2)

    return len(antinodes)


test(solve, 8, 14)
solve(input_file(8))