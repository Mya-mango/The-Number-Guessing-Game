import random

print("Welcome to the Number Guessing Game!")

secret_number = random.randint(1,20)
guess = 0
attempts = 0
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 20:"))

    attempts += 1

    if guess < secret_number:
        print("Too low! try again.")
    elif guess > secret_number:
        print("Too high! try again.")
    else:
        print("Congratulations you guessed it in",attempts,"tries!")
    
