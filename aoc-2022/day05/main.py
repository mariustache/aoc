import re

class Stack:
    def __init__(self, state):
        self.state = state

    def pop(self, n, reverse=True):
        assert n <= len(self.state), f"n: {n}, state length: {len(self.state)}, {self.pprint()}"
        head_n = self.state[-n:]
        if reverse:
            head_n.reverse()
        self.state = self.state[:-n]
        return head_n
    
    def push(self, x):
        self.state += x
    
    def head(self):
        return self.state[-1]

    def pprint(self):
        state = self.state[::-1]
        for x in state:
            print(f"[{x}]")
        print("---")

def solve(stacks, moves, reverse=True):
    for move in moves:
        n, _from, _to = move
        #print(f"Moving {n} crate(s) from {_from} to {_to}")
        x = stacks[_from-1].pop(n, reverse)
        stacks[_to-1].push(x)

    val = str()
    for stack in stacks:
        val += stack.head()
    return val

def parse_states(states):
    states = states.split("\n")
    states.reverse()

    n = len(states[0].replace(" ", ""))
    stacks = [Stack(list()) for i in range(n)]

    for state in states[1:]:
        for i in range(n):
            start, end = 4*i, 4*i+2
            c = state[start:end+1]
            if c != "   ":
                stacks[i].push(c[1:-1])
    
    return stacks

def parse_procedure(procedure):
    moves = list()
    for move in procedure:
        m = re.match("move (\d+) from (\d+) to (\d+)", move)
        moves.append(list(map(int, m.groups())))
    return moves

def parse(path):
    with open(path, "r") as handle:
        data = handle.read().split("\n\n")
        
    stacks = parse_states(data[0])
    moves = parse_procedure(data[1].split("\n"))
    return stacks, moves

def test():
    stacks = list()
    stacks.append(Stack(["Z", "N"]))
    stacks.append(Stack(["M", "C", "D"]))
    stacks.append(Stack(["P"]))
    
    moves = list()
    moves.append((1, 2, 1))
    moves.append((3, 1, 3))
    moves.append((2, 2, 1))
    moves.append((1, 1, 2))
    
    val = solve(stacks, moves)
    assert val == "CMZ", f"test failed, expected: CMZ, got: {val}"

if __name__ == "__main__":
    test()

    stacks, moves = parse("./input.txt")
    answer = solve(stacks, moves)
    print(f"[part1] Answer: {answer}")

    stacks, moves = parse("./input.txt")
    answer = solve(stacks, moves, reverse=False)
    print(f"[part2] Answer: {answer}")
