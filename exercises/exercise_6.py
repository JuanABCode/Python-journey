# hypotunese of a right triangle

import math

num_1 = float(input("What is the first number: "))
num_2 = float(input("What is the second number: "))

hypotunese = math.sqrt(pow(num_1, 2) + pow(num_2, 2))

print(f"The hypotunese of the right triangle is {hypotunese:,.2f}")