
INPUT_FILE = "./input.txt"

PREAMBLE_LENGTH = 25

def is_sum_of_two(numbers, target):
    for i in numbers:
        for j in numbers:
            if i + j == target and numbers.index(i) != numbers.index(j):
                return True
    
    return False

def find_invalid_number(numbers):
    previous_numbers = numbers[:PREAMBLE_LENGTH]
    current_index = PREAMBLE_LENGTH

    while is_sum_of_two(previous_numbers, numbers[current_index]):
        current_index += 1
        next_slice = slice(current_index - PREAMBLE_LENGTH, current_index)
        previous_numbers = numbers[next_slice]

    return numbers[current_index], current_index

def find_encryption_weakness(invalid_number, numbers):
    total_sum = 0
    index = 0
    window_length = 2
    contiguous_numbers = numbers[:window_length]

    while sum(contiguous_numbers) != invalid_number:
        index += 1
        # If the end of the list is reached, 
        # increment the window length and reset index to 0.
        window_end = index + window_length
        if index + window_length > len(numbers):
            window_length += 1
            index = 0
        contiguous_numbers = numbers[index:index+window_length]
    
    return min(contiguous_numbers) + max(contiguous_numbers), contiguous_numbers


if __name__ == "__main__":

    with open(INPUT_FILE, "r") as input_:
        xmas_encrypted_numbers = [int(line) for line in input_.read().split("\n")]
    
    invalid_number, position = find_invalid_number(xmas_encrypted_numbers)
    print(f"Found invalid number: {invalid_number} at position {position}.")
    encryption_weakness, contiguous_numbers = find_encryption_weakness(invalid_number, xmas_encrypted_numbers)
    print(f"Encryption weakness: {encryption_weakness}.")