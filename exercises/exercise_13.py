# Temperature Converter

unit = input("What are we converting to Celcius(C), Fahrenheit(F): ").lower().strip()
amount = int(input("What is the temperature: "))

if unit == "c":
    convertion = (amount - 32) / 1.8
    print(f"{amount}F"f' to Celcius is {convertion:.1f}C')
elif unit == "f":
    convertion = (amount * 1.8) + 32
    print(f"{amount}C"f' to Fahrenheit is {convertion:.1f}F')
else:
    print("Invalid Response")
print("Fahrenheit Was Selected" if unit == "f" else "Fahrenheit Was Not Selected!")
print("Celcius Was Selected" if unit == "c" else "Celcius Was Not Selected!")