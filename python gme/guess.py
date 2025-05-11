import random

def welcome_message():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

def get_user_guess():
    guess = int(input("Enter your guess: "))
    return guess

def check_guess(guess, secret_number):
    if guess < secret_number:
        print("Too low! Try again.")
        return False
    elif guess > secret_number:
        print("Too high! Try again.")
        return False
    else:
        print("Congratulations! You guessed it!")
        return True

def play_game():
    secret_number = random.randint(1, 100)
    welcome_message()
    guess_correct = False
    while not guess_correct:
        guess = get_user_guess()
        guess_correct = check_guess(guess, secret_number)

# Start the game
play_game()
