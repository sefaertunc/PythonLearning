import random

EASY_HEALTH = 10
HARD_HEALTH = 5


class GuessNumber:

    def __init__(self):
        self.lives = 0
        self.number = 0
        self.guessed_number = 0
        self.isGameStart = False
        self.isOver = False

    def create_number(self):
        self.number = random.randint(1, 100)

    def identify_difficulty(self):
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            self.lives = EASY_HEALTH
        else:
            self.lives = HARD_HEALTH
        self.isGameStart = True

    def guess_number(self):
        print(f"You have {self.lives} attempts remaining to guess the number.")
        self.guessed_number = int(input("Guess a number: "))

    def check_number(self):
        if self.guessed_number > self.number:
            print("Too high\nGuess again")
            self.lives -= 1
        elif self.guessed_number < self.number:
            print("Too low\nGuess again")
            self.lives -= 1
        else:
            print("Your guess is right. You win!")
            self.try_again()

    def check_lives(self):
        if self.lives == 0:
            print(f"The number was {self.number}.")
            print("You don't have attempt to guess. You lost!")
            self.try_again()

    def try_again(self):
        if input("Would you like to play again?").lower() == "y":
            self.clean_game()
            return
        else:
            self.isOver = True

    def clean_game(self):
        self.create_number()
        self.guessed_number = 0
        self.isOver = False
        self.isGameStart = False
