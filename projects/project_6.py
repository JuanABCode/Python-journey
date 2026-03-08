# Limited guessing Game

import random

random_number = random.randint(1, 20)

print("Pick a number between 1 and 20 you have 5 tries!")

tries = 5
guess = 0

while guess != random_number and tries > 0:
    guess = int(input("pick a number between 1 and 20: "))
    if guess < 1 or guess > 20:
        print("Guess must be between 1 and 20 (You will not lose a try)")
        print(f"Remaining tries {tries}")
    elif guess < random_number:
        print("Too low")
        tries -= 1
        print(f"Remaining tries {tries}")
    elif guess > random_number:
        print("Too High")
        tries -= 1
        print(f"Remaining tries {tries}")
if guess == random_number:
    print(f"You guessed correctly the number {random_number}")
    print(f"Remaining tries {tries}")
else:
    print(f"You ran out of tries the number was {random_number}")
    print(f"Remaining tries {tries}")