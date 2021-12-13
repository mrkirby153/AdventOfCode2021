with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

"""
Tuple of points
"""
points = []
"""
Tuple of axis and coordinate
"""
instructions = []

for line in input_data:
    if line.startswith('fold along'):
        axis, point = line.split(' ')[2].split('=')
        instructions.append((axis, int(point)))
    else:
        if line == "":
            continue
        x, y = line.split(',')
        points.append((int(x), int(y)))

print(f"Points: {points}")
print(f"Instructions: {instructions}")

def _get_grid_size(points):
    return (max([x for x, _ in points]), max([y for _, y in points]))

def render_grid(points, fold_x = None, fold_y = None, width = None, height = None):
    grid_str = ""
    max_x, max_y = _get_grid_size(points)
    if width is not None:
        max_x = width
    if height is not None:
        max_y = height
    for y in range(max_y+1):
        for x in range(max_x+1):
            if x == fold_x:
                grid_str += "|"
            elif y == fold_y:
                grid_str += "-"
            else:
                grid_str += '█' if (x, y) in points else ' '
        grid_str += "\n"
    return grid_str

def reflect_points(points, reflect_x = None, reflect_y = None):
    new_points = set()
    for x, y in points:
        new_x = x
        new_y = y
        if reflect_x is not None:
            if x > reflect_x:
                distance_from_x = x - reflect_x
                new_x = reflect_x - distance_from_x
        if reflect_y is not None:
            if y > reflect_y:
                distance_from_y = y - reflect_y
                new_y = reflect_y - distance_from_y
        new_points.add((new_x, new_y))
    return new_points

def do_fold(pts, ins):
    grid = pts
    for instruction in ins:
        axis, point = instruction
        to_pass = {}
        if axis == 'y':
            to_pass['reflect_y'] = point
        if axis == 'x':
            to_pass['reflect_x'] = point

        grid = reflect_points(grid, **to_pass)
    return grid

def part_1():    
    return len(do_fold(points, [instructions[0]]))


def part_2():
    grid = do_fold(points, instructions)
    return '\n' + render_grid(grid)


# print(input_data)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
