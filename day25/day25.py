with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

grid = []
# Store a list of locations of both herds for faster lookups (Dunno if this is really neccecary)
east_herd_points = []
south_herd_points = []

for row in input_data:
    grid_row = []
    for col in row:
        grid_row.append(col if col != '.' else None)
    grid.append(grid_row)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        value = grid[y][x]
        if value == 'v':
            south_herd_points.append((x, y))
        if value == '>':
            east_herd_points.append((x, y))

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col if col is not None else '.', end="")
        print()

def do_step(grid, herd_to_consider, delta):
    dX, dY = delta

    to_move = []
    new_locations = []
    for cucumber in herd_to_consider:
        x, y = cucumber
        new_x = (x + dX) % len(grid[y])
        new_y = (y + dY) % len(grid)
        if grid[new_y][new_x] is None:
            to_move.append((x, y))
        else:
            # This cucuber didn't move
            new_locations.append((x, y))

    for point in to_move:
        x, y  = point
        new_x = (x + dX) % len(grid[y])
        new_y = (y + dY) % len(grid)
        old = grid[y][x]
        grid[y][x] = None
        grid[new_y][new_x] = old
        new_locations.append((new_x, new_y))
    
    return new_locations, len(to_move)

def run(grid, east_herd, south_herd):
    new_grid = grid.copy()
    new_east, moved_east = do_step(grid, east_herd, (1, 0))
    new_south, moved_south = do_step(grid, south_herd, (0, 1))
    return (new_grid, new_east, new_south, (moved_east + moved_south))

def run_until_deadlock(grid, east, south, debug=False):
    def sprint(*args, **kwargs):
        if debug:
            print(*args, **kwargs)
    moved = 1
    step = 0
    while moved > 0:
        step += 1
        sprint(f"--- Step {step} ---")
        grid, east, south, moved = run(grid, east, south)
        sprint(f"{moved} cucumbers moved")
        if debug:
            print_grid(grid)
    return step

def part_1():
    print_grid(grid)
    return run_until_deadlock(grid, east_herd_points, south_herd_points)

print(f"Part 1: {part_1()}")
