from os import curdir


with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

ENERGY_COST = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

class Amphipod:

    def __init__(self, type):
        self.type = type

    def __repr__(self) -> str:
        return f"{self.type}"


def print_state(room_a, room_b, room_c, room_d, hallway):
    print("#############")
    print(f"#{''.join(['.' if x is None else x for x in hallway])}#")
    print(f"###{room_a[0]}#{room_b[0]}#{room_c[0]}#{room_d[0]}###")
    print(f"  #{room_a[1]}#{room_b[1]}#{room_c[1]}#{room_d[1]}#")
    print("  #########")

def get_index(object, arr):
    for i, a in enumerate(arr):
        if a == object:
            return i
    return -1

def is_solved(room_a, room_b, room_c, room_d):
    for pod in room_a:
        if pod.type != 'a' or pod is None:
            return False
    for pod in room_b:
        if pod.type != 'b' or pod is None:
            return False
    for pod in room_c:
        if pod.type != 'c' or pod is None:
            return False
    for pod in room_d:
        if pod.type != 'd' or pod is None:
            return False

def get_possible_moves(pod, room_a, room_b, room_c, room_d, hallway):
    if is_solved(room_a, room_b, room_c, room_d):
        return [] # Room is solved, no possible moves
    curr_pos = None
    lookup_map = {
        "hallway": hallway,
        "room_a": room_a,
        "room_b": room_b,
        "room_c": room_c,
        "room_d": room_d
    }

    moves = []

    for k, v in lookup_map.items():
        if pod in v:
            curr_pos = (k, get_index(pod, v))
    
    if curr_pos is None:
        return []
    
    loc, idx = curr_pos
    if loc == "hallway":
        # If the pod is in the hallway, its only possible moves are into its room
        dest_room = f"room_{pod.type}"
        room_arr = lookup_map[dest_room]
        for i, v in enumerate(room_arr):
            pass

def part_1():
    room_a = []
    room_b = []
    room_c = []
    room_d = []
    hallway = [None for _ in range(11)]

    for row in input_data[2:4]:
        a, b, c, d = row[3:10].split("#")
        room_a.append(Amphipod(a))
        room_b.append(Amphipod(b))
        room_c.append(Amphipod(c))
        room_d.append(Amphipod(d))
    
    print_state(room_a, room_b, room_c, room_d, hallway)

def part_2():
    pass

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
