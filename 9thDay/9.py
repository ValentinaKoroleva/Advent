f = open('input.txt')
# f = open('example.txt')
f_list = f.readlines()


def is_low_point(data, row, col):
    value = data[row][col]
    if row - 1 in range(0, len(data)):
        up = data[row - 1][col]
    else:
        up = 10
    if row + 1 in range(0, len(data)):
        down = data[row + 1][col]
    else:
        down = 10
    if col - 1 in range(0, len(data[0])):
        left = data[row][col - 1]
    else:
        left = 10
    if col + 1 in range(0, len(data[0])):
        right = data[row][col + 1]
    else:
        right = 10
    if value < min(up, down, left, right):
        return True
    else:
        return False


def basin(data, row, col, basin_members):
    basin_members.append([row, col])
    if row - 1 in range(0, len(data)):
        up = data[row - 1][col]
        if up < 9:
            if [row - 1, col] not in basin_members:
                basin(data, row - 1, col, basin_members)
    if row + 1 in range(0, len(data)):
        down = data[row + 1][col]
        if down < 9:
            if [row + 1, col] not in basin_members:
                basin(data, row + 1, col, basin_members)
    if col - 1 in range(0, len(data[0])):
        left = data[row][col - 1]
        if left < 9:
            if [row, col - 1] not in basin_members:
                basin(data, row, col - 1, basin_members)
    if col + 1 in range(0, len(data[0])):
        right = data[row][col + 1]
        if right < 9:
            if [row, col + 1] not in basin_members:
                basin(data, row, col + 1, basin_members)


matrix = []
low_points = []
for i in range(len(f_list)):
    line = list(f_list[i].strip())
    line = list(map(int, line))
    matrix.append(line)
first_answer = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if is_low_point(matrix, i, j):
            first_answer = first_answer + matrix[i][j] + 1
            low_points.append([i, j])
print(first_answer)
# print(low_points)
sizes = []
for coordinate in low_points:
    x = coordinate[0]
    y = coordinate[1]
    members = []
    basin(matrix, x, y, members)
    sizes.append(len(members))
    # print(len(basin_members))
first = max(sizes)
# print(first)
sizes.remove(first)
second = max(sizes)
# print(second)
sizes.remove(second)
third = max(sizes)
# print(third)
print(first * second * third)
f.close()
