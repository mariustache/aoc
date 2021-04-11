
INPUT_FILE = "./input.txt"

accumulator = 0

def run(instructions):
    global accumulator
    index_list = list()
    index = 0
    accumulator = 0
    while True:

        if index >= len(instructions):
            print("Program terminates.")
            print(f"Accumulator value: {accumulator}")
            return True

        if index in index_list:
            print("Instructions are entering an infinite loop. Stop.")
            print(f"Stop index: {index}. Current instruction: {instructions[index]}")
            print(f"Accumulator value: {accumulator}")
            return False

        instruction = instructions[index]
        index_list.append(index)
        #print(f"Running instruction at index {index}: {' '.join(instruction)}")
        if instruction[0] == "nop":
            index += 1
            continue
        elif instruction[0] == "acc":
            accumulator = update_value(accumulator, instruction[1])
            index += 1
        elif instruction[0] == "jmp":
            index = update_value(index, instruction[1])   

def update_value(target, instruction):
    sign = instruction[0]
    if sign == "+":
        target += int(instruction[1:])
    else:
        target -= int(instruction[1:])

    return target

def fix_program(instructions):
    for idx, instruction in enumerate(instructions):
        current_instruction = instruction[0]
        if current_instruction == "jmp":
            instructions[idx][0] = "nop"
        elif current_instruction == "nop":
            instructions[idx][0] = "jmp"
        else:
            continue

        print(f"Found {current_instruction} at index {idx}. Changing instruction and running program.")
        if run(instructions):
            break
        else:
            instructions[idx][0] = current_instruction
            

if __name__ == "__main__":

    with open(INPUT_FILE, "r") as input_:
        instructions = [line.split(" ") for line in input_.read().split("\n")]
    
    run(instructions)

    fix_program(instructions)