
INPUT_FILE = "./input.txt"

class Passport:

    parts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    def __init__(self):
        self.data = dict()
    
    def add(self, key, value):
        self.data[key] = value
    
    def is_valid(self, suppress_output=True):
        _is_valid = True
        missing_parts = list()
        for part in Passport.parts:
            if part not in self.data:
                missing_parts.append(part)
        if len(missing_parts) > 1:
            _is_valid = False
        elif len(missing_parts) == 1:
            if "cid" not in missing_parts:
                _is_valid = False

        if not suppress_output and not _is_valid:
            print(f"Invalid passport.")
            print(f"Missing parts: {missing_parts}")
            
        return _is_valid
    
    def check_birth_year(self):
        if self.data.has_key("byr"):
            pass
    
    def pprint(self):
        print("#### PASSPORT DATA ####")
        for part in self.data:
            print(f"{part}:{self.data[part]}")
        print("#### ####")


class PassportBuilder:

    def __init__(self):
        self.reset()

    def build_passport(self, input_string):
        parts = " ".join(input_string.split("\n")).split(" ")
        print("#### Building new passport ####")
        for part in parts:
            # The value is the substring from ":" to end.
            _part = part.split(":")
            name = _part[0]
            value = _part[-1]
            print(f"Adding part {name}: {value}")
            self.set_part(name, value)
        print("#### Done ####")
        print("")
        passport = self.passport
        self.reset()

        return passport
    
    def reset(self):
        self.passport = Passport()
    
    def set_part(self, part, value):
        self.passport.add(part, value)


if __name__ == "__main__":

    builder = PassportBuilder()
    with open(INPUT_FILE, "r") as input_:
        passports = [builder.build_passport(line) for line in input_.read().split("\n\n")]
    
    valid_passports = 0
    for passport in passports:
        if passport.is_valid():
            valid_passports += 1

    print(f"Valid passports: {valid_passports}.")