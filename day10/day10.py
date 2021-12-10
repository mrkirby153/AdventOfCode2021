from enum import Enum
with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

class Symbol(Enum):
    PAREN = 1
    BRACKET = 2
    BRACE = 3
    ANGLE = 4

opening_blocks = {
    '(': Symbol.PAREN,
    '[': Symbol.BRACKET,
    '{': Symbol.BRACE,
    '<': Symbol.ANGLE
}

closing_blocks = {
    ')': Symbol.PAREN,
    ']': Symbol.BRACKET,
    '}': Symbol.BRACE,
    '>': Symbol.ANGLE
}

part_1_points = {
    Symbol.PAREN: 3,
    Symbol.BRACKET: 57,
    Symbol.BRACE: 1197,
    Symbol.ANGLE: 25137
}

def parse_line(line):
    blocks = []
    for char in line:
        if char in opening_blocks:
            blocks.append(opening_blocks[char])
        if char in closing_blocks:
            expected = blocks[-1]
            actual = closing_blocks[char]
            if len(blocks) < 0 or actual != expected:
                return [], actual
            else:
                if len(blocks) > 0:
                    blocks = blocks[:-1]
    return blocks[::-1], None

def part_1():
    score = 0
    for line in input_data:
        _, invalid_char = parse_line(line)
        if invalid_char is not None:
            score += part_1_points[invalid_char]
    return score
            
def part_2():
    scores = []
    for line in input_data:
        completion, invalid_char = parse_line(line)
        if invalid_char is None:
            line_score = 0
            for c in completion:
                line_score *= 5
                line_score += c.value
            scores.append(line_score)
    scores.sort()
    middle = len(scores) // 2
    return scores[middle]

print(input_data)
print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
