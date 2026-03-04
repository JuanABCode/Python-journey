# Age Access System

age = int(input("How old are you: "))

identification = input("Do you have a ID (y. n): ").strip().lower()


if age >= 65:
    if identification == "y":
        print("You are a senior and have identification")
    elif identification == "n":
        print("You are a senior but have no identification")
    else:
        print("INVALID RESPONSE")
elif age >= 18:
    if identification == "y":
        print("You are over 18 and have identification")
    elif identification == "n":
        print("You are over 18 but have no identification")
    else:
        print("INVALID RESPONSE")
elif age < 18:
    print("You are underage")
else:
    print("INVALID RESPONSE")