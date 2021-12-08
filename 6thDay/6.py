import time
f = open('input.txt')
# f = open('example.txt')
initial_state = f.readline()
fish_school = initial_state.strip().split(',')
# print('Initial state: ' + initial_state)
start_time = time.time()

# First Part: For Small Numbers OK


def one_day_of_fish_life(data):
    result = []
    children = 0
    for fish in data:
        if int(fish) > 0:
            fish = int(fish) - 1
        else:
            fish = 6
            children = children + 1
        result.append(str(fish))
    for i in range(children):
        result.append(str(8))
    return result


def several_days_of_fish_life(data, days):
    if days > 1:
        days = days - 1
        data = one_day_of_fish_life(data)
        data = several_days_of_fish_life(data, days)
    elif days > 0:
        data = one_day_of_fish_life(data)
    return data


def print_answer(data, days):
    data = several_days_of_fish_life(data, days)
    grammar = 'day'
    if days > 1:
        grammar = 'days'
    state = ','.join(data)
    number_of_fish = len(data)
    if number_of_fish < 30:
        return 'After ' + str(days) + ' ' + grammar + ': ' + state, number_of_fish
    else:
        return 'After ' + str(days) + ' ' + grammar + ': There are more than 30 fish', number_of_fish


print(print_answer(fish_school, 18))
print("--- %s seconds ---" % (time.time() - start_time))
print(print_answer(fish_school, 80))
print("--- %s seconds ---" % (time.time() - start_time))
# > than 150 BAD

# Second Part: For Big Numbers


def count_states(data):
    fish_state = [0] * 9
    for i in data:
        fish_state[int(i)] = fish_state[int(i)] + 1
    return fish_state


def one_day(fish_state):
    # fish_state = count_states(data)
    children = fish_state[0]
    fish_state[0] = 0
    for i in range(9):
        if fish_state[i] > 0:
            if i > 0:
                fish_state[i - 1] = fish_state[i - 1] + fish_state[i]
                fish_state[i] = 0
    fish_state[6] = fish_state[6] + children
    fish_state[8] = children
    # print(fish_state)
    return fish_state


def several_days(data, days):
    # Day 0
    fish_state = count_states(data)
    for i in range(days):
        fish_state = one_day(fish_state)
    return sum(fish_state)


print(several_days(fish_school, 18))
print("--- %s seconds ---" % (time.time() - start_time))
print(several_days(fish_school, 80))
print("--- %s seconds ---" % (time.time() - start_time))
print(several_days(fish_school, 256))
print("--- %s seconds ---" % (time.time() - start_time))

f.close()
