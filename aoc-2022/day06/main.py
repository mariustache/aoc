
def solve(stream, length):
    chars = list()
    end = 0
    for i, c in enumerate(stream):
        if c in chars:
            idx = chars.index(c)
            chars = chars[idx+1:]
        chars.append(c)
        if len(chars) == length:
            end = i + 1
            break

    return end
def test():
    stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    val = solve(stream, 4)
    assert val == 5, f"test failed, expected: 5, got: {val}"
    val = solve(stream, 14)
    assert val == 23, f"test failed, expected: 23, got: {val}"
    stream = "nppdvjthqldpwncqszvftbrmjlhg"
    val = solve(stream, 4)
    assert val == 6, f"test failed, expected: 6, got: {val}"
    val = solve(stream, 14)
    assert val == 23, f"test failed, expected: 23, got: {val}"
    stream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    val = solve(stream, 4)
    assert val == 10, f"test failed, expected: 10, got: {val}"
    val = solve(stream, 14)
    assert val == 29, f"test failed, expected: 29, got: {val}"
    stream = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    val = solve(stream, 4)
    assert val == 11, f"test failed, expected: 11, got: {val}"
    val = solve(stream, 14)
    assert val == 26, f"test failed, expected: 26, got: {val}"

    pass
if __name__ == "__main__":
    test()

    with open("./input.txt", "r") as handle:
        stream = handle.read()

    answer = solve(stream, 4)
    print(f"[part1] Answer: {answer}")
    answer = solve(stream, 14)
    print(f"[part2] Answer: {answer}")
