from utils import print_result, input_file, test

@print_result
@use_input_file
def solve(input_file: str) -> int:
    input = open(input_file, "r").read()
    return 0


test(solve, input_file(_, True), _)
solve(input_file(_))