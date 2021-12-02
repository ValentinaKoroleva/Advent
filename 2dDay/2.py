f = open("input.txt")
depth_1 = 0
depth_2 = 0
h_position = 0
aim = 0
for x in f:
    direction = x.split(' ')[0]
    amount = int(x.split(' ')[1])
    if direction == 'forward':
        h_position = h_position + amount
        depth_2 = depth_2 + aim * amount
    elif direction == 'up':
        depth_1 = depth_1 - amount
        aim = aim - amount
    elif direction == 'down':
        depth_1 = depth_1 + amount
        aim = aim + amount

print(depth_1 * h_position)
print(depth_2 * h_position)