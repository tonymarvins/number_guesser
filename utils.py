# utils.py

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def log(message):
    print(f"[LOG] {message}")
