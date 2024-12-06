from utils import print_result, input_file, test
from functools import cmp_to_key

@print_result
def solve(input_file: str) -> int:
    rules, updates = open(input_file, "r").read().split("\n\n")

    updates = [ list(map(int, update.split(","))) 
               for update in updates.split("\n") ]

    inOrder = create_rule_function(rules)

    total = 0

    for update in updates:
        if not needsOrdering(update, inOrder):
            continue

        total += sorted(update, key=cmp_to_key(inOrder))[len(update)//2]

    return total

def create_rule_function(rules: str):

    rule_arr = [ tuple(map(int, rule.split("|"))) 
                for rule in rules.split("\n") ]

    def inOrder(a: int, b: int) -> bool:
        if (a, b) in rule_arr:
            return 1
        if (b, a) in rule_arr:
            return -1
        else:
            return 0

    return inOrder

def needsOrdering(update: list[str], inOrder) -> bool:

    for i in range(len(update) - 1):
        if inOrder(update[i], update[i+1]) == -1:
            return True

    return False



test(solve, 5, 123)
solve(input_file(5))