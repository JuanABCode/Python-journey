# Weight converter

operator = input("What are we converting to (Kg, Lb): ").capitalize().strip()
weight = float(input("How much is the weight: "))

if operator == "Kg":
    convertion = weight * 0.4536
    print(f"The weight in Kg is {convertion:.2f}")
elif operator == "Lb":
    convertion = weight * 2.205
    print(f"The weight in Lb is {convertion:.2f}")
else:
    print("INVALID RESPONSE")