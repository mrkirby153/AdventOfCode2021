from os import remove


with open('input.txt') as f:
    input_data = list(map(lambda x: x.replace('\n', ''), f.readlines()))


enhancement_algorithm = input_data[0]
image = []

for row in input_data[2:]:
    image.append([1 if x == '#' else 0 for x in row])

# Give a black border of 5
BORDER_SIZE = 5

img_width = len(image[0]) + (BORDER_SIZE * 2)
bigger_image = []
for _ in range(BORDER_SIZE):
    bigger_image.append([0 for _ in range(img_width)])

for row in image:
    bigger_image.append([0 for _ in range(BORDER_SIZE)] + row + [0 for _ in range(BORDER_SIZE)])

for _ in range(BORDER_SIZE):
    bigger_image.append([0 for _ in range(img_width)])


def print_image(img):
    for row in img:
        print(''.join(['#' if x == 1 else '.' for x in row]))

# print_image(image)
# print("----")
# print_image(bigger_image)


def get_enhancement_index(image, x, y):
    binary_num = ""
    for offset_y in range(-1, 2):
        for offset_x in range(-1, 2):
            curr_x = x + offset_x
            curr_y = y + offset_y
            if curr_x < 0 or curr_x >= len(image[y]) or curr_y < 0 or curr_y >= len(image):
                binary_num += "0"
            else:
                binary_num += str(image[curr_y][curr_x])
    return int(binary_num, 2)

def enhance_image(image):
    new_img = []
    for y in range(len(image)):
        new_row = []
        for x in range(len(image[y])):
            enhancement_index = get_enhancement_index(image, x, y)
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

def part_1():
    # print_image(bigger_image)
    # print("---")
    # print_image(remove_border(bigger_image, BORDER_SIZE))
    new_img = enhance_image(bigger_image)
    new_img = enhance_image(new_img)
    print_image(new_img)

    # Remove the first and last rows, as well as the first and last columns of every image, cos there's garbage in there
    new_img = new_img[1:]
    new_img = new_img[:-1]
    for i, row in enumerate(new_img):
        new_img[i] = row[1:]
        new_img[i] = new_img[i][:-1]

    # new_img = remove_border(new_img, BORDER_SIZE)
    print("new image: ")
    print_image(new_img)


    lit_pixels = sum([sum(x) for x in new_img])
    return lit_pixels

def part_2():
    pass

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
