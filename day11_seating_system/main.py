
INPUT_FILE = "./input.txt"

class GridElement:
    EMPTY = 0
    OCCUPIED = 1
    def __init__(self, row, col):
        self._state = GridElement.EMPTY
        self._row = row
        self._col = col
    
    def is_occupied(self):
        if self._state == GridElement.OCCUPIED:
            return True
        
        return False
    
    def neighbours(self, max_row, max_col):
        neighours = list()
        offsets = [-1, 0, 1]
        for row_offset in offsets:
            row = self._row + row_offset
            if row < 0 or row > max_row:
                continue
            else:
                for col_offset in offsets:
                    col = self._col + col_offset
                    if col < 0 or col > max_col:
                        continue
                    else:
                        neighours.append((row, col))
        # Remove itself from the neighbours list.
        neighours.remove((self._row, self._col))
        return neighours

    def signature(self):
        return str(self._row) + str(self._col)

    def is_floor(self):
        return False

    def pprint(self):
        pass


class Seat(GridElement):
    NUMBER_OF_STATES = 2
    def __init__(self, row, col):
        GridElement.__init__(self, row, col)
        
    def switch_state(self):
        self._state = (self._state + 1) % Seat.NUMBER_OF_STATES

    def pprint(self):
        if self._state == GridElement.EMPTY:
            return "L"
        else:
            return "#"


class Floor(GridElement):
    
    def __init__(self, row, col):
        GridElement.__init__(self, row, col)

    def is_floor(self):
        return True

    def pprint(self):
        return "."


class GridFactory:
    FLOOR = "."
    SEAT = "L"
    def __init__(self):
        self.grid = list()

    def create_elements(self, grid_line):
        row_elements = list()
        row = len(self.grid)
        for col, element in enumerate(grid_line):
            if element == GridFactory.FLOOR:
                row_elements.append(Floor(row, col))
            elif element == GridFactory.SEAT:
                row_elements.append(Seat(row, col))

        self.grid.append(row_elements)

    def get_grid(self):
        return self.grid


def predict_seat_distribution(grid, max_row, max_col):
    iteration = 0
    while True:
        changes = 0
        # Compute occupied seats for current grid state.
        occupied_seats_map = adjacent_occupied_seats(grid)
        for row in grid:
            for element in row:
                # Ignore floor elements.
                if not element.is_floor():
                    seats = occupied_seats_map[str(element.signature())]
                    # Condition for state change empty -> occupied.
                    empty_condition = ((not element.is_occupied()) and (seats == 0))
                    # Condition for state change occupied -> empty.
                    occupied_condition = (element.is_occupied() and (seats >= 4))
                    if empty_condition or occupied_condition:
                            element.switch_state()
                            changes += 1
        if not changes:
            break

def adjacent_occupied_seats(grid):
    # Creates a map from element signature to number of 
    # adjacent occupied seats.
    map_ = dict()
    for row in grid:
        for element in row:
            if not element.is_floor():
                neighbours = element.neighbours(max_row, max_col)
                occupied_seats = 0
                for (row_, col_) in neighbours:
                    if grid[row_][col_].is_occupied():
                        occupied_seats += 1
                map_[element.signature()] = occupied_seats
    return map_

def occupied_seats(grid):
    # Returns the number of occupied seats in the given grid.
    seats = 0
    for row in grid:
        for element in row:
            if element.is_occupied():
                seats += 1
    return seats

def pprint_grid(grid):
    output_string = ""
    for row in grid:
        for element in row:
            output_string += element.pprint()
        output_string += "\n"
    
    print(output_string)
    
if __name__ == "__main__":

    grid_factory = GridFactory()
    length = 0
    with open(INPUT_FILE, "r") as input_:
        [grid_factory.create_elements(line) for line in input_.read().split("\n")]
    grid = grid_factory.get_grid()

    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    predict_seat_distribution(grid, max_row, max_col)
    print(f"Seats that end up occupied: {occupied_seats(grid)}.")
