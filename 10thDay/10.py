f = open('input.txt')
# f = open('example.txt')
f_list = f.readlines()

correspond = {'(': ')', '[': ']', '{': '}', '<': '>'}
score_params = {')': 3, ']': 57, '}': 1197, '>': 25137}
score_params_2 = {')': 1, ']': 2, '}': 3, '>': 4}
# char_test = list(f_list[0].strip())


def cleaning(chars, score):
    for i in range(len(chars)):
        if i - 1 in range(len(chars)) and i in range(len(chars)):
            if chars[i] in correspond.values() and chars[i - 1] in correspond.keys():
                if chars[i] != correspond[chars[i - 1]]:
                    score = score + score_params[chars[i]]
                del chars[i]
                del chars[i - 1]
                chars, score = cleaning(chars, score)
    return chars, score


def find_closing(chars):
    for c in chars:
        if c in correspond.values():
            return True
    return False


total_score = 0
incomplete_lines = []
for r in f_list:
    line = list(r.strip())
    while find_closing(line):
        line, line_score = cleaning(line, 0)
        if line_score == 0:
            incomplete_lines.append(line)
        total_score = total_score + line_score
print(total_score)
# print(incomplete_lines)
scores = []
for k in incomplete_lines:
    line_score = 0
    k.reverse()
    for c in k:
        line_score = line_score * 5 + score_params_2[correspond[c]]
    scores.append(line_score)
scores.sort()
print(scores[len(scores) // 2])
f.close()
