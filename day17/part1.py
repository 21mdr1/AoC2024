from utils import print_result, input_file, test, use_input_file
from re import search;

class Computer:
    def __init__(self, input):
        self.output = []
        self.pointer = 0
        self.a, self.b, self.c, self.program = self.parse_input(input)

    def parse_input(self, input):
        a, b, c, program = search(r'Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (.*)', input).groups()

        return *map(int, (a, b, c)), list(map(int, program.split(',')))

    def combo(self, operand):
        return [0, 1, 2, 3, self.a, self.b, self.c][operand]

    def adv(self, operand):
        self.a = self.a // (2**self.combo(operand))

    def bxl(self, operand):
        self.b = self.b ^ operand

    def bst(self, operand):
        self.b = self.combo(operand) % 8

    def jnz(self, operand):
        if self.a != 0: self.pointer = operand

    def bxc(self, _):
        self.b = self.b ^ self.c

    def out(self, operand):
       self.output.append(self.combo(operand) % 8)

    def bdv(self, operand):
        self.b = self.a // (2**self.combo(operand))

    def cdv(self, operand):
        self.c = self.a // (2**self.combo(operand))
    
    def opcode(self, code):
        opcode = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }

        return opcode[code]

    def debug(self):
        while self.pointer < len(self.program):
            instruction = self.program[self.pointer]
            operand = self.program[self.pointer + 1]

            self.pointer += 2

            self.opcode(instruction)(operand)

        return ','.join(map(str, self.output))

@print_result
@use_input_file
def solve(input: str) -> str:
    computer = Computer(input)
    return computer.debug()

test(solve, input_file(17, True), "4,6,3,5,6,3,5,2,1,0")
test(solve, 'Register A: 10\nRegister B: 0\nRegister C: 9\n\nProgram: 5,0,5,1,5,4', '0,1,2')
test(solve, 'Register A: 2024\nRegister B: 0\nRegister C: 9\n\nProgram: 0,1,5,4,3,0', '4,2,5,6,7,7,7,7,3,1,0')
solve(input_file(17))