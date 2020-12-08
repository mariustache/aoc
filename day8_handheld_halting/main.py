
INPUT_FILE = "./input.txt"

accumulator = 0

def run(instructions):
    global accumulator
    index_list = list()
    index = 0
    while True:
        if index >= len(instructions):
            print("Program terminates.")
            print(f"Accumulator value: {accumulator}")
            return True
        if index in index_list:
            print("Instructions are entering an infinite loop. Stop.")
            print(f"Stop index: {index}.")
            print(f"Accumulator value: {accumulator}")
            return False

        instruction = instructions[index]
        index_list.append(index)
        print(f"Running instruction at index {index}: {' '.join(instruction)}")
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
    global accumulator
    is_fixed = False
    for idx, instruction in enumerate(instructions):
        accumulator = 0
        if instruction[0] == "jmp":
            is_fixed = run_with_changed_instruction(instructions, "nop", idx)
        elif instruction[0] == "nop":
            is_fixed = run_with_changed_instruction(instructions, "jmp", idx)

        if is_fixed:
            break

def run_with_changed_instruction(instructions, changed_instruction, idx):
    changed_instructions = instructions.copy()
    changed_instructions[idx][0] = changed_instruction
    print(f"Run program with changed instruction at index {idx} with {changed_instruction}.")
    is_fixed = run(changed_instructions)
    if is_fixed:
        print("Program is fixed.")
        return True
    else:
        print("Not the right solution.")
        return False


if __name__ == "__main__":

    with open(INPUT_FILE, "r") as input_:
        instructions = [line.split(" ") for line in input_.read().split("\n")]
    
    run(instructions)

    fix_program(instructions)