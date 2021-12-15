import numpy as np
rows = open('example.txt').read().split('\n')
chiton_density = []
for row in rows:
    row = list(map(int, list(row)))
    chiton_density.append(row)
chiton_density = np.array(chiton_density)
height = len(chiton_density)
width = len(chiton_density[0])
# x - col, y - row
start = (0, 0)
# start = (7, 8)
end = (len(chiton_density) - 1, len(chiton_density[0]) - 1)


def neighbors(dot, v):
    x = dot[0]
    y = dot[1]

    chiton_density[x][y - 1], get_up(dot, v)[1] + get_up(get_up(dot, v)[0], get_up(dot, v)[1])[1]
    get_up(dot, v) + get_up(get_up(dot, v)[0], get_up(dot, v)[1])
    get_up(dot, v) + get_up(get_up(dot, v)[0], get_up(dot, v)[1])
    get_up(dot, v) + get_up(get_up(dot, v)[0], get_up(dot, v)[1])
    if y - 1 in range(height):
        up = (x, y - 1)
        up_value = chiton_density[x][y - 1] + v
    if y + 1 in range(height):
        down = (x, y + 1)
        down_value = chiton_density[x][y + 1] + v
    if x - 1 in range(width):
        left = (x - 1, y)
        left_value = chiton_density[x - 1][y] + v
    if x + 1 in range(width):
        right = (x + 1, y)
        right_value = chiton_density[x + 1][y] + v
    neighbors(up[0], up[1], up_value)
    return up_value, down_value, right_value, left_value
    # min(up_value, down_value, right_value, left_value)
    # neighbors()


def get_up(dot, value):
    x = dot[0]
    y = dot[1]
    new_dot, new_dot_value = None, value
    if y - 1 in range(height):
        new_dot = (x, y - 1)
        new_dot_value = chiton_density[x][y - 1] + value
    return new_dot, new_dot_value


def get_down(dot, value):
    x = dot[0]
    y = dot[1]
    new_dot, new_dot_value = None, value
    if y + 1 in range(height):
        new_dot = (x, y - 1)
        new_dot_value = chiton_density[x][y + 1] + value
    return new_dot, new_dot_value


def get_right(dot, value):
    x = dot[0]
    y = dot[1]
    new_dot, new_dot_value = None, value
    if x + 1 in range(width):
        new_dot = (x + 1, y)
        new_dot_value = chiton_density[x + 1][y] + value
    return new_dot, new_dot_value


def get_left(dot, value):
    x = dot[0]
    y = dot[1]
    new_dot, new_dot_value = None, value
    if x - 1 in range(width):
        new_dot = (x - 1, y)
        new_dot_value = chiton_density[x - 1][y] + value
    return new_dot, new_dot_value


neighbors(start, 0)

print(chiton_density)
