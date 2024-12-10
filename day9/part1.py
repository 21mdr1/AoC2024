from utils import print_result, input_file, test

@print_result
def solve(input_file: str) -> int:
    input = open(input_file, "r").read()
    return 0


test(solve, _, _)
solve(input_file(_))