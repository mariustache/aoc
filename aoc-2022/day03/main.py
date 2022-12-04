lowercase_priority = ord('a') - 1
uppercase_priority = ord('A') - 27

def find_duplicated_item(rucksack):
    halfway = int(len(rucksack)/2)
    compartment1, compartment2 = rucksack[0:halfway], rucksack[halfway:]
    common = list(set(compartment1) & set(compartment2))
    assert(len(common) == 1)
    return convert_to_priority(common[0])

def find_common_badge(rucksack_group):
    rucksacks = list(map(set, rucksack_group))
    common = list(rucksacks[0] & rucksacks[1] & rucksacks[2])
    assert(len(common) == 1)
    return convert_to_priority(common[0])

def convert_to_priority(item):
    priority = lowercase_priority if item.islower() else uppercase_priority
    return ord(item) - priority

if __name__ == "__main__":
    rucksacks = list()
    with open("./input.txt", "r") as handle:
        rucksacks = handle.read().split("\n")

    print(f"[part1] Priorities sum: {sum([find_duplicated_item(rucksack) for rucksack in rucksacks])}")

    priority_sum = 0
    i = 0
    while i < len(rucksacks):
        priority_sum += find_common_badge(rucksacks[i:i+3])
        i += 3
    
    print(f"[part2] Priorities sum: {priority_sum}")
