# basic Calculator

math = input("Which operator are you going to use (+, -, *, /): ")
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if math == "+":
    total = num_1 + num_2
    print(f"The total is {total:,.2f}")
elif math == "-":
    total = num_1 - num_2
    print(f"The total is {total:,.2f}")
elif math == "*":
    total = num_1 * num_2
    print(f"The total is {total:,.2f}")
elif math == "/":
    total = num_1 / num_2
    print(f"The total is {total:,.2f}")
else:
    print("INVALID RESPONSE")