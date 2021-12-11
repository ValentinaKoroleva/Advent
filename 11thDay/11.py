import numpy as np
f = open('input.txt')
# f = open('example.txt')
# f = open('simpler_example.txt')
f_list = f.readlines()
n_octopuses = len(f_list)
octopuses = np.array([[0] * n_octopuses for _ in range(n_octopuses)])
for r in range(n_octopuses):
    rang = list(map(int, list(f_list[r].strip())))
    for c in range(n_octopuses):
        octopuses[r][c] = rang[c]
# print(octopuses)


def one_step(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] >= 9:
                matrix = first_wave(matrix, i, j)
    ones = [[1]*len(matrix) for _ in range(len(matrix))]
    # print(np.array(matrix) + np.array(ones))
    matrix = matrix + np.array(ones)
    return matrix


def first_wave(matrix, row, col):
    if row - 1 in range(len(matrix)):
        matrix[row - 1][col] += 1
        if col - 1 in range(len(matrix)):
            matrix[row - 1][col - 1] += 1
        if col + 1 in range(len(matrix)):
            matrix[row - 1][col + 1] += 1
    if row + 1 in range(len(matrix)):
        matrix[row + 1][col] += 1
        if col - 1 in range(len(matrix)):
            matrix[row + 1][col - 1] += 1
        if col + 1 in range(len(matrix)):
            matrix[row + 1][col + 1] += 1
    if col - 1 in range(len(matrix)):
        matrix[row][col - 1] += 1
    if col + 1 in range(len(matrix)):
        matrix[row][col + 1] += 1
    matrix[row][col] = -10
    return matrix


def second_wave(matrix, row, col):
    if row - 1 in range(len(matrix)):
        if matrix[row - 1][col] > 0:
            matrix[row - 1][col] += 1
        if col - 1 in range(len(matrix)) and matrix[row - 1][col - 1] > 0:
            matrix[row - 1][col - 1] += 1
        if col + 1 in range(len(matrix)) and matrix[row - 1][col + 1] > 0:
            matrix[row - 1][col + 1] += 1
    if row + 1 in range(len(matrix)):
        if matrix[row + 1][col] > 0:
            matrix[row + 1][col] += 1
        if col - 1 in range(len(matrix)) and matrix[row + 1][col - 1] > 0:
            matrix[row + 1][col - 1] += 1
        if col + 1 in range(len(matrix)) and matrix[row + 1][col + 1] > 0:
            matrix[row + 1][col + 1] += 1
    if col - 1 in range(len(matrix)) and matrix[row][col - 1] > 0:
        matrix[row][col - 1] += 1
    if col + 1 in range(len(matrix)) and matrix[row][col + 1] > 0:
        matrix[row][col + 1] += 1
    matrix[row][col] = -10
    return matrix


def clearing(matrix):
    for i in range(n_octopuses):
        for j in range(n_octopuses):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            elif matrix[i][j] > 9:
                matrix = second_wave(matrix, i, j)
                # matrix[i][j] = 0
    return matrix


def has_second_wave(matrix):
    for row in matrix:
        for cell in row:
            if cell not in range(n_octopuses):
                return True
    return False


def several_steps(m, steps):
    total_flashes = 0
    for s in range(steps):
        m = one_step(m)
        while has_second_wave(m):
            m = clearing(m)
        total_flashes = total_flashes + number_of_flashes(m)
    return m, total_flashes


def number_of_flashes(matrix):
    n_flashes = 0
    for i in range(n_octopuses):
        for j in range(n_octopuses):
            if matrix[i][j] == 0:
                n_flashes = n_flashes + 1
    return n_flashes


def all_flash(matrix):
    compare = matrix == np.zeros([n_octopuses, n_octopuses], int)
    if compare.all():
        return True
    else:
        return False


# First Part
print(several_steps(octopuses, 100)[1])
# Second Part


def second_part(steps):
    if all_flash(several_steps(octopuses, steps)[0]):
        return steps
    else:
        steps += 1
        return second_part(steps)


# print(all_flash(several_steps(octopuses, 195)[0]))
print(second_part(0))
f.close()
