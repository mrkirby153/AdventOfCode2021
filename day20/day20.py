with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))


enhancement_algorithm = input_data[0]
image = []

for row in input_data[2:]:
    image.append([1 if x == '#' else 0 for x in row])

def print_image(img):
    for row in img:
        print(''.join(['#' if x == 1 else '.' for x in row]))

def get_enhancement_index(image, x, y, infinite_lit):
    binary_num = ""
    for offset_y in range(-1, 2):
        for offset_x in range(-1, 2):
            curr_x = x + offset_x
            curr_y = y + offset_y
            if curr_x < 0 or curr_x >= len(image[y]) or curr_y < 0 or curr_y >= len(image):
                binary_num += "0" if not infinite_lit else "1"
            else:
                binary_num += str(image[curr_y][curr_x])
    return int(binary_num, 2)

def enhance_image(image, infinite_lit):
    image = add_border(image, 3, infinite_lit)
    new_img = []
    for y in range(len(image)):
        new_row = []
        for x in range(len(image[y])):
            enhancement_index = get_enhancement_index(image, x, y, infinite_lit)
            new_row.append(1 if enhancement_algorithm[enhancement_index] == '#' else 0)
        new_img.append(new_row)
    return new_img

def remove_border(image, border_width):
    new_image = image[border_width:]
    for i, row in enumerate(new_image):
        new_image[i] = row[border_width:]
        new_image[i] = new_image[i][:-border_width]
    new_image = new_image[:-border_width]
    return new_image

def add_border(image, size, infinite_lit):
    new_width = len(image) + (size * 2)
    lit = 1 if infinite_lit else 0
    row = [lit for _ in range(size)]
    rows = [[lit for _ in range(new_width)] for _ in range(size)]
    new_img = []
    for r in image:
        new_img.append(row + r + row)
    return rows + new_img + rows

def serial_enhance(image, amount, should_print=False):
    img = image
    all_same_map = 1 if enhancement_algorithm[0] == '#' else 0
    all_same_map_enhanced = 1 if enhancement_algorithm[int(str(all_same_map) * 9, 2)] == '#' else 0
    print(f"All Same: {all_same_map}, Enhanced: {all_same_map_enhanced}")
    for i in range(amount):
        print(f"--- Iteration {i+1} ---")
        to_consider = all_same_map if i % 2 != 0 else all_same_map_enhanced
        print(f"To Consider: {to_consider}")
        img = enhance_image(img, True if to_consider == 1 else False)
        if should_print:
            print_image(img)
    return img

def part_1():
    new_img = serial_enhance(image, 2, True)
    lit_pixels = sum([sum(x) for x in new_img])
    return lit_pixels

def part_2():
    new_img = serial_enhance(image, 50)
    lit_pixels = sum([sum(x) for x in new_img])
    return lit_pixels


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
