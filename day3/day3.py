with open('input.txt', ) as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

bits_per_line = len(input_data[0])

def check_most_common(input, position):
    """
    Returns 1 if 1 is the most common, 0 if 0 is the most common. if there is a tie, it returns -1
    """
    count = 0
    for input_line in input:
        if input_line[position] == '1':
            count += 1
        elif input_line[position] == '0':
            count -= 1
        else:
            raise Exception('Invalid input')
    # print(input)
    # print("Count: " + str(count))
    if count == 0:
        return -1
    return 1 if count > 0 else 0

def invert_binary_string(string):
    return ''.join(map(lambda x: '1' if x == '0' else '0', string))

def part_1():
    gamma_raw_binary = ""
    for i in range(bits_per_line):
        gamma_raw_binary += str(check_most_common(input_data, i))
    gamma = int(gamma_raw_binary, 2)
    print(gamma)
    epsilon = int(invert_binary_string(gamma_raw_binary), 2)
    print(epsilon)
    return gamma * epsilon

def calculate_part_2(keep_most_common):
    kept_numbers = input_data[:]
    bit_pos = 0
    while len(kept_numbers) > 1 and bit_pos < bits_per_line:
        most_common = check_most_common(kept_numbers, bit_pos)
        # print(f"Most common: {most_common}")
        if most_common == -1:
            most_common = 1 if keep_most_common else 0
        else:
            most_common = most_common if keep_most_common else 0 if most_common == 1 else 1
        new_list = []
        for i in range(len(kept_numbers)):
            if kept_numbers[i][bit_pos] == str(most_common):
                # print(f"Keeping {kept_numbers[i]}")
                new_list.append(kept_numbers[i])
        kept_numbers = new_list
        bit_pos += 1
    return int(kept_numbers[0], 2)

def part_2():
    o2 = calculate_part_2(True)
    co2 = calculate_part_2(False)
    return o2 * co2

print(input_data)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
