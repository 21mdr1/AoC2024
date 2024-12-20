from utils import print_result, input_file, test, use_input_file
import re

@print_result
@use_input_file
def solve(input: str) -> int:
    q1 = 0; q2 = 0; q3 = 0; q4 = 0

    for robot in input.split('\n'):
        posx, posy, velx, vely = map(int, re.fullmatch(r'p=(\d+|-\d+),(\d+|-\d+) v=(\d+|-\d+),(\d+|-\d+)', robot).group(1,2,3,4))

        posx = ((posx + 100*velx) % 101)
        posy = ((posy + 100*vely) % 103)

        if posx > 50 and posy > 51:
            q1 += 1
        elif posx > 50 and posy < 51:
            q2 += 1
        elif posx < 50 and posy > 51:
            q3 += 1
        elif posx < 50 and posy < 51:
            q4 += 1

    return q1 * q2 * q3 * q4


# test(solve, input_file(14, True), 12)
solve(input_file(14))