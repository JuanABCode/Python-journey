# user input exercise

print("Username can't be more then 12 characters")
print("Username can't contain spaces")
print("Username can't contain digits")

user_name = input("Enter a username: ").strip()

spaces = user_name.find(" ")

if len(user_name) > 12:
    print("Username Can't be more then 12 characters!")
elif not user_name.find(" ") == -1:
    print("You can't have spaces")
elif not user_name.isalpha():
    print("You can't have numbers")
else:
    print(f"Welcome {user_name}")