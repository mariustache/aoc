
INPUT_FILE = "./input.txt"
DEBUG = True

def navigate(instructions, current_direction="E"):
    # Store distance on each direction.
    distances = {"N": 0, "E": 0, "S": 0, "W": 0}
    for action, value in instructions:
        if action in "LR":
            current_direction = rotate_ship(current_direction, action, value)
        elif action == "F":
            distances[current_direction] += value
        else:
            distances[action] += value

    return distances

def navigate_with_waypoint(instructions):
    # Store distance on each direction.
    ship = {"N": 0, "E": 0, "S": 0, "W": 0}
    # Initial waypoint coordinates, relative to the ship.
    waypoint_latitude = ["N", 1]
    waypoint_longitude = ["E", 10]

    for action, value in instructions:
        if action in "LR":
            waypoint_latitude[0] = rotate_ship(waypoint_latitude[0], action, value)
            waypoint_longitude[0] = rotate_ship(waypoint_longitude[0], action, value)
        # Only "F" action affects the ship coordinates.
        elif action == "F":
            ship[waypoint_latitude[0]] += (value * waypoint_latitude[1])
            ship[waypoint_longitude[0]] += (value * waypoint_longitude[1])
        # Any other action affects the coordinates of the waypoint.
        else:
            waypoint_latitude = update_position(waypoint_latitude, action, value)
            waypoint_longitude = update_position(waypoint_longitude, action, value)
    return ship

def update_position(position, action, value):
    opposites = {"N": "S", "E": "W", "S": "N", "W": "E"}
    direction, offset = position[0], position[1]
    # If action matches the current direction, update the value.
    if action == direction:
        offset += value
        return [action, offset]
    # If action is the opposite of current direction
    elif action == opposites[direction]:
        # If the current offset is lower than the input value,
        # change direction to its opposite and set the new value
        # to the absolute value of the difference.
        if offset < value:
            return [opposites[direction], value - offset]
        else:
            return [direction, offset - value]
        
    return position

def rotate_ship(direction, action, value):
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
        print(f"rotate_ship('N', 'L', 90).  Expected: W. Actual: {rotate_ship('N', 'L', 90)}")
        print(f"rotate_ship('N', 'L', 180). Expected: S. Actual: {rotate_ship('N', 'L', 180)}")
        print(f"rotate_ship('N', 'L', 270). Expected: E. Actual: {rotate_ship('N', 'L', 270)}")

        print(f"rotate_ship('N', 'R', 90).  Expected: E. Actual: {rotate_ship('N', 'R', 90)}")
        print(f"rotate_ship('N', 'R', 180). Expected: S. Actual: {rotate_ship('N', 'R', 180)}")
        print(f"rotate_ship('N', 'R', 270). Expected: W. Actual: {rotate_ship('N', 'R', 270)}")
    
    distances = navigate(instructions)
    print(f"Part one: {manhattan_distance(distances)}.")
    distances = navigate_with_waypoint(instructions)
    print(f"Part two: {manhattan_distance(distances)}.")