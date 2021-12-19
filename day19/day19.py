# There becomes a time to admit defeat, and this is it.
# Most of this code is https://github.com/dankoo97/AoC_2021/blob/06936b9707cdae0f2d88c46f2fda1899b6af1a07/BeaconScanner.py
import re
import itertools
from collections import Counter, defaultdict

SCANNER_HEADER_RE = re.compile(r"--- scanner (\d+) ---")

with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

def orientation():
    """Yields each of 8 possible orientations"""
    for i in range(8):
        yield (-1) ** (i % 2), (-1) ** ((i // 2) % 2), (-1) ** ((i // 4) % 2)

class Scanner:
    def __init__(self, id, beacon_points=None, pos=None) -> None:
        self.id = id
        self.beacon_points = set() if beacon_points is None else beacon_points
        self.pos = pos
    
    def __repr__(self) -> str:
        points = "\n".join(map(lambda p: ','.join(map(str, p)), self.beacon_points))
        return f"--- Scanner {self.id} ---\n{points}"
    
    def compare_and_reorient(self, other):
        c = dict()
        for orient in orientation():
            for perm in itertools.permutations((0, 1, 2)):
                c[orient,perm] = defaultdict(int)

                for our_beacons in self.beacon_points:
                    for their_beacons in other.beacon_points:
                        stuff = tuple(da+o*their_beacons[dp] for da, o, dp in zip(our_beacons, orient, perm))
                        c[orient,perm][stuff] += 1
                for k, v in c[orient,perm].items():
                    if v >= 12:
                        other.pos = k

                        other.reorient(orient, perm)
                        return other.pos
    
    def reorient(self, orient, perm):
        new_s = set()
        for b in self.beacon_points:
            new_b = tuple(self.pos[order] - o*b[p] for o, p, order in zip(orient, perm, (0, 1, 2)))
            new_s.add(new_b)
        self.beacon_points = new_s

scanner_data = []

curr_scanner = None
for line in input_data:
    if line == "":
        continue
    header_match = SCANNER_HEADER_RE.match(line)
    if header_match is not None:
        scanner_id = header_match.group(1)
        if curr_scanner is not None:
            scanner_data.append(curr_scanner)
        curr_scanner = Scanner(scanner_id)
    else:
        x, y, z = line.split(',')
        curr_scanner.beacon_points.add((int(x), int(y), int(z)))
scanner_data.append(curr_scanner)

def reorient_all_beacons(beacons):
    # Assume beacon 0 is the origin
    known = {0}
    beacons[0].pos = (0, 0, 0)

    while set(range(len(beacons))) - known != set():
        new = set()
        for k in known:
            for i in range(len(beacons)):
                if i in known:
                    continue
                if beacons[k].compare_and_reorient(beacons[i]):
                    new.add(i)
        known |= new
        print(f"Total Mapped: {len(known)}/{len(beacons)}")


reorient_all_beacons(scanner_data)

def part_1():
    beacons = set.union(*(scan.beacon_points for scan in scanner_data))
    return len(beacons)

def manhattan_distance(scanner_1, scanner_2):
    x1, y1, z1 = scanner_1.pos
    x2, y2, z2 = scanner_2.pos
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

def part_2():
    largest = 0
    largest_pair = None
    for scanner_1, scanner_2 in itertools.combinations(scanner_data, 2):
        md = manhattan_distance(scanner_1, scanner_2)
        if md > largest:
            largest = md
            largest_pair = (scanner_1, scanner_2)
    p1, p2 = largest_pair
    return f"{largest} (Between {p1.id} ({p1.pos}) and {p2.id} ({p2.pos})"



print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
