
class Cave:

    def __init__(self, name, large) -> None:
        self.name = name
        self.connections = set()
        self.large = large
    
    def __repr__(self) -> str:
        return f"<{self.name}: {list(map(lambda x: x.name, self.connections))}>"


with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))


def parse_input(input_data):
    cave_map = {}
    for line in input_data:
        pt_1, pt_2 = line.split('-')
        print(f"{pt_1} connects to {pt_2}")
        cave_1 = cave_map.setdefault(pt_1, Cave(pt_1, pt_1.isupper()))
        cave_2 = cave_map.setdefault(pt_2, Cave(pt_2, pt_2.isupper()))
        cave_1.connections.add(cave_2)
        cave_2.connections.add(cave_1)
    return cave_map

def print_path(cave: list[Cave]):
    return ','.join(map(lambda x: x.name, cave))

def find_all_paths(current_node: Cave, end_node: Cave, acc: list[Cave], current_path: list[Cave] = None, visited_caves: set[Cave] = None):
    if visited_caves is None:
        visited_caves = set()
    if current_path is None:
        current_path = []

    p = current_path.copy()
    p.append(current_node)
    
    if current_node == end_node:
        acc.append(p)
        return
    for cave in current_node.connections:
        # We only want to visit the cave if it's a large cave, or if this is the first time through the small cave
        if cave not in visited_caves or cave.large:
            v = visited_caves.copy()
            v.add(current_node)
            find_all_paths(cave, end_node, acc, p, v)


def find_all_paths_pt2(current_node: Cave, end_node: Cave, acc: list[Cave], current_path: list[Cave] = None, depth: int = 0):
    if current_path is None:
        current_path = []

    p = current_path.copy()
    p.append(current_node)
    indent = '  ' * depth

    if current_node == end_node:
        acc.append(p)
        return
    for cave in current_node.connections:
        if cave.name == 'start':
            continue # we can't go back to the start
        # We only want to visit the cave if it's a large cave, or if this is the first time through the small cave
        if cave.large:
            find_all_paths_pt2(cave, end_node, acc, p, depth = depth + 1)
        else:
            if cave in current_path:
                # This is our 2nd time in the cave. Keep going if we've not been in another small cave twice already
                m = {}
                for c in current_path:
                    if not c.large:
                        m[c.name] = m.get(c.name, 0) + 1
                if 2 not in m.values():
                    find_all_paths_pt2(cave, end_node, acc, p, depth = depth + 1)
            else:
                # This is our first time in the cave
                find_all_paths_pt2(cave, end_node, acc, p, depth = depth + 1)

def part_1():
    cave_map = parse_input(input_data)
    start = cave_map['start']
    end = cave_map['end']
    found_paths = []
    find_all_paths(start, end, found_paths)
    return len(found_paths)


def part_2():
    cave_map = parse_input(input_data)
    start = cave_map['start']
    end = cave_map['end']
    found_paths = []
    print("Finding paths...")
    find_all_paths_pt2(start, end, found_paths)
    # find_all_paths_pt2 is broken so lets just sanity check the paths here
    print("Verifying paths...")
    valid_paths = []
    for p in found_paths:
        tmp_map = {}
        for c in p:
            if not c.large:
                tmp_map[c.name] = tmp_map.get(c.name, 0) + 1
        if list(tmp_map.values()).count(2) <= 1:
            valid_paths.append(p)
    return len(valid_paths)

print(input_data)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
