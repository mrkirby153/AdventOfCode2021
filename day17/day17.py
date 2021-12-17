import re

with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

min_x, max_x, min_y, max_y = map(int, re.findall(r'-?\d+', input_data[0]))


def simulate(initial_vel_x, initial_vel_y, target_min_x, target_max_x, target_min_y, target_max_y):
    vel_x = initial_vel_x
    neg_x = initial_vel_x < 0
    vel_y = initial_vel_y
    x, y = 0, 0
    step_points = []
    step_points.append((x, y))
    while True:
        x += vel_x
        y += vel_y
        step_points.append((x, y))
        vel_x = max(vel_x - 1, 0) if not neg_x else min(vel_x + 1, 0)
        vel_y -= 1
        if target_min_x <= x and x <= target_max_x and target_min_y <= y and y <= target_max_y:
            return True, step_points
        # Check if the point is past the target (i.e. < than the min_y and >
        # than the max_x)
        if x > max_x or y < min_y:
            return False, []

def part_1():
    # This is 100% a calculus problem but i forget calculus so bruteforce go
    # brrr
    successful_points = {}
    for x in range(300):
        for y in range(300):
            success, steps = simulate(x, y, min_x, max_x, min_y, max_y)
            if success:
                successful_points[(x, y)] = steps
    # return successful_points
    m = None
    for steps in successful_points.values():
        step_max_y = max(map(lambda x: x[1], steps))
        if m is None or step_max_y > m:
            m = step_max_y
    return m


def part_2():
    count = 0
    # Bruteforce go brrr again, just keep changing these until the output stops
    # changing. Using a reasonable guess of x can never be more than the max_x
    # of the target, and y can never be less than the min_x of the target, and a
    # random very high y value
    for x in range(400):
        for y in range(-100, 300):
            success = simulate(x, y, min_x, max_x, min_y, max_y)[0]
            count += 1 if success else 0
    return count

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
