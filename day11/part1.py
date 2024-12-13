from utils import print_result, input_file, test, use_input_file

@print_result
@use_input_file
def solve(input: str) -> int:
    stones = input.strip('\n').split(' ')

    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == '0':
                new_stones.append('1')
            elif len(stone) % 2 == 0:
                new_stones.append(str(int(stone[:len(stone)//2])))
                new_stones.append(str(int(stone[(len(stone)//2):])))
            else:
                new_stones.append(str(int(stone) * 2024))
        stones = new_stones
            
    return len(stones)


test(solve, input_file(11, True), 55312)
solve(input_file(11))