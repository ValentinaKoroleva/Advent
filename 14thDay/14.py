import copy as cp
import datetime
import math
from collections import Counter

start = datetime.datetime.now()
f = open('input.txt')
# f = open('example.txt')
polymer_template = f.readline().strip()
f.readline()
insertion_rules = f.readlines()
insertion_dic = dict()
for rule in insertion_rules:
    poly_line = rule.strip().split(' -> ')[0]
    insert = rule.strip().split(' -> ')[1]
    insertion_dic[poly_line] = insert
polymer_start = list(polymer_template)


def insert_in_pair(pair, new_element):
    return [pair[0], new_element, pair[1]]


def one_step(polymer):
    pairs = []
    for i in range(len(polymer) - 1):
        pairs.append([polymer[i], polymer[i + 1]])
    triples = []
    for p in pairs:
        p_line = p[0] + p[1]
        triples.append(insert_in_pair(p, insertion_dic[p_line]))
    result = ''
    for t in triples:
        triple_line = t[0] + t[1]
        result = result + triple_line
    result = result + triples[-1][2]
    return result


def several_steps(pairs, steps):
    polymer = cp.deepcopy(pairs)
    for s in range(steps):
        polymer = one_step(polymer)
    return polymer


def first_part(polymer):
    print(len(polymer))
    count = dict()
    for i in polymer:
        poly = list(i)
        for p in poly:
            count[p] = count.get(p, 0) + 1
    count_list = sorted((value, key) for (key, value) in count.items())
    return count_list[-1][0] - count_list[0][0]


# print(first_part(several_steps(polymer_start, 10)))
# first_part_time = datetime.datetime.now()
# print(first_part_time - start)

# Second Part
# print(insertion_dic)
insertion = dict()
for k, t in insertion_dic.items():
    letters = list(k)
    insertion[k] = (k[0] + t, t + k[1])
polymer_init = []
for i in range(len(polymer_start) - 1):
    polymer_init.append(polymer_start[i] + polymer_start[i + 1])


def second_part(pairs):
    count = dict()
    for p, c in pairs.items():
        p = list(p)
        count[p[0]] = count.get(p[0], 0) + c
        count[p[1]] = count.get(p[1], 0) + c
    count_list = sorted((value, key) for (key, value) in count.items())
    return math.ceil((count_list[-1][0] - count_list[0][0]) / 2)


# print(second_part(polymer_init))


def one_step_further(pairs, steps):
    s = 0
    count = dict()
    while s < steps:
        for p in pairs.copy():
            count[p] = count.get(p, 0) - 1
            p = insertion[p]
            count[p[0]] = count.get(p[0], 0) + 1
            count[p[1]] = count.get(p[1], 0) + 1
        s += 1
        print(s)
        print(datetime.datetime.now() - start)
    # count = dict()
    # for p in pairs:
    #     p = insertion[p]
    #     count[p[0]] = count.get(p[0], 0) + 1
    #     count[p[1]] = count.get(p[1], 0) + 1
    return count


print(polymer_init)
res = one_step_further(polymer_init, 10)
print(res)
print(second_part(res))
print(datetime.datetime.now() - start)
f.close()
