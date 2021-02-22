import re

INPUT_FILE = "./input.txt"

def compute(expression):
    NUMBERS = r"([0-9]+)"
    OPERATION = r"([+*])"
    ADD = "+"
    MUL = "*"
    numbers = [int(value) for value in re.findall(NUMBERS, expression)]
    operations = re.findall(OPERATION, expression)
    value = numbers.pop(0)
    while operations:
        operation = operations.pop(0)
        if operation == ADD:
            value += numbers.pop(0)
        else:
            value *= numbers.pop(0)
    return value

def evaluate(expression):
    REGEX = r"\(([^()]*)\)"
    parantheses = re.search(REGEX, expression)
    value = 0
    while parantheses != None:
        for group in parantheses.groups():
            value = compute(group)
            print(f"{group} = {value}")
            expression = expression.replace("(" + group + ")", str(value))
        parantheses = re.search(REGEX, expression)
    value = compute(expression)
    return int(value)

if __name__ == "__main__":

    with open(INPUT_FILE, "r") as input_:
        expressions = [line.replace(" ", "") for line in input_.read().split("\n")]
    
    total = 0
    for expression in expressions:
        total += evaluate(expression)
    print(f"TEST: compute(4+7*3+6+4+2) == {45} is {compute('4+7*3+6+4+2') == 45}")
    print(f"TEST: compute(40+7*300+60+4+2) == {14166} is {compute('40+7*300+60+4+2') == 14166}")
    print(f"Part 1. Sum of resulting values: {total}")