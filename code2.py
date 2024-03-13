
# Path: code3.py
import random
number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Enter a number between 1 and 100: "))
    attempts += 1
    if guess == number:
        print("Congratulations! You guessed the correct number in", attempts, "attempts.")
        break
    elif guess < number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")

