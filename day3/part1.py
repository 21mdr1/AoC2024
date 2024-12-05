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
    mul_intruction = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = findall(mul_intruction, memory)

    return sum([ int(match[0]) * int(match[1]) for match in matches ])

test(solve, 3, 161)
solve(input_file(3))