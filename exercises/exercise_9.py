# temperature converter

operator = input("What are we converting to (F, C): ").strip().capitalize()
temp = float(input("What is the temperature: "))

if operator == "F":
    convertion = (temp * 9/5) + 32
    print(f"Your temperature in F is {convertion:.2f} F")
elif operator == "C":
    convertion = (temp - 32) * 5/9
    print(f"Your temperature in C is {convertion:.2f} C")
else:
    print("INVALID RESPONSE")