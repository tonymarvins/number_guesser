#game.py
import random
from config import LEVELS

def generate_number(level):
  rng, tries = LEVELS[level]
  return random.randint(1, rng),tries
  
