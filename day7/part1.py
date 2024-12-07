from utils import print_result, input_file, test
from math import prod

def parse_equation(equation: str):
    result, nums = equation.split(": ")
    nums = list(map(int, nums.split(" ")))

    return { "result": int(result), "nums": nums }

@print_result
def solve(input_file: str) -> int:
    input = open(input_file, "r").read().split("\n")

    equations = [ parse_equation(equation) for equation in input ]

    calibration_value = 0

    for equation in equations:
        total_configs = 2 ** (len(equation["nums"]) - 1)

        length = len(bin(total_configs)[2:]) - 1

        for configuration in range(total_configs):
            configuration = bin(configuration)[2:].rjust(length, "0")

            total = equation["nums"][0]

            for i, num in enumerate(equation["nums"][1:]):
                if configuration[i] == "0":
                    total += num
                elif configuration[i] == "1":
                    total *= num
            
            if total == equation["result"]:
                calibration_value += equation["result"]
                break

    return calibration_value


test(solve, 7, 3749)
solve(input_file(7))