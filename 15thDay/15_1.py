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


def neighbors(x, y, v):
    # print(str(x) + '|' + str(y))
    up, down, left, right = None, 10, None, 10
    if y - 1 in range(height):
        up = chiton_density[x][y - 1] + v
    if y + 1 in range(height):
        down = chiton_density[x][y + 1] + v
    if x - 1 in range(width):
        left = chiton_density[x - 1][y] + v
    if x + 1 in range(width):
        right = chiton_density[x + 1][y] + v
    if up is None and left is None:
        return x, y, v
    else:
        # chiton_density[x][y] = 10
        print(chiton_density)
        print(str(up) + '|' + str(left))
        coordinates = ()
        if up is None:
            val = neighbors(x - 1, y, left)[0]
            coordinates = (x - 1, y)
        elif left is None:
            val = neighbors(x, y - 1, up)[0]
            coordinates = (x, y - 1)
        else:
            val1 = neighbors(x, y - 1, up)[0]
            val2 = neighbors(x - 1, y, left)[0]
            val = min(val1, val2)
            if val1 == val:
                coordinates = (x, y - 1)
            if val2 == val:
                coordinates = (x - 1, y)
        print(coordinates)
        # val = min(down, right)
        # coordinates = ()
        # if down == val:
        #     coordinates = (x, y + 1)
        # if right == val:
        #     coordinates = (x + 1, y)
        # chiton_density[x][y] = 10
        # chiton_density[coordinates[0]][coordinates[1]] = 10
    return v + val, coordinates


def step(s):
    steps = 0
    value = chiton_density[s[0], s[1]]
    coord = s
    while coord != start:
        value, coord = neighbors(coord[0], coord[1], value)
        steps += 1
    return value


print(chiton_density)
# print(neighbors(start[0], start[1], chiton_density[start[0], start[1]]))
print(step(end))
print(chiton_density)

