from hangman_words import word_list
from hangman_art import stages, logo
import random

chosen_word = random.choice(word_list)
list_display = []
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

for num in range(word_length):
    list_display += "_"

while not end_of_game:
    # player input
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in list_display:
        print(f"You have already guessed {guessed_letter}")
    # Letter check loop
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guessed_letter:
            list_display[pos] = letter

    if guessed_letter not in chosen_word:
        print("That's wrong. You are losing a live.")
        lives -= 1
        if lives < 1:
            end_of_game = True
            print(f"The word was {chosen_word}")
            print("You lost!!!")

    print(f"{' '.join(list_display)}")

    if "_" not in list_display:
        end_of_game = True
        print("You won!!")

    print(stages[lives])
