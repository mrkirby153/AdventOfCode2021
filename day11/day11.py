with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

octopus_grid = [list(map(int, list(x))) for x in input_data]
print(octopus_grid)

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col if col < 10 else 'X', end="")
        print()
    print()

def get_octopi_to_flash(grid):
    """
    Returns a tuple of (x, y) coordinates of octopi that flash
    """
    coords = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] > 9:
                coords.append((x, y))
    return coords

def increment_power(grid):
    """Modifies the grid and increments the power level of all octopi
    """
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1

def increment_adjacent(grid, pos):
    x, y = pos
    for delta_x in range(-1, 2):
        for delta_y in range(-1, 2):
            new_x = x + delta_x
            new_y = y + delta_y
            
            if new_y >= 0 and new_y < len(grid) and new_x >= 0 and new_x < len(grid[new_y]):
                grid[new_y][new_x] += 1

def run_step(grid):
    increment_power(grid)
    to_flash = set(get_octopi_to_flash(grid))
    flashed_octopi = set()
    while len(to_flash) > 0:
        # print(f"Flashing {len(to_flash)}")
        for point in to_flash:
            if point in flashed_octopi:
                continue
            increment_adjacent(grid, point)
            flashed_octopi.add(point)
        to_flash = set(get_octopi_to_flash(grid)) - flashed_octopi
    # print(f"{len(flashed_octopi)} flashed this step")
    for x, y in flashed_octopi:
        grid[y][x] = 0
    return len(flashed_octopi)

def part_1():
    flash_count = 0
    for i in range(100):
        flash_count += run_step(octopus_grid)
    return flash_count

def part_2():
    for i in range(1, 5000):
        if run_step(octopus_grid) == 100:
            return i
    # Something probably has gone wrong
    assert "No synchronized flash in 5k steps"


print(f"Part 1: {part_1()}")
octopus_grid = [list(map(int, list(x))) for x in input_data] # Reset the octopus grid
print(f"Part 2: {part_2()}")
