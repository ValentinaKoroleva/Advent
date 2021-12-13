import numpy as np
import copy as cp
f = open('input.txt')
# f = open('example.txt')
f_list = f.readlines()
dots = list()
x_dots = list()
y_dots = list()
instructions = list()
r = 0
while f_list[r].strip() != '':
    dots_pair = f_list[r].strip().split(',')
    dots_pair = list(map(int, dots_pair))
    dots.append(dots_pair)
    x_dots.append(dots_pair[0])
    y_dots.append(dots_pair[1])
    r += 1
r += 1
while r < len(f_list):
    instruction = f_list[r].strip()
    instruction = instruction.replace("fold along", "")
    instructions.append(instruction)
    r += 1
# print(instructions)
max_x = max(x_dots)
max_y = max(y_dots)
# print(max_x)
# print(max_y)
# x - col, y - row
paper_array = [['.'] * (max_x + 1) for _ in range(max_y + 1)]
paper = np.array(paper_array)
for pair in dots:
    x = pair[0]
    y = pair[1]
    paper[y][x] = '#'
# print(paper)


def fold(data, parameter):
    axis, value = parameter.split('=')
    axis = axis.strip()
    value = int(value)
    if axis == 'y':
        first = data[:value, :]
        second = data[value + 1:, :]
    else:
        first = data[:, :value]
        second = data[:, value + 1:]
    second_reverse = np.empty_like(second)
    if axis == 'y':
        for row in range(len(second_reverse)):
            second_reverse[row] = cp.deepcopy(second[len(second) - 1 - row])
    else:
        second_transposed = np.transpose(cp.deepcopy(second))
        second_reverse_transposed = np.empty_like(second_transposed)
        for row in range(len(second_transposed)):
            second_reverse_transposed[row] = cp.deepcopy(second_transposed[len(second_transposed) - 1 - row])
        second_reverse_transposed = np.transpose(second_reverse_transposed)
        second_reverse = second_reverse_transposed
    result = np.empty_like(second)
    for row in range(len(result)):
        row_result = np.empty_like(first[row])
        for col in range(len(row_result)):
            row_result[col] = '.'
            if first[row][col] == '#' or second_reverse[row][col] == '#':
                row_result[col] = '#'
        result[row] = row_result
    return result


def visible_dots(data):
    result = 0
    for row in data:
        for cell in row:
            if cell == '#':
                result = result + 1
    return result


# First Part
first_fold = fold(paper, instructions[0])
second_fold = fold(first_fold, instructions[1])
print(visible_dots(first_fold))
# Second Part
for task in instructions:
    paper = fold(paper, task)

code = open("output.txt", "w")
for line in paper:
    for cell in line:
        code.write(cell)
    code.write("\n")
code.close()
f.close()
