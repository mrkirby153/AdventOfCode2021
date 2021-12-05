from typing import overload


with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

# List tuples of (x1, y1, x2, y2)
parsed_lines = []

for line in input_data:
    pts = line.split('->')
    pt1 = pts[0].split(',')
    pt2 = pts[1].split(',')
    parsed_lines.append((int(pt1[0]), int(pt1[1]), int(pt2[0]), int(pt2[1])))

size_x = 0
size_y = 0

for line in parsed_lines:
    if line[0] > size_x:
        size_x = line[0]
    if line[1] > size_y:
        size_y = line[1]
    if line[2] > size_x:
        size_x = line[2]
    if line[3] > size_y:
        size_y = line[3]

print(f"Board is {size_x}x{size_y}")

board = [[0 for _ in range(size_x+1)] for _ in range(size_y+1)]


def print_board(board):
    for row in board:
        for col in row:
            print('.' if col == 0 else str(col), end='')
        print()

def get_overlap_count(board):
    overlap_count = 0
    for row in board:
        for col in row:
            if col > 1:
                overlap_count += 1
    return overlap_count

def part_1():
    # Only consider lines that are horizontal or vertical
    filter_function = lambda line: line[0] == line[2] or line[1] == line[3]
    for line in filter(filter_function, parsed_lines):
        print(f"Plotting {line}")
        min_x = min(line[0], line[2])
        max_x = max(line[0], line[2])
        min_y = min(line[1], line[3])
        max_y = max(line[1], line[3])
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                board[y][x] += 1
    # print_board(board)
    return get_overlap_count(board)
                
def part_2():
    # Plot the other lines on top of our existing board
    def filter_function(line): return line[0] != line[2] and line[1] != line[3]

    for line in filter(filter_function, parsed_lines):
        print(f"Plotting {line}")
        start_point = (line[0], line[1])
        end_point = (line[2], line[3])
        x = start_point[0]
        y = start_point[1]
        delta_x = 1 if start_point[0] < end_point[0] else -1
        delta_y = 1 if start_point[1] < end_point[1] else -1
        while (x, y) != end_point:
            board[y][x] += 1
            x += delta_x
            y += delta_y
        # Plot the last point cos the loop above misses it
        board[y][x] += 1
    return get_overlap_count(board)


print(parsed_lines)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
