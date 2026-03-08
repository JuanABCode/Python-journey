# Username Validator

print("Username must be at least 3 characters long!")
print("Username must not include spaces!!")
print("Must start with a letter!!!")
username = input("Create a username: ").strip()

while len(username) < 3 or " " in username or username[0].isdigit():
    if " " in username:
        print("Username has spaces")
        print("Username must not include spaces")
    if username[0].isdigit():
        print("Username must start with a letter!")
    if len(username) < 3:
        print("Username is too short")
    username = input("Create a username: ").strip()
print(f"Welcome, {username}! Your account has been created.")   