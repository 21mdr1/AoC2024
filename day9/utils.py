from collections.abc import Callable

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