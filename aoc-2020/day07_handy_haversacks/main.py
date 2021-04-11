
INPUT_FILE = "./input.txt"

class BagCategory:

    def __init__(self, name, children):
        self.name = name
        self.children = children
        self.children_bags = dict()
        self.bags_number = 0
    
    def children_names(self):
        return list(self.children.keys())

    def add_child_bag(self, bag):
        self.children_bags[bag.name] = bag

    def can_contain_bag(self, bag_name):
        if bag_name in self.children:
            return True
        else:
            for key, bag in self.children_bags.items():
                result = bag.can_contain_bag(bag_name)
                if result:
                    return True
        return False

    def number_of_bags(self, iteration=0):
        prefix = " "*iteration
        print(prefix + f"### ENTER {self.name} ####")
        print(prefix + f"{self.children}")
        total_bags = 0
        if self.children:
            for key, quantity in self.children.items():
                total_bags += quantity
                number = self.children_bags[key].number_of_bags(iteration + 1)
                total_bags += quantity * number
        print(prefix + f"Total bags: {total_bags}")
        print(prefix + f"### EXIT {self.name} ####")
        return total_bags


class BagCategoryFactory:

    def __init__(self):
        self.categories = dict()

    def create_category(self, input_string):
        name, children = parse_bag_rule(input_string)
        category = BagCategory(name, children)
        self.categories[name] = category

        return category
    
    def populate_categories(self):
        for key, category in self.categories.items():
            for child_bag in category.children_names():
                if child_bag in self.categories:
                    category.add_child_bag(self.categories[child_bag])
                else:
                    print(f"Child bag '{child_bag}' not in categories.")


def parse_bag_rule(bag_rule):
    splited = bag_rule.split("contain ")
    bag = splited[0].split(" ")
    bag_name = " ".join(bag[0:2])
    
    if "no other" in bag_rule:
        return bag_name, dict()

    children_bags = splited[-1].split(", ")

    bags = dict()
    for bag in children_bags:
        elements = bag.split(" ")
        quantity = elements[0]
        color_code = " ".join(elements[1:-1])
        bags[color_code] = int(quantity)

    return bag_name, bags


if __name__ == "__main__":

    factory = BagCategoryFactory()
    with open(INPUT_FILE, "r") as input_:
        bag_categories = [factory.create_category(line) for line in input_.read().split("\n")]
    
    factory.populate_categories()

    bag_name = "shiny gold"
    bags_counter = 0
    for bag_category in bag_categories:
        if bag_category.can_contain_bag(bag_name):
            bags_counter += 1
        
    print(f"The number of bags that can contain at least one '{bag_name}' bag is: {bags_counter}")
    print(f"Number of individual bags required in a single '{bag_name}' bag: {factory.categories[bag_name].number_of_bags()}")
