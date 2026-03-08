# Secure PIN Mask System

card_number = input("Enter your card number: ").strip()
pin = input("Enter your pin number (4 digits): ").strip()

attempts = 3

if len(card_number) < 12:
    print("Card number can't be under 12 characters")
elif not card_number.replace('-', '').isdigit():
    print("Card number can only have numbers")
else:
    last_digits = card_number[-4:]
    masked = "*" * len(card_number[:-4])
    masked_card = masked + last_digits
    print(f"Card Number: {masked_card}")
if len(pin) != 4:
    print("The lenght of the pin can't be more then 4 characters or less")
elif not pin.isdigit():
    print("Pin can only be digits")
else:
    print("Pin Created")
    
login_pin = ""

while login_pin != pin and attempts > 0:
        print(f"Card Number: {masked_card}")
        print("To login please enter your pin")
        login_pin = input("Enter the pin you created: ").strip()

        if login_pin != pin:
            attempts -= 1
            print("Access Denied")

if login_pin == pin:
     print("Access Granted")
else: 
    print("Card Locked")

