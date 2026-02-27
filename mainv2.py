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
  guess = get_number("Enter your guess: "))
    attempts += 1
  result = check_guess(guess, number_to_guess)
    print(result)
  if result == "Correct":
     print(f"You guessed it in {attempts} tries! 🎉")
        break
  
#Game over message 
if attempts == max_tries and result !="Correct":
    print(f"Game over! The number was {number_to_guess}")
#score logging
with open("score.txt", "a") as f:
    f.write(f"Level {level}: {attempts} tries\n")
