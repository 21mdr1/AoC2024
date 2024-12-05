from collections.abc import Callable
from re import findall

def input_file(day: int, test: bool = False) -> str:
    test_text = "test/test-" if test else ""
    return f"../input/{test_text}input{day}.txt"

def print_result(func: Callable) -> Callable: 

    def fn(*args, **kwargs):
        answer = func(*args, **kwargs)
        print(answer)
        return answer

    return fn

@print_result
def test(routine: Callable[[str], int], day: int, answer: int) -> bool:
     return routine(input_file(day, True)) == answer

@print_result
def solve(input_file: str) -> int:
    memory = open(input_file, "r").read()

    regor = r'|'
    mul_intruction = r'mul\(\d{1,3},\d{1,3}\)'
    do_instruction = r'do\(\)'
    dont_instruction = r'don\'t\(\)'

    instructions = findall(mul_intruction + regor + do_instruction + regor + dont_instruction, memory)

    total = 0
    enabled = True

    for instruction in instructions:
        if instruction == "don't()":
            enabled = False
            continue
        if instruction == 'do()':
            enabled = True
            continue

        if not enabled:
            continue

        mul_nums = r'mul\((\d{1,3}),(\d{1,3})\)'
        nums = findall(mul_nums, instruction)[0]

        total += int(nums[0]) * int(nums[1])

    return total

test(solve, 3, 48)
solve(input_file(3))