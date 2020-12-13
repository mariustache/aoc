
INPUT_FILE = "./input.txt"

class GridElement:
    EMPTY = 0
    OCCUPIED = 1
    def __init__(self):
        self._state = GridElement.EMPTY
    
    def is_occupied(self):
        if self._state != GridElement.EMPTY:
            return True
        
        return False

class Seat(GridElement):
    NUMBER_OF_STATES = 2
    def __init__(self):
        GridElement.__init__(self)
        
    def switch_state(self):
        self._state = (self._state + 1) % Seat.NUMBER_OF_STATES

class Floor(GridElement):
    
    def __init__(self):
        GridElement.__init__(self)


class GridFactory:
    FLOOR = "."
    SEAT = "L"
    def __init__(self):
        self.elements = list()

    def create_elements(self, grid_line):
        for element in grid_line:
            if element == GridFactory.FLOOR:
                self.elements.append(Floor())
            elif element == GridFactory.SEAT:
                self.elements.append(Seat())

if __name__ == "__main__":

    grid_factory = GridFactory()
    with open(INPUT_FILE, "r") as input_:
        adapters = [grid_factory.create_elements(line) for line in input_.read().split("\n")]
    
    