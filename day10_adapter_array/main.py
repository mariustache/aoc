
import math

INPUT_FILE = "./input.txt"

MAX_ADAPTER_JUMP = 3

def find_differences(adapters):
    # Take into account the built-in jolted adapter.
    differences_map = {"1": 0, "2": 0, "3": 1}
    # Take into account the first adapter.
    sorted_adapters = sorted(adapters)
    first_adapter = sorted_adapters[0]
    differences_map[str(first_adapter)] += 1
    # Check if the first adapter can be removed.
    removable_adapters = list()
    second_adapter = sorted_adapters[1]
    if second_adapter <= MAX_ADAPTER_JUMP:
        removable_adapters.append(first_adapter)
    # Add difference between first two adapters
    differences_map[str(second_adapter - first_adapter)] += 1

    # Find differences for the other adapters.
    for adapter in sorted_adapters[1:-1]:
        idx = sorted_adapters.index(adapter)
        next_adapter = sorted_adapters[idx + 1]
        difference = next_adapter - adapter
        differences_map[str(difference)] += 1
        previous_adapter = sorted_adapters[idx - 1]
        last_difference = adapter - previous_adapter
        # If adapter neighbours are at MAX_ADAPTER_JUMP difference away,
        # the adapter is not removable.
        if difference != MAX_ADAPTER_JUMP and last_difference != MAX_ADAPTER_JUMP:
            removable_adapters.append(adapter)

    return differences_map, removable_adapters

def is_consecutive(list_):
    if not list_[1] - list_[0] == 1:
        return False
    if list_[2] - list_[1] == 1:
        return True
    
    return False

def number_of_subsets(adapters):
    # Compute the number of subsets that contain 3 adapters with
    # a difference of 1.
    end = 3
    idx = 0
    total_number = 0
    subset = adapters[idx:end]
    while idx < len(adapters) and end <= len(adapters):
        if is_consecutive(subset):
            idx = end
            end += 3
            total_number += 1
        else:
            idx += 1
            end += 1
        
        subset = adapters[idx:end]
    
    return total_number
    
def combinations(n, k):
    return math.factorial(n)/(math.factorial(k) * math.factorial(n - k))

def count_arrangements(removable_adapters):
    adapters_number = len(removable_adapters)
    subsets = number_of_subsets(removable_adapters)

    m = adapters_number
    n = subsets
    l = 3
    print(f"m: {m}; n: {n}; l: {l};")
    total_sum = 2**m
    for k_ in range(1, n+1):
        print(f"Adding: (-1)**{k_} * {combinations(n, k_)} * 2**({m-l*k_})")
        value = combinations(n, k_) * 2**(m-l*k_)
        total_sum += ((-1)**k_ * value) 
    
    return int(total_sum)
    

if __name__ == "__main__":

    with open(INPUT_FILE, "r") as input_:
        adapters = [int(line) for line in input_.read().split("\n")]
    
    differences, removable_adapters = find_differences(adapters)
    print(f"Differences: {differences}.")
    answer = differences["1"] * differences["3"]
    print(f"Product of 1-jolt and 3-jolt differences: {answer}.")
    
    print(f"Adapters ({len(adapters)}): {sorted(adapters)}.")
    print(f"Removable adapters ({len(removable_adapters)}): {removable_adapters}.")

    print(f"Possible arrangements: {count_arrangements(removable_adapters)}.")
