import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 0

print("Guess the number (between 1 and 10):")

# Loop until the user guesses the correct number
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low, try again.")
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
        break
