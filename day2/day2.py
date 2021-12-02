with open('input.txt', ) as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

def part_1():
    horiz = 0
    vert = 0
    for line in input_data:
        command, amount = line.split(' ')
        if command == 'forward':
            horiz += int(amount)
        elif command == 'down':
            vert += int(amount)
        elif command == 'up':
            vert -= int(amount)
    return horiz * vert

def part_2():
    horiz = 0
    vert = 0
    aim = 0
    for line in input_data:
        command, amount = line.split(' ')
        if command == 'down':
            aim += int(amount)
        elif command == 'up':
            aim -= int(amount)
        elif command == 'forward':
            horiz += int(amount)
            vert += aim * int(amount)
    return horiz * vert

print(input_data)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
