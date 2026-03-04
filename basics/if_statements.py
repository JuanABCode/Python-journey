# if statements

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old")
elif age >= 18:
    print("You are older then 18")
elif age < 0:
    print("You havent been born yet")
elif age < 18:
    print("You are a child")
else:
    print("Invalid response")

food = input("Would you like some food (Y/N): ")

if food == "Y":
    print("You can have some food")
elif food == "":
    print("You did not type anything")
else:
    print("No food for you")

for_sale = True
is_online = False

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

if is_online:
    print("You are online")
else:
    print("You are offline")