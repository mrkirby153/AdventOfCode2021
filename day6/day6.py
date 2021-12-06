with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

fishies = list(map(int, input_data[0].split(',')))

fish_map = {}

for days_left in fishies:
    count = fish_map.setdefault(days_left, 0)
    count += 1
    fish_map[days_left] = count

print(fish_map)

def process_optimized_day(fishies):
    new_map = {}
    for (days, count) in fishies.items():
        if days == 0:
            # Make new fishes
            new_map[8] = new_map.get(8, 0) + count
            # Reset the fishes to 6
            new_map[6] = new_map.get(6, 0) + count
            continue
        new_map[days - 1] = new_map.get(days - 1, 0) + count
    return new_map

def process_day():
    new_fishies = []
    for i in range(len(fishies)):
        fish = fishies[i]
        if fish == 0:
            new_fishies.append(8)
            fishies[i] = 6
        else:
            fishies[i] -= 1
    fishies.extend(new_fishies)

def part_1():
    new_map = fish_map.copy()
    for i in range(0, 80):
        print(f"processing day {i}")
        new_map = process_optimized_day(new_map)
    fish_count = 0
    for count in new_map.values():
        fish_count += count
    return fish_count
    # Initial brute-force solution kept for posterity
    # for i in range(0, 80):
    #     process_day()
    # return len(fishies)


def part_2():
    new_map = fish_map.copy()
    for i in range(0, 256):
        print(f"processing day {i}")
        new_map = process_optimized_day(new_map)
    fish_count = 0
    for count in new_map.values():
        fish_count += count
    return fish_count


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
