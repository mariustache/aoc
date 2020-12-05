
INPUT_FILE = "./input.txt"

class Passport:

    parts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

    def __init__(self):
        self.data = dict()
    
    def add(self, key, value):
        self.data[key] = value
    
    def is_valid(self):
        missing_parts = list()
        for part in Passport.parts:
            if part not in self.data:
                missing_parts.append(part)
                if len(missing_parts) > 1:
                    return False
            else:
                if not self.check_part(part):
                    return False

        if len(missing_parts) == 1:
            if "cid" not in missing_parts:
                return False

        return True
    
    def check_part(self, part):
        is_valid = False
        if part in self.data:
            if part == "byr":
                is_valid = self.check_birth_year(int(self.data[part]))
            elif part == "iyr":
                is_valid = self.check_issue_year(int(self.data[part]))
            elif part == "eyr":
                is_valid = self.check_expiration_year(int(self.data[part]))
            elif part == "hgt":
                is_valid = self.check_height(self.data[part])
            elif part == "hcl":
                is_valid = self.check_hair_color(self.data[part])
            elif part == "ecl":
                is_valid = self.check_eye_color(self.data[part])
            elif part == "pid":
                is_valid = self.check_passport_id(self.data[part])
            else:
                is_valid = True

        return is_valid

    def check_birth_year(self, value):
        if len(str(value)) != 4:
            print("ERROR: Birth year length not 4.")
            return False
        if value < 1920 or value > 2002:
            print("ERROR: Birth year not between 1920 and 2002.")
            return False
        
        return True
    
    def check_issue_year(self, value):
        if len(str(value)) != 4:
            print("ERROR: Issue year length not 4.")
            return False
        if value < 2010 or value > 2020:
            print("ERROR: Issue year not between 2010 and 2020.")
            return False

        return True

    def check_expiration_year(self, value):
        if len(str(value)) != 4:
            print("ERROR: Expiration year length not 4.")
            return False
        if value < 2020 or value > 2030:
            print("ERROR: Expiration year not between 2020 and 2030.")
            return False

        return True

    def check_height(self, value):
        if "cm" in value:
            number = int(value.replace("cm", ""))
            if number < 150 or number > 193:
                print("ERROR: Height(cm) not between 150 and 193.")
                return False
        elif "in" in value:
            number = int(value.replace("in", ""))
            if number < 59 or number > 76:
                print("ERROR: Height(in) not between 59 and 76.")
                return False
        else:
            print("ERROR: 'cm' or 'in' not found in value.")
            return False
        
        return True
    
    def check_hair_color(self, value):
        if len(value) != 7:
            print("ERROR: Hair color length not 7.")
            return False
        elif value[0] != "#":
            print("ERROR: Hair color not starting with '#'.")
            return False
        else:
            try:
                hex_value = int(value[1:], 16)
            except ValueError:
                print("ERROR: Hair color values are not '0-9a-f'.")
                return False
        return True
    
    def check_eye_color(self, value):
        if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            print("ERROR: Eye color invalid value.")
            return False
        return True
    
    def check_passport_id(self, value):
        if len(value) != 9:
            print("ERROR: Passport id length not 9.")
            return False
        elif not value.isdigit():
            print("ERROR: Passport id contains an invalid value.")
            return False
        
        return True

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