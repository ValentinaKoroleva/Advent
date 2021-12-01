f = open("input.txt")
test = open("output.txt", "w")
prev = ''
count1 = 0
count2 = 0
order = 0
three_sum = 0
x1 = 0
x2 = 0
x3 = 0
for x in f:
    res = 'first'
    # First Part
    if order > 0 and int(x) > int(prev):
        count1 = count1 + 1
        res = "increased"
    else:
        res = "decreased"
    # Second Part
    if order == 0:
        x1 = x
    elif order == 1:
        x2 = x
    else:
        x3 = x
        three_sum_new = int(x1) + int(x2) + int(x3)
        if three_sum_new > three_sum and three_sum > 0:
            count2 = count2 + 1
        three_sum = int(x1) + int(x2) + int(x3)
        print(int(x1) + int(x2) + int(x3))
        x1 = x2
        x2 = x3
    prev = x
    order = order + 1
    line = x.strip() + "|" + res + "\n"
    line = x.strip() + "|" + str(three_sum) + "\n"
    test.write(line)

print(count1)
print(count2)
