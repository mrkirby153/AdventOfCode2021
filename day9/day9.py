import heapq

with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

parsed_data = [list(map(int, list(x))) for x in input_data]

def get_low_points():
    low_points = []
    low_coords = []
    for y in range(len(parsed_data)):
        for x in range(len(parsed_data[y])):
            # Check bounds
            point = parsed_data[y][x]
            marked = []
            # Check all directions
            lowest = True
            if y + 1 < len(parsed_data):
                marked.append((x, y+1))
                if parsed_data[y+1][x] <= point:
                    lowest = False
            if y - 1 >= 0:
                marked.append((x, y-1))
                if parsed_data[y-1][x] <= point:
                    lowest = False
            if x + 1 < len(parsed_data[y]):
                marked.append((x+1, y))
                if parsed_data[y][x+1] <= point:
                    lowest = False
            if x - 1 >= 0:
                marked.append((x-1, y))
                if parsed_data[y][x-1] <= point:
                    lowest = False
            if lowest:
                low_points.append(point)
                low_coords.append((x, y))
    return low_points, low_coords


def part_1():
    low_points, _ = get_low_points()
    return sum(map(lambda x: x+1, low_points))


def find_basin_points(pos, acc = None, used_points = None):
    """
    Recursively find all points in the basin.
    Get the number of each point, and for each up, down, left, and right points, check if it's not 9, then recursively check those
    """
    x, y = pos
    if acc is None:
        acc = set()
    if used_points is None:
        used_points = set()
    point = parsed_data[y][x]
    if point == 9 or (x, y) in used_points:
        return acc # We're at the top or we've already counted this point
    used_points.add((x, y))
    acc.add((x, y))
    if y + 1 < len(parsed_data):
        acc.update(find_basin_points((x, y+1), acc, used_points))
    if y - 1 >= 0:
        acc.update(find_basin_points((x, y-1), acc, used_points))
    if x + 1 < len(parsed_data[y]):
        acc.update(find_basin_points((x+1, y), acc, used_points))
    if x - 1 >= 0:
        acc.update(find_basin_points((x-1, y), acc, used_points))
    return acc


def part_2():
    _, low_coords = get_low_points()

    basin_sizes = []
    for point in low_coords:
        basin_sizes.append(len(find_basin_points(point)))
    heapq._heapify_max(basin_sizes)
    top_3 = [heapq._heappop_max(basin_sizes) for _ in range(0, 3)]
    return top_3[0] * top_3[1] * top_3[2]




# print(parsed_data)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
