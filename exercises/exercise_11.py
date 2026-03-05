# BMI Calculator

print("Metric Unit is Kg and meters")
print("Imperial Unit is Lbs and inches")
formulas = input("Which formula are we using today (Metric (M), Imperial (I)): ").lower().strip()

if formulas == "m":
    weight = float(input("How much do you weight in Kg: "))
    height = float(input("How tall are you in meters: "))
    fixed_height = height * 100
    bmi = weight / height**2
    print("---------- BMI ----------")
    print(f"Weight:{weight:>15.2f} Kg")
    print(f"Height:{fixed_height:>15.2f} Cm")
    if bmi > 30:
        obese = "Obese"
        print(f"BMI:{bmi:>21.2f}") # Bmi dosen't have to be inside if/elif it can be moves outside
        print(f"Results:{obese:>17}")
    elif bmi > 25:
        overweight = "Overweight"
        print(f"BMI:{bmi:>21.2f}")
        print(f"Results:{overweight:>17}")
    elif bmi > 18.5:
        normal = "Normal"
        print(f"BMI:{bmi:>21.2f}")
        print(f"Results:{normal:>17}")
    elif bmi < 18.5:
        underweight = "Underweight"
        print(f"BMI:{bmi:>21.2f}")
        print(f"Results:{underweight:>17}")
elif formulas == "i":
    weight = float(input("How much do you weight in Lbs: "))
    height = float(input("How tall are you in inches: "))
    fixed_height = height / 12
    bmi = (weight / height**2) * 703
    print("---------- BMI ----------")
    print(f"Weight:{weight:>14.2f} Lbs")
    print(f"Height:{fixed_height:>13.1f} feet")
    if bmi > 30:
        obese = "Obese"
        print(f"BMI:{bmi:>21.2f}")
        print(f"Results:{obese:>17}")
    elif bmi > 25:
        overweight = "Overweight"
        print(f"BMI:{bmi:>21.2f}")
        print(f"Results:{overweight:>17}")
    elif bmi > 18.5:
        normal = "Normal"
        print(f"BMI:{bmi:>21.2f}")
        print(f"Results:{normal:>17}")
    elif bmi < 18.5:
        underweight = "Underweight"
        print(f"BMI:{bmi:>21.2f}")
        print(f"Results:{underweight:>17}")
else:
    print("Invalid Response!!!")