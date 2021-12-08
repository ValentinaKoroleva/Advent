import math
import statistics
f = open('input.txt')
# f = open('example.txt')
initial_state = f.readline()
crabs = initial_state.strip().split(',')
crabs = list(map(int, crabs))
print(statistics.median(crabs))
# First Part: Constant Fuel
# I don't know why that works
perfect_crab_1 = statistics.median(crabs)
total_fuel_1 = 0
for c in crabs:
    total_fuel_1 = total_fuel_1 + abs(c - perfect_crab_1)
print(total_fuel_1)
# Second Part: Cost of Fuel Changes
perfect_crab_2 = math.floor(statistics.mean(crabs))
print(perfect_crab_2)
# perfect_crab_2 = 466
total_fuel_2 = 0
for c in crabs:
    fuel = 0
    for i in range(1, abs(c - perfect_crab_2) + 1):
        fuel = i + fuel
    total_fuel_2 = total_fuel_2 + fuel
print(total_fuel_2)
f.close()
