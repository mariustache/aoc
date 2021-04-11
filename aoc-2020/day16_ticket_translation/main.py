import re
from functools import reduce

INPUT_FILE = "./input.txt"

class Ticket:

    def __init__(self):
        self.data = list()

    def add_fields(self, data):
        self.data = [int(entry) for entry in data]
    
    def is_valid(self, rules):
        valid = True
        value = 0
        for entry in self.data:
            in_range = False
            value = entry
            for rule in rules:
                if rule.is_valid(entry):
                    in_range = True
                    break
            if not in_range:
                valid = False
                break
                            
        return valid, value

class Rule:
    names = list()

    def __init__(self, name):
        self.name = name
        self.ranges = list()
        if name not in Rule.names:
            Rule.names.append(name)
    
    def add_range(self, _range):
        self.ranges.append(_range)

    def is_valid(self, value):
        in_range = False
        for _range in self.ranges:
            if value >= _range[0] and value <= _range[1]:
                in_range = True
                break

        return in_range

def scan(tickets, rules):
    error_rate = 0
    valid_tickets = list()
    for ticket in tickets:
        valid, value = ticket.is_valid(rules)
        if not valid:
            error_rate += value
        else:
            valid_tickets.append(ticket)

    return error_rate, valid_tickets

def determine_fields(tickets, rules):
    length = len(tickets[0].data)
    fields = list()
    for idx in range(0, length):
        rule_list = list()
        for rule in rules:
            all_valid = True
            for ticket in tickets:
                value = ticket.data[idx]
                if not rule.is_valid(value):
                    all_valid = False
                    break
            if all_valid:
                rule_list.append(rule.name)
        fields.append([idx, rule_list])    

    fields = sorted(fields, key=lambda x: len(x[-1]))
    already_added = list()
    index_list = list()
    for field_list in fields:
        for field in field_list[-1]:
            if field not in already_added:
                already_added.append(field)
                index_list.append(field_list[0])
    return zip(index_list, already_added)

def departure_values(fields, ticket):
    keyword = "departure"
    index_list = list()
    for field in fields:
        if keyword in field[-1]:
            index_list.append(field[0])
    
    product = 1
    for index in index_list:
        product *= ticket.data[index]
    
    return product

def parse_rules(data):
    rules = list()
    for rule in data:
        rule_obj = Rule(rule.split(":")[0])
        ranges = rule.split(":")[-1].replace(" ", "").split("or")
        for _range in ranges:
            numbers = [int(number) for number in _range.split("-")]
            rule_obj.add_range(numbers)
        
        rules.append(rule_obj)
    
    return rules

if __name__ == "__main__":
    rules = list()
    my_ticket = Ticket()
    tickets = list()

    with open(INPUT_FILE, "r") as input_:
        # Split input into three parts: rules, my ticket and nearby tickets
        keyword_ticket = "your ticket:"
        keyword_nearby = "nearby tickets:"
        data = input_.read().split("\n")
        ticket_index = data.index(keyword_ticket)
        rules_index = ticket_index - 1
        nearby_index = data.index(keyword_nearby) + 1

        rules = parse_rules(data[:rules_index])
    
        my_ticket.add_fields(data[ticket_index+1].split(","))

        for ticket_data in data[nearby_index:]:
            ticket = Ticket()
            ticket.add_fields(ticket_data.split(","))
            tickets.append(ticket)
    
    error_rate, valid_tickets = scan(tickets, rules)
    print(f"Part 1. Error rate: {error_rate}")
    
    fields = determine_fields(valid_tickets, rules)
    departure_value = departure_values(fields, my_ticket)
    print(f"Part 2. Departure values multiplied: {departure_value}")