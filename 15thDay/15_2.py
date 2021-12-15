import numpy as np
rows = open('input.txt').read().split('\n')
chiton_density = []
for row in rows:
    row = list(map(int, list(row)))
    chiton_density.append(row)
chiton_density = np.array(chiton_density)
chiton_density2 = np.array(chiton_density)
height = len(chiton_density)
width = len(chiton_density[0])
# x - col, y - row
start = (0, 0)
# start = (7, 8)
end = (len(chiton_density) - 1, len(chiton_density[0]) - 1)


def distance(node1, node2):
    if node1 == node2:
        return 0
    value = chiton_density2[node1[0]][node1[1]] + chiton_density[node2[0]][node2[1]]
    # value = 1000
    for n in neighbors(node2):
        if n is not None and value > chiton_density[n[0]][n[1]] + chiton_density[node2[0]][node2[1]]:
            value = chiton_density[n[0]][n[1]] + chiton_density[node2[0]][node2[1]]
            # print(distance(node2, end))
    # print(value)
    # chiton_density2[node2[0], node2[1]] = value
    return value


def neighbors(dot):
    x = dot[0]
    y = dot[1]
    up, down, left, right = None, None, None, None
    # if y - 1 in range(height):
    #     up = (x, y - 1)
    if y + 1 in range(height):
        down = (x, y + 1)
    # if x - 1 in range(width):
    #     left = (x - 1, y)
    if x + 1 in range(width):
        right = (x + 1, y)
    return [up, down, left, right]


# print(chiton_density)
print(neighbors(start))
# first_neighbors = neighbors(start)


def next_node(s):
    val = 1000
    node = ()
    first_neighbors = neighbors(s)
    for ni in first_neighbors:
        if ni is not None and val > distance(start, ni):
            val = distance(start, ni)
            node = ni
    # print(node)
    return val - 1, node


def generate():
    node = start
    total = 0
    total2 = 0
    step = 0
    while node != (8, 9):
        chiton_density[node[0]][node[1]] = 10
        # print(str(total) + '|' + str(node))
        node = next_node(node)[1]
        total = total + next_node(node)[0]
        total2 = total2 + chiton_density2[node[0]][node[1]]
        step += 1
        print(total)
    return total, total2


print(generate())
# print(chiton_density2)
