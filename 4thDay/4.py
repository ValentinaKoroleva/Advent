import numpy as np
import copy
# f = open("example.txt")
f = open("input.txt")
chosen_numbers = np.array(f.readline().strip().split(','), dtype=float)
f.readline()
f_list = f.readlines()
data = [np.zeros((5, 5))]
n = 0
b_number = 0
for row in f_list:
    if n > 4:
        n = 0
        b_number = b_number + 1
        array = np.zeros((5, 5))
        data.append(array)
    else:
        row = row.strip().replace('  ', ' ')
        for k in range(5):
            data[b_number][n][k] = row.split(' ')[k]
        n = n + 1


def is_winner(matrix):
    for i in range(5):
        r = 1
        c = 1
        for j in range(5):
            r = matrix[i][j] * r
            c = matrix[j][i] * c
        if c == -1 or r == -1:
            return True
    return False


def interim_score(matrix):
    score = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] != -1:
                score = matrix[i][j] + score
    return score


def final_score(boards):
    boards_checked = copy.deepcopy(boards)
    board_winner = -1
    for number in chosen_numbers:
        b_n = 0
        for b_n in range(len(boards_checked)):
            b = boards_checked[b_n]
            for rw in b:
                if number in rw:
                    rw[np.where(rw == number)] = -1
            if is_winner(b):
                board_winner = b_n
                break
        if board_winner >= 0:
            return number * interim_score(boards_checked[b_n]), b_n


print(final_score(data)[0])
while len(data) > 1:
    print(len(data))
    del data[final_score(data)[1]]
    print(final_score(data)[0])

f.close()
