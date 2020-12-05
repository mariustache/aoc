
INPUT_FILE = "./input.txt"

class PasswordPolicy:
    DELIMITER = " "
    RANGE_DELIMITER = "-"

    def __init__(self, input_string):
        l, h, key, password = self._parse_input(input_string)

        self.range = range(l, h+1)
        self.lowest = l
        self.highest = h
        self.key = key
        self.password = password

    def _parse_input(self, input_):
        splited = input_.split(PasswordPolicy.DELIMITER)

        range_ = splited[0].split(PasswordPolicy.RANGE_DELIMITER)        
        l, h = int(range_[0]), int(range_[1])

        key = splited[1][0]
        
        password = splited[2]

        return l, h, key, password

    def is_password_valid(self):
        key_occurences = self.password.count(self.key)
        if key_occurences in self.range:
            return True
        return False
    
    def is_password_valid_official(self):
        is_low = self.password[self.lowest - 1] == self.key
        is_high = self.password[self.highest - 1] == self.key

        if (is_low and not is_high) or (is_high and not is_low):
            return True
        return False


if __name__ == "__main__":
    policies = list()
    with open(INPUT_FILE, "r") as input_:
        policies = [PasswordPolicy(line) for line in input_.read().split("\n")]
    
    valid_passwords = 0
    for policy in policies:
        if policy.is_password_valid():
            valid_passwords += 1
    
    print("##### Initial policy rules #####")
    print(f"Valid passwords: {valid_passwords}.")
    print(f"Invalid passwords: {len(policies) - valid_passwords}.")
    print(f"Total passwords: {len(policies)}")

    valid_passwords = 0
    for policy in policies:
        if policy.is_password_valid_official():
            valid_passwords += 1

    print("##### Official policy rules #####")
    print(f"Valid passwords: {valid_passwords}.")
    print(f"Invalid passwords: {len(policies) - valid_passwords}.")
    print(f"Total passwords: {len(policies)}")