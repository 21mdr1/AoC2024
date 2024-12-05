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

    items = len(matrix)

    right_leaning = \
        [ ''.join([ matrix[i][total-i] for i in range(total + 1) ]) 
            for total in range(items) ] + \
        [ ''.join([ matrix[i][items - 1 + total - i] for i in range(total, items) ]) 
            for total in range(1, items)]

    left_leaning = \
        [ ''.join([ matrix[i][i+total] for i in range(items - abs(total)) ]) 
            for total in range(items) ] + \
        [ ''.join([ matrix[i][i-total] for i in range(total, items) ]) 
            for total in range(1, items) ]

    return right_leaning + left_leaning

test(solve, 4, 18)
solve(input_file(4))