import re
import itertools
import functools
import dataclasses
from collections import Counter

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

@dataclasses.dataclass(frozen=True)
class Player:
    position: int
    score: int = 0
    
    def move(self, amount):
        pos = self.position + amount
        pos = (pos % 10) + 10 * (pos % 10 == 0)
        score = self.score + pos
        return Player(pos, score=score)

# Cache the function results to make it go significantly faster
@functools.cache
def quantum_wins(player_1, player_2, current_player):
    win_counts = Counter()

    for rolls in itertools.product([1, 2, 3], repeat=3):
        roll = sum(rolls)

        player_lookup = {1: player_1, 2: player_2}
        player = player_lookup[current_player].move(roll)
        player_lookup[current_player] = player # move is immutable, so we want to re-assign our lookup map

        if player.score >= 21:
            win_counts[current_player] += 1
        else:
            next_player = 2 if current_player == 1 else 1
            win_counts.update(quantum_wins(player_lookup[1], player_lookup[2], next_player))

    return win_counts
    

def part_1():
    p1_score, p2_score, die_count = recursive_game(p1_start, p2_start, 0, 0, 0, DIE_CYCLE)
    return min(p1_score, p2_score) * die_count

def part_2():
    return quantum_wins(Player(p1_start), Player(p2_start), 1).most_common(1)[0][1]

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
