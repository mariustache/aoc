
from functools import reduce

INPUT_FILE = "./input.txt"
MAGIC_NUMBER = 2020
NUMBERS_TO_FIND = 3

def find_two_numbers(total_sum, numbers):
    results = list()
    for number in numbers:
        if total_sum - number in numbers:
            results.append(number)
            results.append(total_sum - number)
            break
    
    return results

def find_numbers(count, total_sum, numbers):
    results = list()


    return results

if __name__ == "__main__":
    numbers = list()
    with open(INPUT_FILE, "r") as input_:
        numbers = [int(line) for line in input_.read().split("\n")]
    
    results = find_numbers(NUMBERS_TO_FIND, MAGIC_NUMBER, numbers)
    
    if results:
        print(f"Numbers found.")
        for result in results:
            print(f"{result}")
        print(f"Product: {reduce((lambda x, y: x*y), results)}")
        print(f"Sum: {sum(results)}")
    else:
        print("No numbers found.")