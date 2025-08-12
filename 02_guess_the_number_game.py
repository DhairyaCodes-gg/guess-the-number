import random

secret_number = random.randint(1, 100)  # random number between 1 and 100
attempts = 0

print("🎯 Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! 📉")
    elif guess > secret_number:
        print("Too high! 📈")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} tries.")
        break
