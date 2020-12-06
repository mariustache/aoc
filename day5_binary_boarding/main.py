
INPUT_FILE = "./input.txt"

class BoardingPass:

    BITS_FOR_ROW = 7
    BITS_FOR_COL = 3
    SEAT_MAX_ROW = 2**BITS_FOR_ROW - 1
    SEAT_MAX_COL = 2**BITS_FOR_COL - 1

    def __init__(self, data):
        self.data = data

        self.row = 0
        self.col = 0
    
    def decode(self):
        # Decode seat from encoded data.
        # First BITS_FOR_ROW bits encode the seat row.
        row_data = self.data[:BoardingPass.BITS_FOR_ROW]
        # Last BITS_FOR_COL bits encode the seat column.
        col_data = self.data[BoardingPass.BITS_FOR_ROW:]

        self.row = self.decode_from_key(["F", "B"], row_data, BoardingPass.SEAT_MAX_ROW)
        self.col = self.decode_from_key(["L", "R"], col_data, BoardingPass.SEAT_MAX_COL)
    
    def decode_from_key(self, keys, encoded_data, max_value):
        _lower = 0
        _upper = max_value
        _left = keys[0]
        _right = keys[1]
        result = 0

        for _char in encoded_data:
            if _char == _left:
                _upper = (_upper + _lower)//2
                result = _upper
            elif _char == _right:
                _lower = (_upper + _lower)//2 + 1
                result = _lower
            else:
                print(f"ERROR: Invalid character '{_char}'.")
            #print(f"Char: {_char}. Range: [{_lower}, {_upper}].")
        return result

    def seat_id(self):
        return self.row * 8 + self.col

if __name__ == "__main__":

    with open(INPUT_FILE, "r") as input_:
        boarding_passes = [BoardingPass(line) for line in input_.read().split("\n")]
    
    seat_ids = list()
    for boarding_pass in boarding_passes:
        boarding_pass.decode()
        seat_ids.append(boarding_pass.seat_id())
    
    sorted_seats = sorted(seat_ids)
    current_seat = sorted_seats[0]
    for seat_id in sorted_seats[1:]:
        if seat_id - 1 != current_seat:
            print(f"Found the missing seat: {seat_id - 1}. Current seat: {current_seat}")
            break
        current_seat = seat_id
    print(f"Highest seat id: {max(seat_ids)}.")