import re
import copy

INPUT_FILE = "./input.txt"

NUMBERS = r"([0-9]+)"
OPERATION = r"([+*])"
ADD = "+"
MUL = "*"
ADDITION = r"((?:[0-9]+)\+(?:[0-9]+))"
PARANTHESES = r"\(([^()]*)\)"

def compute(expression):
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

def advanced_compute(expression):
    additions = re.findall(ADDITION, expression)
    while additions:
        for addition in additions:
            value = compute(addition)
            expression = expression.replace(addition, str(value))
        additions = re.findall(ADDITION, expression)
    return compute(expression)

def evaluate(expression, compute_function):
    parantheses = re.findall(PARANTHESES, expression)
    while parantheses:
        for group in parantheses:
            value = compute_function(group)
            expression = expression.replace("(" + group + ")", str(value))
        parantheses = re.findall(PARANTHESES, expression)
    return compute_function(expression)

if __name__ == "__main__":

    with open(INPUT_FILE, "r") as input_:
        expressions = [line.replace(" ", "") for line in input_.read().split("\n")] 
        expressions2 = copy.deepcopy(expressions)
    
    print(f"TEST: compute(4+7*3+6+4+2) == {45} is {compute('4+7*3+6+4+2') == 45}")
    print(f"TEST: compute(40+7*300+60+4+2) == {14166} is {compute('40+7*300+60+4+2') == 14166}")
    total = 0
    for expression in expressions:
        total += evaluate(expression, compute)
    print(f"Part 1. Sum of resulting values: {total}")

    print(f"TEST: advanced_compute(4+7*3+6+4+2) == 11*15 is {advanced_compute('4+7*3+6+4+2') == '11*15'}")
    print(f"TEST: advanced_compute(40+7*300+60+4+2) == 47*366 is {advanced_compute('40+7*300+60+4+2') == '47*366'}")
    print(f"TEST: evaluate(1+(2*3)+(4*(5+6))) == {51} is {evaluate('1+(2*3)+(4*(5+6))', advanced_compute) == 51}")
    print(f"TEST: evaluate(2*3+(4*5)) == {46} is {evaluate('2*3+(4*5)', advanced_compute) == 46}")
    print(f"TEST: evaluate(5+(8*3+9+3*4*3)) == {1445} is {evaluate('5+(8*3+9+3*4*3)', advanced_compute) == 1445}. " + \
          f"Actual value: {evaluate('5+(8*3+9+3*4*3)', advanced_compute)}")
    print(f"TEST: evaluate(5*9*(7*3*3+9*3+(8+6*4))) == {669060} is {evaluate('5*9*(7*3*3+9*3+(8+6*4))', advanced_compute) == 669060}. " + \
          f"Actual value: {evaluate('5*9*(7*3*3+9*3+(8+6*4))', advanced_compute)}")
    print(f"TEST: evaluate(((2+4*9)*(6+9*8+6)+6)+2+4*2) == {23340} is {evaluate('((2+4*9)*(6+9*8+6)+6)+2+4*2', advanced_compute) == 23340}. " + \
          f"Actual value: {evaluate('((2+4*9)*(6+9*8+6)+6)+2+4*2', advanced_compute)}")
    total = 0
    for expression in expressions2:
        total += evaluate(expression, advanced_compute)
    print(f"Part 2. Advanced sum of resulting values: {total}")
    