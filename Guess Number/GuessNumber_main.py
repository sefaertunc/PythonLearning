import random

EASY_HEALTH = 10
HARD_HEALTH = 5


def check_number(guess, lives):
    if guess > the_number:
        print("Too high\nGuess again")
        return lives - 1
    elif guess < the_number:
        print("Too low\nGuess again")
        return lives - 1
    else:
        print("Your guess is right. You win!")


def identify_health(level):
    if level < 1:
        return EASY_HEALTH
    else:
        return HARD_HEALTH


def guess_number():
    number = int(input("Guess a number: "))
    return number


print("Welcome to the Number Guessing Game!")
print("You have to choose a number between 1 and 100.")

difficulties = {"easy": 0, "hard": 1}
is_game_over = False

the_number = random.randint(1, 100)

difficulty = difficulties[input(
    "Choose a difficulty. Type 'easy' or 'hard': ")]
health = identify_health(difficulty)

guessed_number = 0

while guessed_number != the_number:
    print(f"You have {health} attemps remaining to guess the number.")
    guessed_number = guess_number()
    health = check_number(guessed_number, health)

    if health == 0:
        print(f"The number was {the_number}.")
        print("You don't have attemp to guess. You lost!")
        break
