from utils import print_result, input_file, test

@print_result
def solve(input_file: str) -> int:
    rules, updates = open(input_file, "r").read().split("\n\n")

    updates = [ list(map(int, update.split(","))) 
               for update in updates.split("\n") ]

    inOrder = create_rule_function(rules)

    return sum([ check(update, inOrder) for update in updates ])

def create_rule_function(rules: str):

    rule_arr = [ tuple(map(int, rule.split("|"))) 
                for rule in rules.split("\n") ]

    def inOrder(a: int, b: int) -> bool:
        if (b, a) in rule_arr:
            return False
        else:
            return True

    return inOrder

def check(update: list[str], inOrder) -> int:

    for i in range(len(update) - 1):
        if not inOrder(update[i], update[i+1]):
            return 0

    return update[len(update)//2]

test(solve, 5, 143)
solve(input_file(5))