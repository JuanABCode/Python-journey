# conditional expression also named as (ternary operator)

num = 5
a = 6
b = 7
age = 33
temperature = 25
user_role = "admin"


print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"

print(result)

max_num = a if a > b else b
min_num = a if a < b else b

status = "Adult" if age >= 18 else "Child"

print("Hot" if temperature > 25 else "Cold")
print("Full Access" if user_role == "admin" else "Limited Access")

print(max_num)
print(min_num)
print(status)
