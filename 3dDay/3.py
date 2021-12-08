# First Part

f = open("input.txt")
# f = open("example_1.txt")
f_list = f.readlines()


def first_part(data):
    gamma = ''
    epsilon = ''
    order = 0
    ones = len(list(data[0].strip())) * [0]
    for x in data:
        digits = list(x.strip())
        for i in range(len(digits)):
            ones[i] = int(ones[i]) + int(digits[i])
        order = order + 1
    for i in range(len(ones)):
        if ones[i] >= order/2:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
    return gamma, epsilon


def bin2dec(binary):
    digits = list(binary)
    digits.reverse()
    dec = 0
    for i in range(len(digits)):
        dec = dec + int(digits[i]) * 2 ** i
    return dec


(gamma_res, epsilon_res) = first_part(f_list)
gamma_dec = bin2dec(gamma_res)
epsilon_dec = bin2dec(epsilon_res)
print(gamma_dec * epsilon_dec)

# Second Part


def filter_data(data, type):
    result = data.copy()
    length = len(list(data[0].strip()))
    for col in range(length):
        if len(result) > 1:
            (g, e) = first_part(result)
            for line in data:
                digits = list(line.strip())
                if type == 1:
                    bit_criteria = list(g)
                else:
                    bit_criteria = list(e)
                if digits[col] != bit_criteria[col] and line in result:
                    result.remove(line)
    return result


oxygen_list = filter_data(f_list, 1)
CO2_list = filter_data(f_list, 0)

oxygen = bin2dec(oxygen_list[0].strip())
CO2 = bin2dec(CO2_list[0].strip())

print(oxygen * CO2)
f.close()
