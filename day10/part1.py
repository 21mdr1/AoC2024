from utils import print_result, input_file, test, use_input_file

@print_result
@use_input_file
def solve(input: str) -> int:
    topomap = [ list(map(int, line.split(""))) for line in input.split("\n") ]

    trail_heads = []

    for i, j in [ (x, y) for x in range(len(topomap)) for y in range(len(topomap[0])) ]:
        if topomap[i][j] == 0:
            trail_heads.append((i, j))

    # evaluate each trailhead

    return 0


test(solve, input_file(10, True), 36)
# solve(input_file(10))