from utils import print_result, input_file, test, use_input_file

OUTPUT = []
A = None; B = None; C = None
POINTER = 0

def getA(): return A
def getB(): return B
def getC(): return C

combo = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: getA,
    5: getB,
    6: getC,
}

def adv(operand):
    global A
    A = getA() // (2**combo[operand]())

def bxl(operand):
    global B
    B = getB() ^ operand

def bst(operand):
    global B
    B = combo[operand]() % 8

def jnz(operand):
    global POINTER
    if getA() == 0:
        POINTER += 2
    else: POINTER = operand

def bxc(_):
    global B
    B = getB() ^ getC()

def out(operand):
    global OUTPUT
    OUTPUT.append(combo[operand]() % 8)

def bdv(operand):
    global B
    B = getA() // (2**combo[operand]())

def cdv(operand):
    global C
    C = getA() // (2**combo[operand]())

opcode = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

def output():
    return ','.join(map(str, OUTPUT))

def parse_input(input):
    global A, B, C

    for i, line in enumerate(input.split('\n')):
        if i == 0:
            A = int(line.split(' ')[-1])
        elif i == 1:
            B = int(line.split(' ')[-1])
        elif i == 2:
            C = int(line.split(' ')[-1])
        elif i == 4:
            program = list(map(int, line.split(' ')[1].split(',')))

    return program


@print_result
@use_input_file
def solve(input: str) -> str:
    global POINTER, OUTPUT

    program = parse_input(input)

    while POINTER < len(program):
        instruction = program[POINTER]
        operand = program[POINTER + 1]

        # print("instruction", instruction, "operand", operand)

        opcode[instruction](operand)

        # print("A", A, "B", B, "C", C)

        if instruction == 3:
            continue

        POINTER += 2

    res = output()

    OUTPUT = []; POINTER = 0
    return res


# test(solve, input_file(17, True), "4,6,3,5,6,3,5,2,1,0")
# test(solve, 'Register A: 10\nRegister B: 0\nRegister C: 9\n\nProgram: 5,0,5,1,5,4', '0,1,2')
# test(solve, 'Register A: 2024\nRegister B: 0\nRegister C: 9\n\nProgram: 0,1,5,4,3,0', '4,2,5,6,7,7,7,7,3,1,0')
solve(input_file(17))