
def contain(x, y):
    return x[0] >= y[0] and x[1] <= y[1]

def overlap(x, y):
    _range = range(y[0], y[1] + 1)
    return x[0] in _range or x[1] in _range

def solve(x, criterion):
    return criterion(x[0], x[1]) or criterion(x[1], x[0])

def tuplify(x):
    x = list(map(lambda y: tuple(map(int, y.split("-"))), x))
    return x

def process(path):
    with open(path, "r") as handle:
        data = handle.read().split("\n")
        data = map(lambda x: x.split(","), data)
        data = map(tuplify, data)
    return list(data)

if __name__ == "__main__":
    data = process("./test.txt")
    test = sum([solve(x, contain) for x in data])
    assert test == 2, f"test failed, expected: {2}, got: {test}"
    test = sum([solve(x, overlap) for x in data])
    assert test == 4, f"test2 failed, expected: {4}, got: {test}"

    data = process("./input.txt")
    print(f"[part1] Answer: {sum([solve(x, contain) for x in data])}")
    print(f"[part2] Answer: {sum([solve(x, overlap) for x in data])}")
