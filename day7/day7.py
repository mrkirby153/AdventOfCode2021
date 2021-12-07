with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

crab_positions = list(map(int, input_data[0].split(',')))

def calculate_fuel_cost(target, crabs):
    total_cost = 0
    for crab in crabs:
        total_cost += abs(crab - target)
    return total_cost

def calculate_part_2_cost(target, crabs):
    total_cost = 0
    for crab in crabs:
        total_cost += sum(range(1, abs(crab - target) + 1))
    return total_cost

def part_1():
    position = None
    fuel_cost = None
    for i in range(0, max(crab_positions)):
        if fuel_cost is None or calculate_fuel_cost(i, crab_positions) < fuel_cost:
            position = i
            fuel_cost = calculate_fuel_cost(i, crab_positions)
    return position, fuel_cost

def part_2():
    position = None
    fuel_cost = None
    for i in range(0, max(crab_positions)):
        if fuel_cost is None or calculate_part_2_cost(i, crab_positions) < fuel_cost:
            position = i
            fuel_cost = calculate_part_2_cost(i, crab_positions)
    return position, fuel_cost


print(input_data)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
