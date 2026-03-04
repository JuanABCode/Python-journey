# logical operators

temp = float(input("What is the temperature Celcius: "))
is_raining = input("Is it raining outside (Y, N): ").strip().lower()
is_sunny = input("Is it sunny outside (Y, N): ").strip().lower()
is_snowing = input("Is it snowing outside (Y, N): ").strip().lower()

if temp > 100 and not is_raining == "y" and not is_sunny == "y" and not is_snowing == "y":
    print("Its a red moon the world is burning!")
elif temp > 50 or is_sunny == "y":
    print("Perfect")
elif temp > 10 and not is_raining == "y" and not is_snowing == "y":
    print("The temperature is cold but thas it")
elif temp < 10 and is_snowing == "y" and is_raining == "y":
    print("Its the end of the world out there, don't got outside!!!")
elif temp > 25 and is_sunny == "y" and not is_raining == "y" and not is_snowing == "y":
    print("Its ok to go outside be aware")
elif temp < 0 or is_snowing == "y" or is_raining == "y":
    print("Its freezing and wet outside")
else:
    print("Up to you if you want to go outside :)")