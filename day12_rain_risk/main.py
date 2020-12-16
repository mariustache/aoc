
INPUT_FILE = "./input.txt"
DEBUG = True

def navigate(instructions, current_direction="E"):
    # Store distance on each direction.
    distances = {"N": 0, "E": 0, "S": 0, "W": 0}
    for instruction in instructions:
        action, value = instruction[0], instruction[1]
        if action in "LR":
            current_direction = update_direction(current_direction, action, value)
        elif action == "F":
            distances[current_direction] += value
        else:
            distances[action] += value
    return distances

def update_direction(direction, action, value):
    directions = "NESW"
    # Extract position of the given direction.
    pos = directions.find(direction)
    # Compute the number of 90 turns.
    turns = value // 90
    # Extract position of new direction.
    pos += (action == "R") * turns
    pos -= (action == "L") * turns
    pos %= len(directions)

    return directions[pos]

def compute_position(distances, coords):
    diff = distances[coords[0]] - distances[coords[1]]
    return [coords[(diff < 0)], abs(diff)]
    
def manhattan_distance(distances):
    longitude = compute_position(distances, ("E", "W"))
    latitude = compute_position(distances, ("N", "S"))
    if DEBUG:
        print(f"Latitude: {latitude}.")
        print(f"Longitude: {longitude}.")
    return longitude[1] + latitude[1]


if __name__ == "__main__":
    with open(INPUT_FILE, "r") as input_:
        instructions = [(line[0], int(line[1:])) for line in input_.read().split("\n")]

    if DEBUG:
        print(f"update_direction('N', 'L', 90).  Expected: W. Actual: {update_direction('N', 'L', 90)}")
        print(f"update_direction('N', 'L', 180). Expected: S. Actual: {update_direction('N', 'L', 180)}")
        print(f"update_direction('N', 'L', 270). Expected: E. Actual: {update_direction('N', 'L', 270)}")

        print(f"update_direction('N', 'R', 90).  Expected: E. Actual: {update_direction('N', 'R', 90)}")
        print(f"update_direction('N', 'R', 180). Expected: S. Actual: {update_direction('N', 'R', 180)}")
        print(f"update_direction('N', 'R', 270). Expected: W. Actual: {update_direction('N', 'R', 270)}")
    
    distances = navigate(instructions)
    print(manhattan_distance(distances))