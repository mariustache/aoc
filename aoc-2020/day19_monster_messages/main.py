from typing import List, Dict

INPUT_FILE = "./input.txt"

class Rule:

    def __init__(self, _subrules):
        self.subrules = _subrules
        self.children_options = list()

    def add_option(self, child_option):
        self.children_options.append(child_option)


class LeafRule:
    
    def __init__(self, _value):
        self.value = _value
    
    def match(self, _value):
        return self.value == _value

    def value(self):
        return self.value


if __name__ == "__main__":

    rules_map = dict()
    messages = list()
    with open(INPUT_FILE, "r") as input_:
        rules, messages = input_.read().split("\n\n")
        rules = rules.split("\n")
        messages = messages.split("\n")
        for rule in rules:
            _id, subrules = rule.split(": ")
            subrules = subrules.replace("\"", "")
            if len(subrules) == 1 and not subrules.isnumeric():
                rules_map[_id] = LeafRule(subrules)
            else:
                rules_map[_id] = Rule(subrules)
    # For each Rule instance, map its subrules to actual instances.        
    for key, rule in rules_map.items():
        if type(rule) == Rule:
            options = rule.subrules.split(" | ")
            for option in options:
                ids = option.split(" ")
                child_option = [rules_map[_id] for _id in ids]
                rule.add_option(child_option)
    
    for message in messages:
        print(rules_map['0'].match())
