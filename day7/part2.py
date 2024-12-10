from utils import print_result, input_file, test

def parse_equation(equation: str):
    result, nums = equation.split(": ")
    nums = list(map(int, nums.split(" ")))

    return { "result": int(result), "nums": nums }

def test_without_concat(equation) -> bool:
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
            return True
    
    return False

def test_with_concat(equation) -> bool:
    total_calcs = len(equation["nums"]) - 2
    total_configs = 2 ** (total_calcs)

    if total_configs <= 1:
        return  equation["result"] == int(str(equation["nums"][0]) + str(equation["nums"][1]))

    for config in range(total_configs):
        config = bin(config)[2:].rjust(total_calcs, "0")

        for spot in range(total_calcs + 1):
            new_config = config[:spot] + "2" + config[spot:]
            total = equation["nums"][0]

            for i, num in enumerate(equation["nums"][1:]):
                if new_config[i] == "0":
                    total += num
                elif new_config[i] == "1":
                    total *= num
                elif new_config[i] == "2":
                    total = int(str(total) + str(num))

            if total == equation["result"]:
                return True
    
    return False

@print_result
def solve(input_file: str) -> int:
    equations = [ parse_equation(equation) 
                 for equation in open(input_file, "r").read().split("\n") ]

    calibration_value = 0

    for equation in equations:
        if test_without_concat(equation):
            calibration_value += equation["result"]
        
        elif test_with_concat(equation):
            calibration_value += equation["result"]

    return calibration_value


test(solve, 7, 11387)
solve(input_file(7))
# 6154475944263 is too low