from utils import print_result, input_file, test, use_input_file
from matrix import Matrix
import re

def parse(machine):
    for i, line in enumerate(machine.split('\n')):
            if i == 0:
                Max, May = map(int, re.fullmatch(r'Button A: X\+(\d+), Y\+(\d+)', line).group(1,2))
            elif i == 1:
                Mbx, Mby = map(int, re.fullmatch(r'Button B: X\+(\d+), Y\+(\d+)', line).group(1,2))
            else:
                Px, Py = map(int, re.fullmatch(r'Prize: X=(\d+), Y=(\d+)', line).group(1,2))
    return Matrix([[Max, Mbx], [May, Mby]]), Matrix([[Px + 10000000000000], [Py + 10000000000000]])

@print_result
@use_input_file
def solve(input: str) -> int:
    machines = input.split('\n\n')

    tokens = 0

    for machine in machines:
        coefs, prize = parse(machine)

        # to account for division error, we divide the determinant at the end
        solution = (coefs.inverse_without_det() * prize) / coefs.determinant()

        if solution.isInt():
            tokens += int(solution.a) * 3
            tokens += int(solution.b)

    return tokens

# test(solve, input_file(13, True), 480)
solve(input_file(13))