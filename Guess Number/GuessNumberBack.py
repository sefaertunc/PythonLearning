import random

EASY_HEALTH = 10
HARD_HEALTH = 5


class GuessNumber:

    def __init__(self):
        self.__lives = 0
        self.__number = 0
        self.__guessed_number = 0
        self.isOver = False
        self.create_number()
        self.identify_difficulty()

    def create_number(self):
        self.__number = random.randint(1, 100)

    def identify_difficulty(self):
        while True:
            level = input("Choose a difficulty. Type 'easy' or 'hard': ")
            if level == "easy" or level == "hard":
                break
            else:
                print("Invalid input. Please try again.")
                continue
        if level == "easy":
            self.__lives = EASY_HEALTH
        else:
            self.__lives = HARD_HEALTH

    def guess_number(self):
        print(f"You have {self.__lives} attempts remaining to guess the number.")
        while True:
            try:
                self.__guessed_number = int(input("Guess a number: "))
                break
            except ValueError:
                print("Invalid Input")

    def check_number(self):
        if self.__guessed_number > self.__number:
            print("Too high\nGuess again")
            self.__lives -= 1
        elif self.__guessed_number < self.__number:
            print("Too low\nGuess again")
            self.__lives -= 1
        else:
            print("Your guess is right. You win!")
            self.try_again()

    def check_lives(self):
        if self.__lives == 0:
            print(f"The number was {self.__number}.")
            print("You don't have attempt to guess. You lost!")
            self.try_again()

    def try_again(self):
        if input("Would you like to play again?").lower() == "y":
            self.clean_game()
            return
        else:
            self.isOver = True

    def clean_game(self):
        self.__guessed_number = 0
        self.isOver = False
        self.create_number()
        self.identify_difficulty()
