from __future__ import annotations

class FsParser:
    dirs = list()

    def __init__(self):
        self.root = Directory("/")
        self.cd = self.root
    
    def parse_cmd(self, cmd):
        args = cmd.split(" ")
        if args[0] == "$":
            if args[1] == "cd":
                assert len(args) == 3, f"Incorrect command: {cmd}"
                if args[2] == "..":
                    self.cd = self.cd.parent
                else:
                    child = self.cd.get_child(args[2])
                    assert child is not None, f"Child with name {args[2]} not found in current directory: {self.cd.name}"
                    self.cd = child
            elif args[1] == "ls":
                assert len(args) == 2, f"Incorrect command: {cmd}"
                pass
            else:
                raise f"Wrong command {args[1]}"
        elif args[0] == "dir":
            assert len(args) == 2, f"Incorrect command: {cmd}"
            _dir = Directory(args[1], parent=self.cd)
            FsParser.dirs.append(_dir)
            self.cd.add_child(_dir)
        else:
            assert len(args) == 2, f"Incorrect command: {cmd}"
            self.cd.add_child(File(args[0], args[1], self.cd))

    @staticmethod
    def solve(max_size: int = 100000):
        sizes = [_dir.size() for _dir in FsParser.dirs]
        sizes = list(filter(lambda x: x <= max_size, sizes))
        return sum(sizes)

    @staticmethod
    def solve2(used_size: int = 0):
        total_size = 70000000
        needed_size = 30000000
        unused_size = total_size - used_size
        to_free_size = needed_size - unused_size
        sizes = [_dir.size() for _dir in FsParser.dirs]
        sizes = list(filter(lambda x: x >= to_free_size, sizes))
        return min(sizes)

class File:
    def __init__(self, size: int, name: str, parent: Directory):
        self._size = int(size)
        self.name = name
        self.parent = parent

    def size(self) -> int:
        return self._size
    
    def pprint(self, depth=0):
        print(4*" "*depth, f"- {self.name} (file, size={self._size})")

class Directory:
    
    def __init__(self, name: str, parent: Directory = None):
        self.name = name
        self.parent = parent
        self.children = list()

    def size(self) -> int:
        return sum([child.size() for child in self.children])
    
    def get_child(self, name: str):
        child = None
        for c in self.children:
            if c.name == name:
                child = c
                break
        return child

    def add_child(self, child: Directory | File):
        self.children.append(child)

    def pprint(self, depth=0):
        print(4*" "*depth, f"- {self.name} (dir)")
        for child in self.children:
            child.pprint(depth + 1)
    
    @classmethod
    def print_tree(cls, root: Directory):
        root.pprint()

def solve(path: str, _print: bool = False):
    with open(path, "r") as handle:
        cmds = handle.read().split("\n")

    parser = FsParser()
    for cmd in cmds[1:]:
        parser.parse_cmd(cmd)

    if _print:
        Directory.print_tree(root=parser.root)

    return FsParser.solve(), FsParser.solve2(parser.root.size())

if __name__ == "__main__":
    val1, val2 = solve("./test.txt", _print=True)
    assert val1 == 95437, f"test failed, expected: 95437, got: {val1}"
    assert val2 == 24933642, f"test failed, expected: 24933642, got: {val2}"
    FsParser.dirs = list()

    answer1, answer2 = solve("./input.txt")
    print(f"[part1] Answer: {answer1}")
    print(f"[part2] Answer: {answer2}")
