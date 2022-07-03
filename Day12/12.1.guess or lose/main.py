import random

from art import logo


def checktheDifficulity():
    difficulity = input("Choose a difficulity 'easy' or 'hard' ").lower()
    if difficulity == "hard":
        return 5
    else:
        return 10


def checkAnswer(guessNum, GUESSED_NUMBER, ATTEMPS):
    if guessNum > GUESSED_NUMBER:
        print("Too high")
        return ATTEMPS - 1

    elif guessNum < GUESSED_NUMBER:
        print("Too Low")
        return ATTEMPS - 1
    else:
        print(f"You got it the number was {GUESSED_NUMBER}")


def game():
    print(logo + "\nwelcome to number guessing game.\n\nI'm thinking of number between 1 to 100.")

    GUESSED_NUMBER = random.randint(0, 101)

    # assign the difficulity
    attemps = checktheDifficulity()
    guess = 0

    while guess != GUESSED_NUMBER:
        print(f"You have {attemps} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))

        # check the left attemp number
        attemps = checkAnswer(guess, GUESSED_NUMBER, attemps)
        if attemps == 0:
            print("game over")
            return
            # we can write break too

        elif guess != GUESSED_NUMBER:
            print("Guess again.")


game()
