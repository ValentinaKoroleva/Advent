import re
import copy as cp
f = open('input.txt')
# f = open('example.txt')
# f = open('larger_example.txt')
# f = open('simpler_example.txt')
f_list = f.readlines()
start_nodes = []
end_nodes = []
neighbours = dict()
task = 2
for line in f_list:
    line = line.strip()
    if re.search("start", line):
        line = line.replace("start", '')
        line = line.replace("-", '')
        start_nodes.append(line)
    elif re.search("end", line):
        line = line.replace("end", '')
        line = line.replace("-", '')
        end_nodes.append(line)
    else:
        from_ = line.split('-')[0]
        to_ = line.split('-')[1]
        if from_ not in neighbours.keys():
            neighbours[from_] = [to_]
        else:
            neighbours[from_].append(to_)
        if to_ not in neighbours.keys():
            neighbours[to_] = [from_]
        else:
            neighbours[to_].append(from_)


def is_big(cave_name):
    upper_case = cave_name.upper()
    return upper_case == cave_name


def which_part(node, path, task_part):
    if task_part == 1:
        return node not in path
    if task_part == 2:
        fav = get_favourite(path)
        # if fav is None:
        #     fav = node
        return node not in path or fav is None
        # return node != path[0]


def get_favourite(path):
    count = dict()
    result = None
    for element in path:
        count[element] = count.get(element, 0) + 1
    for element in path:
        if not is_big(element) and count[element] > 1 and result is None:
            result = element
            # print(path)
        # elif not is_big(element) and count[element] > 1 and result is not None:
        #     print(path)
    return result


all_paths = []


def create_paths(start, paths):
    result = []
    if paths[0] == '':
        for s in start:
            paths.append([s])
            if s in end_nodes:
                all_paths.append([s])
        del paths[0]
        result = paths
    else:
        for p in paths:
            for new in neighbours[p[-1]]:
                if is_big(new) or which_part(new, p, task):
                    result.append(p + [new])
                    all_paths.append(p + [new])
    return result


res = 1
step = 0
suka = ['']
while len(suka) > 0:
    suka = create_paths(start_nodes, suka)
    # print(suka)
    step += 1


def bad_path(path):
    if path[-1] not in end_nodes:
        return True
    # count = dict()
    # for c in path:
    #     count[c] = count.get(c, 0) + 1
    # for c in count.keys():
    #     if not is_big(c) and count[c] > 1:
    #         return True
    return False


total_paths = cp.deepcopy(all_paths)
for a in all_paths:
    if bad_path(a):
        total_paths.remove(a)

print(len(total_paths))
# print(total_paths)
# for a in total_paths:
#     print(['start'] + a + ['end'])
# print(end_nodes)
# print(is_big('HN'))
f.close()
