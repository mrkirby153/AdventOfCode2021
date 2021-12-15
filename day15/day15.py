from queue import PriorityQueue

with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

class Node:

    def __init__(self, position, cost):
        self.position = position
        self.cost = cost # Node cost
        self.total_cost = 0
    
    def __eq__(self, other) -> bool:
        return self.position == other.position
    
    def __lt__(self, other):
        return self.total_cost < other.total_cost
    
    def __repr__(self) -> str:
        return f"{self.position}: {self.cost}"

# grid = [list(map(int, x)) for x in input_data for y in x]
grid = []

for y in range(len(input_data)):
    row = []
    for x in range(len(input_data[y])):
        row.append(Node((x, y), int(input_data[y][x])))
    grid.append(row)


def find_neighbors(pos, grid):
    neighbors = []
    x, y = pos

    if y + 1 < len(grid):
        neighbors.append(grid[y+1][x])
    if y - 1 >= 0:
        neighbors.append(grid[y-1][x])
    
    if x + 1 < len(grid[y]):
        neighbors.append(grid[y][x+1])
    
    if x - 1 >= 0:
        neighbors.append(grid[y][x-1])
    return neighbors

def find_path(grid, start, end):
    open_set = PriorityQueue()
    came_from = dict()
    cumulitive_cost = dict()

    came_from[start.position] = None
    cumulitive_cost[start.position] = start.cost
    open_set.put(start, start.cost)
    
    while not open_set.empty():
        current = open_set.get()

        if current == end:
            trace = []
            pos = end.position
            while came_from.get(pos, None) is not None:
                trace.append(pos)
                pos = came_from.get(pos).position
            return trace[::-1]

        for next in find_neighbors(current.position, grid):
            new_cost = cumulitive_cost[current.position] + next.cost
            if next.position not in cumulitive_cost or new_cost < cumulitive_cost[next.position]:
                next.total_cost = new_cost
                cumulitive_cost[next.position] = new_cost
                open_set.put(next, new_cost)
                came_from[next.position] = current

def print_board(grid, marked_squares=[]):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            color = '\033[92m' if (x, y) in marked_squares else '\033[91m'
            print(f"{color}{grid[y][x].cost}", end=" ")
        print()
    print('\033[0m') # Reset color

def part_1():
    start_node = grid[0][0]
    end_node = grid[len(grid)-1][len(grid)-1]
    print(f"Calculating cost from {start_node} to {end_node}")
    trace = find_path(grid, start_node, end_node)
    
    return sum(map(lambda x: grid[x[1]][x[0]].cost, trace))


risk_map = [[0,1,2,3,4],
            [1,2,3,4,5],
            [2,3,4,5,6],
            [3,4,5,6,7],
            [4,5,6,7,8]]

def part_2():
    # Lets make the grid _very_ big
    new_grid = []
    new_height = len(grid) * 5
    new_width = len(grid) * 5
    print(f"Tiling board to {new_width} {new_height}")
    for y in range(new_height):
        row = []
        for x in range(new_width):
            mapped_x = x % len(grid)
            mapped_y = y % len(grid)
            modifier_y = y // len(grid)
            modifier_x = x // len(grid)
            modifier = risk_map[modifier_y][modifier_x]
            cost = grid[mapped_y][mapped_x].cost
            modified_cost = modifier + cost
            while modified_cost > 9:
                modified_cost -= 9
            row.append(Node((x, y), modified_cost))
        new_grid.append(row)
    print(f"Tiled board")
    start_node = new_grid[0][0]
    end_node = new_grid[len(new_grid)-1][len(new_grid)-1]
    print(f"Calculating cost from {start_node} to {end_node}")
    trace = find_path(new_grid, start_node, end_node)
    
    return sum(map(lambda x: new_grid[x[1]][x[0]].cost, trace))

#print(grid)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
