import itertools

with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

parsed_data = []
for line in input_data:
    input_raw, output_raw = line.split('|')
    parsed_data.append((input_raw.strip().split(' '), output_raw.strip().split(' ')))


# Map the numbers to their segments
segment_map = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

def part_1():
    # 1 uses 2 segments, 4 uses 4 segments, 7 uses 3 segments, 8 uses 7 segments
    count = 0
    for _, out_data in parsed_data:
        count += len(list(filter(lambda x: len(x) in [2, 3, 4, 7], out_data)))
    return count

def translate(str, mapping):
    return ''.join(sorted(mapping[x] for x in str))


def decode(patterns, output):
    # Yolo brute force it
    for perm in itertools.permutations('abcdefg'):
        mapping = {x: y for x, y in zip(perm, 'abcdefg')}
        translated_patterns = map(lambda x: translate(x, mapping), patterns)
        if all((x in segment_map) for x in translated_patterns):
            # We got a valid match
            output = [segment_map[translate(x, mapping)] for x in output]
            return int(''.join(map(str, output)))
    raise Exception(f'Pattern not decoded: {patterns}')

def part_2():
    sum = 0
    for input, output in parsed_data:
        sum += decode(input, output)
    return sum

# print(input_data)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
