from utils import print_result, test, input_file
from re import findall

XMAS = "XMAS"
SAMX = "SAMX"

@print_result
def solve(input_file: str) -> int:
    search = open(input_file, "r").read().split("\n")

    # horizontal
    total_h = sum([ check(line) for line in search ])

    # vertical   
    total_v = sum([ check(line) for line in transpose(search) ])

    # diagonal
    total_d = sum([ check(line) for line in diagonals(search) ])

    return total_h + total_v + total_d

def check(line: str) -> int:
    return len(findall(XMAS, line)) + len(findall(SAMX, line))

def transpose(matrix: list[str]) -> list[str]:
    return [ ''.join([ line[i] for line in matrix ]) for i in range(len(matrix[0])) ]

def diagonals(matrix: list[str]) -> list[str]:

    right_leaning = []

    for total in range(len(matrix[0]) * 2):
        curr = ""
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                if i + j == total:
                    curr += matrix[i][j]
        
        right_leaning.append(curr)

    left_leaning = []

    for total in range(-len(matrix[0]) + 1, len(matrix[0])):
        curr = ""

        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                if i - j == total:
                    curr += matrix[i][j]
        
        left_leaning.append(curr)

    return right_leaning + left_leaning

test(solve, 4, 18)
solve(input_file(4))