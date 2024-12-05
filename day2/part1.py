def test(routine, input_file, answer):
    calculation = routine(input_file)
    print(calculation)
    return calculation == answer

def isSafe(report):
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

def calculateSafety(inputFile):
    input = open(inputFile, "r").read().split("\n")
    reports = [ list(map(int, line.split(" "))) for line in input ]

    return sum([ 1 if isSafe(report) else 0 for report in reports ])

# print(test(calculateSafety, "../input/test/test-input2.txt", 2))
print(calculateSafety("../input/input2.txt"))