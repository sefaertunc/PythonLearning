import random
from hangman_words import word_list
import hangman_art


class Hangman(object):
    def __init__(self):
        self.lives = 6
        self.word = random.choice(word_list)
        self.length = len(self.word)
        self.display_word(word_list)

    def replace_letter(self, guessed_letter, display_list):
        for pos in range(self.length):
            letter = self.word[pos]
            if letter == guessed_letter:
                display_list[pos] = letter

    def check_letter(self, guessed_letter):
        if guessed_letter not in self.word:
            print("That's wrong. You are losing a live.")
            self.lives -= 1
            if self.lives < 1:
                print(f"The word was {self.word}")
                print("You lost!!!")
                return True

    @staticmethod
    def guess_letter(display_list):
        letter = input("Guess a letter: ").lower()
        if letter in display_list:
            print(f"You have already guessed {letter}")
        return letter

    @staticmethod
    def check_winner(display_list):
        if "_" not in display_list:
            print("You won!!")
            return True

    @staticmethod
    def display_word(display_list):
        return f"{' '.join(display_list)}"

    @staticmethod
    def get_logo():
        return hangman_art.logo

    @staticmethod
    def get_stages(index):
        return hangman_art.stages[index]
