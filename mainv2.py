from game import generate_number, check_guess
from utils import get_number, log
from config import APP_NAME, LEVELS

# Welcome message
print(f"\nWelcome to {APP_NAME}!")
# Level selection
print("\nSelect difficulty level:")
print("1. Easy (1-50, 10 tries)")
print("2. Medium (1-100, 7 tries)")
print("3. Hard (1-200, 5 tries)")

level = input("Choose level (1-3): ")

number_to_guess, max_tries = generate_number(level)

log(f"Game started at level {level}")
attempts = 0
while attempts < max_tries:
  guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == number_to_guess:
        print(f"You guessed it in {attempts} tries! 🎉")
        break
    else:
        print("Wrong! Try again.")
if guess < number_to_guess:
  print("Too low!")
elif guess > number_to_guess:
  print("Too high!")

if attempts == max_tries and guess != number_to_guess:
    print(f"Game over! The number was {number_to_guess}")
