#game.py
import random
from config import LEVELS

def generate_number(level):
  rng, tries = LEVELS[level]
  return random.randint(1, rng),tries
def check_guess(guess, number):
    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    else:
        return "Correct"
