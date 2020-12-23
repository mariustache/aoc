import re
from functools import reduce

INPUT_FILE = "./input.txt"
DELIMITER = " = "
MASK = "mask"
ADDRESSES = "addresses"
ADDRESS_REGEX = r"mem\[(\d*)\]"

def initialize(data, part_one=False):
    memory_ = dict()
    mask = 0
    for line in data:
        lvalue, rvalue = line.split(DELIMITER)
        if lvalue == MASK:
            mask = rvalue
        else:
            address = re.search(ADDRESS_REGEX, lvalue).group(1)
            if part_one:
                memory_[address] = update_value(mask, int(rvalue))
            else:
                # Compute all addresses that will be modified.
                addresses = get_address_space(address, mask)
                for address_ in addresses:
                    memory_[address_] = int(rvalue)
    return sum(memory_.values())

def update_value(mask, value):
    bits = len(mask)
    for idx, bit in enumerate(mask):
        if bit != "X":
            pos = bits - 1 - idx
            value = set_bit(value, int(bit), pos)
    return value

def get_address_space(address, mask):
    length = len(mask)
    bin_address_list = binary_list(int(address), length)
    # Add floating bits to the binary list.
    for idx, bit in enumerate(mask):
        if bit != "0": 
            bin_address_list[idx] = bit
    
    return generate_address(bin_address_list)

def generate_address(floating_address_list):
    addresses = list()
    floating_bits = sum(map(lambda x: x == "X", floating_address_list))
    combinations = list()
    # Generate all combinations for the floating bits.
    for i in range(0, 2**floating_bits):
        combinations.append(binary_list(i, floating_bits))
    # Generate all addresses.
    for combination in combinations:
        counter = 0
        current_address = floating_address_list.copy()
        for idx, floating_bit in enumerate(current_address):
            if floating_bit == "X":
                current_address[idx] = combination[counter]
                counter += 1
        
        addresses.append(current_address)
    # Transform from binary char list to numbers.
    return [int("".join(address), 2) for address in addresses]

def binary_list(number, length):
    # Converts a number's binary form into a string.
    # The number is completed with '0' values if the
    # resulting string is not of length `length`
    binary = "{0:b}".format(number)
    binary_list = [char for char in binary]
    zeros = ["0" for i in range(0, length - len(binary_list))]
    return zeros + binary_list


def set_bit(number, bit, pos):
    mask = (1 << pos)
    if bit == 0:
        number &= ~mask
    else:
        number |= mask
    return number


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as input_:
        data = [line for line in input_.read().split("\n")]
    
    print(f"Part one. Sum of all values left in memory: {initialize(data, part_one=True)}")
    print(f"Part two. Sum of all values left in memory: {initialize(data)}")
    