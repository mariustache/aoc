
INPUT_FILE = "./input.txt"

class TreeMap:
    SQUARE_SYMBOL = "."
    TREE_SYMBOL = "#"

    def __init__(self):
        self.lines = list()
        self.trees = dict()
        self.width = 0
        self.length = 0

    def add_line(self, line):
        self.lines.append(line)

    def set_map_dimensions(self):
        self.width = len(self.lines[0])
        print(f"Width set to: {self.width}.")
        self.length = len(self.lines)
        print(f"Length set to: {self.length}.")

    def find_trees(self):
        for idx, line in enumerate(self.lines):
            self.trees[idx] = self.tree_positions(line)
            print(f"Trees on row {idx} are found on columns: {self.trees[idx]}")

    def tree_positions(self, line):
        positions = list()
        for idx, char_ in enumerate(line):
            if char_ == TreeMap.TREE_SYMBOL:
                positions.append(idx)
        
        return positions
    
    def travel(self, right, down):
        current_row = down
        current_col = right
        encountered_trees = 0

        while current_row < self.length:
            if current_col in self.trees[current_row]:
                encountered_trees += 1
            current_col = (current_col + right) % self.width 
            current_row += down 
        
        return encountered_trees

if __name__ == "__main__":

    tree_map = TreeMap()
    with open(INPUT_FILE, "r") as input_:
        [tree_map.add_line(line) for line in input_.read().split("\n")]
    
    tree_map.set_map_dimensions()
    tree_map.find_trees()

    slope_pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for pair in slope_pairs:
        print(f"##### Slope: right({pair[0]}), down({pair[1]}) #####")
        trees = tree_map.travel(pair[0], pair[1])
        print(f"Encountered trees: {trees}.")
        print("##### #####")
        product *= trees
    
    print("##### Final result #####")
    print(f"Product of all encountered trees: {product}")