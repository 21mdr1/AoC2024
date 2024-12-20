from utils import print_result, input_file, test, use_input_file

@print_result
@use_input_file
def solve(input: str) -> int:
    return 0


test(solve, input_file(_, True), _)
#solve(input_file(_))