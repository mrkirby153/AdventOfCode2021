import re
import itertools

START_POS_PATTERN = re.compile(": (\d+)")

with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

p1_start = int(START_POS_PATTERN.search(input_data[0]).group(1))
p2_start = int(START_POS_PATTERN.search(input_data[1]).group(1))

print(f"p1: {p1_start}, p2 {p2_start}")

def get_board_score(space):
    while space > 10:
        space -= 10
    return space

DIE_CYCLE = itertools.cycle(range(1, 101))

def get_next_3(die):
    a = [next(die) for _ in range(3)]
    return sum(a)

def recursive_game(p1_pos, p2_pos, p1_score, p2_score, die_roll_count, die):
    p1_move = get_next_3(die)
    p1_new_pos = p1_move + p1_pos
    p1_new_score = p1_score + get_board_score(p1_new_pos)
    if p1_new_score >= 1000:
        return p1_new_score, p2_score, die_roll_count + 3
    p2_move = get_next_3(die)
    p2_new_pos = p2_move + p2_pos
    p2_new_score = p2_score + get_board_score(p2_new_pos)
    if p2_new_score >= 1000:
        return p1_score, p2_new_score, die_roll_count
    return recursive_game(p1_new_pos, p2_new_pos, p1_new_score, p2_new_score, die_roll_count + 6, die)

def part_1():
    p1_score, p2_score, die_count = recursive_game(p1_start, p2_start, 0, 0, 0, DIE_CYCLE)
    return min(p1_score, p2_score) * die_count


def part_2():
    pass

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
