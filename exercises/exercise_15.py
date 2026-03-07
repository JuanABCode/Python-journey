# basic login system

correct_username = "Jumpywizard"
correct_password = "@Juan2477"

attempts = 3

while attempts > 0:
    print("Username must have 1 capital letter!")
    username = input("To sign in enter your username: ").strip()
    print("Password must include 1 special character")
    print("Password must have at least 1 number")
    print("Password must have 1 capital letter!")
    password = input("Enter your password: ").strip()
    if username == correct_username and password == correct_password:
        print("Successfully signed in")
        break
    else:
        attempts -= 1
        print(f"You have {attempts} left!!!")
else:
    print("You ran out of tries you are locked out")
    print("You must wait 24 hours to try again!")