import itertools
f = open('input.txt')
# f = open('example.txt')
# f = open('example_1.txt')
f_list = f.readlines()


def permutation(string, i, length, answer):
    if i == length:
        answer.append(''.join(string))
    else:
        for j in range(i, length):
            string[i], string[j] = string[j], string[i]
            # keep increasing i by 1 till it becomes equal to 0
            permutation(string, i + 1, length, answer)
        string[i], string[j] = string[j], string[i]


def generate_strings(str_s, decode):
    result = {}
    for s in str_s:
        # answer = []
        # permutation(list(s), 0, len(s), answer)
        answer = itertools.permutations(s)
        answer = list(answer)
        answer = [''.join(permut) for permut in answer]
        for i in answer:
            result[i] = decode[s]
        if s == 'bcdfe':
            print(answer)
    return result


# First Part
order = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}
strings = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
decode_1 = {'abcefg':'0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5',
          'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}
decoding = generate_strings(strings, decode_1)
first_part = [2, 3, 4, 7]
# print(decoding['acedgfb'])
total_first_part = 0
for line in f_list:
    four_digits = line.split('|')[1].strip().split(' ')
    for i in four_digits:
        if len(i) in first_part:
            total_first_part = total_first_part + 1
    # signals = line.split('|')[0].strip().split(' ')
print(total_first_part)

# Second Part


def substract(a, b):
    a_s = set(a)
    b_s = set(b)
    return "".join(a_s - b_s)


def generate_decode(line):
    second_part = {2: 1, 3: 7, 4: 4, 7: 8}
    encode = dict()
    unknown = []
    signals = line.split('|')[0].strip().split(' ')
    for signal in signals:
        if len(signal) in second_part.keys():
            encode[second_part[len(signal)]] = signal
        else:
            unknown.append(signal)
    order['a'] = substract(encode[7], encode[1])
    for i in unknown:
        if len(i) == 6:
            four = set(encode[4]).copy()
            four.update(set(encode[7]))
            if four == set(i).intersection(four):
                encode[9] = i
                order['e'] = substract(encode[8], encode[9])
                for x in set(i).difference(four):
                    g = x
                order['g'] = g
            if substract(encode[8], i) in encode[7]:
                encode[6] = i
            elif i not in encode.values():
                encode[0] = i
    for i in unknown:
        if len(i) == 5:
            if order['g'] in i and order['e'] in i:
                encode[2] = i
            elif len(substract(i, encode[1])) == 3:
                encode[3] = i
            else:
                encode[5] = i
    decode_2 = {v: k for k, v in encode.items()}
    decoding_2 = generate_strings(decode_2.keys(), decode_2)
    return decode_2, decoding_2


res = []
for file_row in f_list:
    decode_2, decoding_2 = generate_decode(file_row)
    four_digits = file_row.split('|')[1].strip().split(' ')
    row = ''
    for digit in four_digits:
        if digit in decoding_2:
            row = row + str(decoding_2[digit])
    res.append(row)

total = 0
for number in res:
    total = total + int(number)

print(total)

f.close()
