
import math
from functools import reduce

INPUT_FILE = "./input.txt"
START_TIMESTAMP = 100000000000000
TEST = False

def earliest_bus(timestamp, ids):
    departure_times = [math.ceil(timestamp/id_) * id_ for id_ in ids]
    waiting_times = [time - timestamp for time in departure_times]

    min_ = min(waiting_times)
    id_of_min = ids[waiting_times.index(min_)]
    return id_of_min, min_ 

def count_offsets(bus_ids):
    ids_with_offset = list()
    for index, id_ in enumerate(bus_ids):
        if id_ != "x":
            ids_with_offset.append((int(id_), index))
    
    return ids_with_offset

""" Naive.
def earliest_timestamp(start_timestamp, ids):
    # Computes the earliest timestamp such that all `ids` depart at offsets
    # matching their position in the `ids` list.
    timestamp, offset = first_timestamp(start_timestamp, ids[0])
    while True:
        if check_timestamp(timestamp, ids):
            break
        else:
            # If current timestamp does not follow the rule, increment the timestamp.
            timestamp += offset

    return timestamp

def first_timestamp(timestamp, id_):
    # Computes the first timestamp that is a multiple of id.
    while True:
        if math.ceil(timestamp/id_[0]) * id_[0] == timestamp + id_[1]:
            break
        timestamp += 1
    return timestamp, id_[0]

def check_timestamp(timestamp, ids):
    for (id_, offset_) in ids:
        print(f"Timestamp: {timestamp}. Id: {id_}.")
        if (math.ceil((timestamp)/id_) * id_) != timestamp + offset_:
            # If one of the ids do not follow the rule, stop checking for current timestamp.
            return False

    return True
"""

def check_coprime(ids):
    for idx, id_ in enumerate(ids[:-1]):
        print(f"Checking {id_} against range: {ids[idx+1:]}")
        for next_id in ids[idx+1:]:
            if math.gcd(id_, next_id) != 1:
                return False
    return True

def mod_inv(p, id_):
    # Finds the multiplier `k`, such that p*k % id_ = 1.
    k = 1
    while p*k % id_ != 1:
        k += 1
    
    return k

def chinese_remainder(ids, offsets):
    # Find a solution for x mod t = 0, x mod t+k = k, for each k found in offsets.
    # Compute the product of all ids.
    prod = reduce(lambda x, y: x*y, ids)
    total_sum = 0
    for id_, offset_ in zip(ids, offsets):
        # t + offset_ = j*id_ => t = j*id_ - offset_
        remainder_ = id_ - offset_
        # Divide current id in order to find the number p*k mod id_ = 1
        p = prod // id_
        total_sum += (remainder_ * mod_inv(p, id_) * p)
    
    return total_sum % prod


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as input_:
        first, second = [line.strip() for line in input_.readlines()]
        timestamp = int(first)
        bus_ids = [int(id_) for id_ in second.split(",") if id_ != "x"]
        bus_ids_offsets = count_offsets(second.split(","))
        
    id_, waiting_time = earliest_bus(timestamp, bus_ids)
    print(f"Timestamp: {timestamp}.")
    print(f"Earliest bus (id: {id_}) leaves at: {timestamp + waiting_time}.")
    print(f"Waiting time: {waiting_time}.")

    print(f"Part one answer: {id_ * waiting_time}.")
    if TEST:
        bus_ids_offsets = [(7, 0), (13, 1), (59,4), (31, 6), (19, 7)]
        print(f"Expected: {1068781}. Actual: {earliest_timestamp(0, bus_ids_offsets)}")

        bus_ids_offsets = [(17, 0), (13, 2), (19,3)]
        print(f"Expected: {3417}. Actual: {earliest_timestamp(0, bus_ids_offsets)}")

        bus_ids_offsets = [(67, 0), (7, 1), (59, 2), (61, 3)]
        print(f"Expected: {754018}. Actual: {earliest_timestamp(0, bus_ids_offsets)}")

        bus_ids_offsets = [(67, 0), (7, 2), (59, 3), (61, 4)]
        print(f"Expected: {779210}. Actual: {earliest_timestamp(0, bus_ids_offsets)}")

        bus_ids_offsets = [(67, 0), (7, 1), (59, 3), (61, 4)]
        print(f"Expected: {1261476}. Actual: {earliest_timestamp(0, bus_ids_offsets)}")

        bus_ids_offsets = [(1789, 0), (37, 1), (47,2), (1889, 3)]
        print(f"Expected: {1202161486}. Actual: {earliest_timestamp(0, bus_ids_offsets)}")

        exit()

    if not check_coprime(bus_ids):
        print(f"The numbers are not coprime. Numbers: {bus_ids}.")
        exit()
    else:
        print(f"Apply Chinese Remainder Theorem to find the earliest timestamp.")
        ids, offsets = zip(*bus_ids_offsets)
        print(ids, offsets)
        print(f"Part two answer: {chinese_remainder(ids, offsets)}.")