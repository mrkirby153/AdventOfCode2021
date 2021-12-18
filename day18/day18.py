from itertools import combinations
with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))

def convert(ln):
    return [int(s) if s.isdigit() else s for s in ln.rstrip()]

def display(snail):
    return ''.join(map(str, snail))

def add(num_1, num_2):
    num_1 = display(num_1)
    num_2 = display(num_2)
    return convert(f"[{num_1},{num_2}]")

def explode(str, index):
    # print(f"Exploding {str} at {index}")
    left = str[index+1]
    right = str[index+3]
     #print(f"L: {left}, R: {right}")

    # Go backwards
    for i in range(index-1, -1, -1):
        if isinstance(str[i], int):
            # print(f"Adding {left} to {str[i]}")
            str[i] += left
            break
    
    # Go forwards
    for i in range(index+5, len(str)):
        if isinstance(str[i], int):
            # print(f"Adding {right} to {str[i]}")
            str[i] += right
            break
    return str[:index] + [0] + str[index+5:]

def split(str, index):
    # print(f"Splitting {display(str)} at {index}")
    num = str[index]
    # print(f"NUM: {num}")
    return str[:index] + ['[', (num) // 2, ',', (num+1) // 2, ']'] + str[index+1:]

def run(snail):
    # print(f"-- Running {display(snail)} --")
    changed = True
    while changed:
        changed = False
        depth = 0
        for index, char in enumerate(snail):
            if char == '[':
                depth += 1
                if depth == 5:
                    snail = explode(snail, index)
                    changed = True
                    break
            elif char == ']':
                depth -= 1
        if changed:
            continue
        # print(f"After exploding: {display(snail)}")
        
        for index, char in enumerate(snail):
            if isinstance(char, int) and char >= 10:
                snail = split(snail, index)
                changed = True
                break
    return snail

def add_many(snailfish):
    snail = snailfish[0]
    for i in range(1, len(snailfish)):
        snail = add(snail, snailfish[i])
        snail = run(snail)
    return snail

def get_magnitude(snailfish):
    while len(snailfish) > 1:
        # print(display(snailfish))
        for index, char in enumerate(snailfish):
            if isinstance(char, int):
                # Check if this is a part of a pair
                if isinstance(snailfish[index+2], int):
                    left = char
                    right = snailfish[index+2]
                    magnitude = (3 * left) + (2 * right)
                    snailfish = snailfish[:index-1] + [magnitude] + snailfish[index+4:]
                    break
    return snailfish[0]

def part_1():
    final_sum = add_many(list(map(convert, input_data)))
    return get_magnitude(final_sum)

def part_2():
    max_mag = 0
    # Brute force go brrrr, get all combinations of any two number
    for one, two in combinations(list(map(convert, input_data)), 2):
        m = get_magnitude(add_many([one, two]))
        if  m > max_mag:
            max_mag = m
    return max_mag

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
