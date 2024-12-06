from utils import print_result, test, input_file
from re import findall

MAS = "MAS"
SAM = "SAM"

@print_result
def solve(input_file: str) -> int:
    search = open(input_file, "r").read().split("\n")

    xmases = 0
    
    for i in range(1, len(search) - 1):
        for j in range(1, len(search) - 1):
            if search[i][j] != "A":
                continue

            # find out if they make 2 MASs
            one = search[i-1][j-1] + "A" + search[i+1][j+1]
            two = search[i-1][j+1] + "A" + search[i+1][j-1]

            if (one == MAS or one == SAM) and (two == MAS or two == SAM):
                xmases += 1        

    return xmases

test(solve, 4, 9)
solve(input_file(4))