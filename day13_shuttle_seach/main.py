
import math

INPUT_FILE = "./input.txt"

def earliest_bus(timestamp, ids):
    departure_times = [math.ceil(timestamp/id_) * id_ for id_ in ids]
    waiting_times = [time - timestamp for time in departure_times]

    min_ = min(waiting_times)
    id_of_min = ids[waiting_times.index(min_)]
    return id_of_min, min_ 

if __name__ == "__main__":
    with open(INPUT_FILE, "r") as input_:
        timestamp, bus_ids = [line.strip() for line in input_.readlines()]
        timestamp = int(timestamp)
        bus_ids = [int(id_) for id_ in bus_ids.split(",") if id_ != "x"]
        
    id_, waiting_time = earliest_bus(timestamp, bus_ids)
    print(f"Timestamp: {timestamp}.")
    print(f"Earliest bus (id: {id_}) leaves at: {timestamp + waiting_time}.")
    print(f"Waiting time: {waiting_time}.")

    print(f"Part one answer: {id_ * waiting_time}.")