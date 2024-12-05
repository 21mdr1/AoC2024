from collections.abc import Callable;

def print_result(func: Callable) -> Callable: 

    def fn(*args, **kwargs):
        answer = func(*args, **kwargs)
        print(answer)
        return answer

    return fn

    # return lambda *args, **kwargs: print(func(*args, **kwargs))

@print_result
def test(routine: Callable[[str], int], day: int, answer: int) -> bool:
     return routine(f"../input/test/test-input{day}.txt") == answer

@print_result
def calculate_safety(input_file: str) -> int:
    input = open(input_file, "r").read().split("\n")
    reports = [ list(map(int, line.split(" "))) for line in input ]

    safe_reports = 0

    for report in reports:

        if isSafe(report):
            safe_reports += 1
            continue
        
        for i in range(len(report)):

            if isSafe(report[:i]+ report[i+1:]):
                safe_reports += 1
                break

    return safe_reports

def isSafe(report: list[int]) -> bool:
    changes = [ report[i + 1] - report[i] for i in range(len(report) - 1)]

    previous = None

    for change in changes:
        if abs(change) == 0 or abs(change) > 3:
            return False
        
        if previous is None or previous * change > 0:
            previous = change
        else:
            return False

    return True

test(calculate_safety, 2, 4)
calculate_safety("../input/input2.txt")