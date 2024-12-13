from utils import print_result, input_file, test, use_input_file
from data import stoneCycles

def calc(startStone, blinks):
    if blinks == 0:
        return 1
    
    if blinks not in stoneCycles:
        stoneCycles[blinks] = dict()

    if startStone in stoneCycles[blinks]:
        return stoneCycles[blinks][startStone]

    if startStone == '0':
        ans = calc('1', blinks - 1)
    elif len(startStone) % 2 == 0:
        ans = calc(str(int(startStone[:len(startStone)//2])), blinks - 1) +\
            calc(str(int(startStone[(len(startStone)//2):])), blinks - 1)
    else:
        ans = calc(str(int(startStone) * 2024), blinks - 1)

    stoneCycles[blinks][startStone] = ans

    return ans

@print_result
@use_input_file
def solve(input: str) -> int:
    stones = input.strip('\n').split(' ')
    return sum([ calc(stone, 75) for stone in stones ])

# test(solve, input_file(11, True), 55312)
# test(solve, input_file(11, False), 207683)
solve(input_file(11))