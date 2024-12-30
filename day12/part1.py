from utils import print_result, input_file, test, use_input_file
from homology import homology
from math import sqrt

def picks_thm(i=None, b=None, A=None, h=0):
    if A is None:
        return i + h - 1 + b/2
    
    if b is None:
        return (A + 1 - i - h) * 2

    if i is None:
        return A - h + 1 - b/2

def get_region(garden):
    region = []

    for i, j in [ (a, b) for a in range(len(garden)) for b in range(len(garden[0])) ]:
        if garden[i][j] != '.':
            letter = garden[i][j]
            curr = i, j
            region.append(curr)
            garden[i][j] = '.'
            break

    if len(region) == 0:
        return []
    
    stack = []

    while True:
        if curr[1] + 1 < len(garden[0]) and garden[curr[0]][curr[1] + 1] == letter:
            stack.append(curr)
            curr = curr[0], curr[1] + 1
            region.append(curr)
            garden[curr[0]][curr[1]] = '.'
            
        elif curr[0] + 1 < len(garden) and garden[curr[0] + 1][curr[1]] == letter:
            stack.append(curr)
            curr = curr[0] + 1, curr[1]
            region.append(curr)
            garden[curr[0]][curr[1]] = '.'

        elif curr[1] - 1 >= 0 and garden[curr[0]][curr[1] - 1] == letter:
            stack.append(curr)
            curr = curr[0], curr[1] - 1
            region.append(curr)
            garden[curr[0]][curr[1]] = '.'
        
        elif curr[0] - 1 >= 0 and garden[curr[0] - 1][curr[1]] == letter:
            stack.append(curr)
            curr = curr[0] - 1, curr[1]
            region.append(curr)
            garden[curr[0]][curr[1]] = '.'
        
        else:
            try:
                curr = stack.pop()
            except:
                return region

@print_result
@use_input_file
def solve(input: str) -> int:
    garden = [ list(line) for line in input.split('\n') ]

    total_price = 0
    while True:
        region = get_region(garden)
        if len(region) == 0:
            break

        A = len(region)
        h = homology(region, sqrt(2))
        i = homology(region, 1) - h

        b = picks_thm(A= A, i = i, h = h)

        total_price += A * b

    return total_price


# small_ex = 'AAAA\nBBCD\nBBCC\nEEEC'
# test(solve, small_ex, 140)
# holes_ex = 'OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO'
# test(solve, holes_ex, 772)
# test(solve, input_file(12, True), 1930)
solve(input_file(12))