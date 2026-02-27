# Welcome message
print(f"\nWelcome to {APP_NAME}!")
# Level selection
print("\nSelect difficulty level:")
print("1. Easy (1-50, 10 tries)")
print("2. Medium (1-100, 7 tries)")
print("3. Hard (1-200, 5 tries)")

level = input("Choose level (1-3): ")

if level == "1":
  max_tries = 10
  number_to_guess = random.randint(1, 50)
elif level == "2":
  max_tries = 12
  number_to_guess = random.randint(1,100)
else:
  max_tries = 15
  number_to_guess = random.randint(1,200)
