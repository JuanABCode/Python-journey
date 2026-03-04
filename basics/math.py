# math

import math

n = 5
m = 9.4

print(math.pi)
print(math.e)
total_1 = math.sqrt(n)
total_2 = math.ceil(m)
total_3 = math.floor(m)

print(total_1)
print(total_2)
print(total_3)

friends = 10

friends = friends + 1
friends += 1

friends -= 2
friends *= 5
friends /= 2
friends **= 2

# finds the remainder of the number for example 10 3 + 3 + 3 = 9 remainder 1 can't go in a group evenly
remainder = friends % 3

print(friends)

x = 3.14
y = -4
z = 5

# rounds to the nearest whole number
result_5 = round(x)
# Finds the absolute value closer to 0
result_4 = abs(y)
# makes y multiple by itself x amount of times
result_3 = pow(y,3)
# Prints the biggest value
result_1 = max(x, y, z)
# Prints the lowest value
result_2 = min(x, y, z)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)