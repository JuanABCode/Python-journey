# while loop

name = input("Enter your name: ").strip()
age= int(input("Enter your age: "))
food = input("Enter a food you like (q to quit): ").strip().lower()
num = int(input("Enter a number between 1 - 10: "))

while name == "":
    print("you did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

while age < 0:
    print("Age can't be negative")
    age= int(input("Enter your age: "))
print(f"You are {age} years old")

while not food == "q":
    print(f"{food}")
    food = input("Enter a food you like (q to quit): ").strip().lower()
print("BYE")

while num < 1 or num > 10:
    print("Number has to be between 1 - 10")
    num = int(input("Enter a number between 1 - 10: "))
print(f"Your number is {num}")
