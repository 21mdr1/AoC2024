from utils import print_result, input_file, test, use_input_file
from matrix import Matrix, inverse
import re

def parse(machine):
    for i, line in enumerate(machine.split('\n')):
            if i == 0:
                Max, May = map(int, re.fullmatch(r'Button A: X\+(\d+), Y\+(\d+)', line).group(1,2))
            elif i == 1:
                Mbx, Mby = map(int, re.fullmatch(r'Button B: X\+(\d+), Y\+(\d+)', line).group(1,2))
            else:
                Px, Py = map(int, re.fullmatch(r'Prize: X=(\d+), Y=(\d+)', line).group(1,2))
    return Matrix([[Max, Mbx], [May, Mby]]), Matrix([[Px], [Py]])

@print_result
@use_input_file
def solve(input: str) -> int:
    machines = input.split('\n\n')

    tokens = 0

    for machine in machines:
        coefs, prize = parse(machine)

        coefs_inv = inverse(coefs) * coefs.determinant()
        solution = (coefs_inv * prize) / coefs.determinant()

        if int(solution.a) == solution.a and int(solution.b) == solution.b:
            tokens += int(solution.a) * 3
            tokens += int(solution.b)

    return tokens

test(solve, input_file(13, True), 480)
solve(input_file(13))

# 24911 is too low