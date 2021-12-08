# x1 - horizontal, i.e. col, y1 - vertical, i.e. row
import numpy as np
# f = open('example_1.txt')
f = open('input.txt')
f_list = f.readlines()


def initiate_diagram(data):
    diagram_length = 0
    for line in data:
        cells = line.strip().split(' ')
        # print(cells)
        (x1, y1) = cells[0].split(',')
        (x2, y2) = cells[2].split(',')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if max(x1, x2, y1, y2) > diagram_length:
            diagram_length = max(x1, x2, y1, y2)
    diagram_length = diagram_length + 1
    diagram = np.array([['.'] * diagram_length] * diagram_length)
    return diagram


def display_hydrothermal_vents(data):
    diagram = initiate_diagram(data)
    for line in data:
        cells = line.split(' ')
        (x1, y1) = cells[0].split(',')
        (x2, y2) = cells[2].split(',')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if x1 < x2:
            xs = np.arange(x1, x2 + 1)
        else:
            xs = np.arange(x1, x2 - 1, -1)
        if y1 < y2:
            ys = np.arange(y1, y2 + 1)
        else:
            ys = np.arange(y1, y2 - 1, -1)
        if x1 != x2 and y1 != y2:
            # diagonal condition: Second Part
            diag = []
            if len(xs) != len(ys):
                print('not 45 degrees')
                continue
            else:
                for k in range(len(xs)):
                    diag.append([xs[k], ys[k]])
            for (x, y) in diag:
                if diagram[y][x] == '.':
                    diagram[y][x] = 1
                else:
                    diagram[y][x] = int(diagram[y][x]) + 1
            continue
        if x1 != x2:
            for x in xs:
                if diagram[y1][x] == '.':
                    diagram[y1][x] = 1
                else:
                    diagram[y1][x] = int(diagram[y1][x]) + 1
        if y1 != y2:
            for y in ys:
                if diagram[y][x1] == '.':
                    diagram[y][x1] = 1
                else:
                    diagram[y][x1] = int(diagram[y][x1]) + 1
    return diagram


def two_overlaps(data):
    diagram = display_hydrothermal_vents(data)
    result = 0
    for i in range(len(diagram)):
        for j in range(len(diagram)):
            if diagram[i][j] == '.':
                continue
            else:
                if int(diagram[i][j]) >= 2:
                    result = result + 1
    return result


# print(display_hydrothermal_vents(f_list))
print(two_overlaps(f_list))
f.close()
