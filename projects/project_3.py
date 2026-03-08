# account sign up and login system (CLI)

print("Create an account and login to get free candy :)\n")
print("Username can't be longer than 12 characters\n")
print("Username can't contain spaces\n")
print("Username Can't contain numbers or special characters\n")

username = input("Enter a new username: ").strip()

print("Password must be at least 8 characters\n")
print("Password must include 1 digit\n")
print("Password can't contain spaces\n")

password = input("Create a password: ").strip()

print("Must be over 18 years old\n")

age = int(input("How old are you: "))

status = ("Adult" if age >= 18 else "Child")


if age < 18:
    print("Sorry, you must be 18+ to continue.")
elif len(username) > 12:
    print("Username can't be longer than 12 characters\n")
elif " " in username:
    print("Username can't contain spaces\n")
elif not username.isalpha():
    print("Username can't contain numbers or special characters\n")
else:
    print(f"{username} has been created\n")
    if len(password) < 8:
        print("Password is too short\n")
    elif " " in password:
        print("Password can't contain spaces\n")
    elif not any(num.isdigit() for num in password):
        print("Password must contain one number\n")
    else:
        covered = "*" * len(password)
        print(f"{covered} Password has been created\n")
        print("Please Enter your username and password to login\n")
        created_username = input("Please enter your username that you created: ").strip()
        created_password = input("Please enter your password that you created: ").strip()
        counter = 3
        
        while (created_username != username or created_password != password) and counter > 0:
            print("Access Denied")
            counter = counter - 1
            created_username = input("Please enter your username that you created: ").strip()
            created_password = input("Please enter your password that you created: ").strip()
        if created_username == username and created_password == password:
            print("Access Granted")
            print(status)
            print(f"Welcome {username}")
        else:
            print("Access Denied")
            print("You ran out of tries")



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    """ 
        
        
        if created_username == username and created_password == password:
            print("Access Granted")
            print(status)
        else:
            print("Access Denied")
            print("You can try again 3 tries left")
            created_username = input("Please enter your username that you created: ").strip()
            created_password = input("Please enter your password that you created: ").strip()
            if created_username == username and created_password == password:
                print("Access Granted")
                print(status)
            else:
                print("Access Denied")
                print("You can try again 2 tries left")
                created_username = input("Please enter your username that you created: ").strip()
                created_password = input("Please enter your password that you created: ").strip()
                if created_username == username and created_password == password:
                    print("Access Granted")
                    print(status)
                else:
                    print("Access Denied")
                    print("You can try again 1 try left")
                    created_username = input("Please enter your username that you created: ").strip()
                    created_password = input("Please enter your password that you created: ").strip()
                    if created_username == username and created_password == password:
                        print("Access Granted")
                        print(status)
                    else:
                        print("Access Denied")
                        print("You have 0 tries left")

"""