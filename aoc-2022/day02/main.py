
score_offset = 64
ascii_offset = 23 # 'X' - 'A'

def compute_score(_round):
    score = _round[1] - ascii_offset - score_offset
    diff = _round[1] - _round[0] - ascii_offset
    if diff in [-2, 1]:
        score += 6
    elif diff == 0:
        score += 3

    return score

def compute_score_2(_round):
    score = 0
    if _round[1] == ord('X'):
        if _round[0] == ord('A'):
            score += 3
        else:
            score += _round[0] - score_offset - 1
    elif _round[1] == ord('Y'):
        score += _round[0] - score_offset + 3
    else:
        if _round[0] == ord('B'):
            score += 3 + 6
        else:
            score += (_round[0] - score_offset + 1) % 3 + 6
    return score

if __name__ == "__main__":
    rounds = list()
    with open("./input.txt", "r") as handle:
        rounds = handle.read().split("\n")
        rounds = [list(map(ord, _round.split(" "))) for _round in rounds]
    
    total_score = sum([compute_score(_round) for _round in rounds])
    print(f"[part1] Total score: {total_score}")
    total_score = sum([compute_score_2(_round) for _round in rounds])
    print(f"[part2] Total score: {total_score}")