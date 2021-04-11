import re
from functools import reduce

INPUT_FILE = "./input.txt"
STOP_NUMBER = 2020
STOP_NUMBER_2 = 30000000

def play(numbers, stop_index):
    # Initialize occurences map with number: number of occurences entries.
    occurences_map = {k: 1 for v, k in enumerate(numbers)}
    # Initialize last positions map with number: list of last two positions entries.
    last_positions_map = {k: [v + 1, v + 1] for v, k in enumerate(numbers)}

    last_spoken = numbers[-1]
    iteration = len(numbers) + 1

    while iteration <= stop_index:
        # Speak 0 if the last number spoken was spoken
        # for the first time.
        if occurences_map[last_spoken] == 1:
            last_spoken = 0
        # Speak the difference between the last two positions of 
        # the last spoken number.
        else:
            latest_1 = last_positions_map[last_spoken][0]
            latest_2 = last_positions_map[last_spoken][-1]
            last_spoken = latest_2 - latest_1

        # Update spoken number occurences and last two positions.
        if last_spoken not in occurences_map:
            occurences_map[last_spoken] = 1
            last_positions_map[last_spoken] = [iteration, iteration]
        else:
            occurences_map[last_spoken] += 1
            last_positions_map[last_spoken][0] = last_positions_map[last_spoken][-1]
            last_positions_map[last_spoken][-1] = iteration
    
        iteration += 1 

    return last_spoken

if __name__ == "__main__":
    with open(INPUT_FILE, "r") as input_:
        numbers = [int(line) for line in input_.readline().split(",")]
    
    print(f"Part one. Last spoken number (index {STOP_NUMBER}): {play(numbers, STOP_NUMBER)}")
    
    print(f"Part two. Last spoken number (index {STOP_NUMBER_2}): {play(numbers, STOP_NUMBER_2)}")
    