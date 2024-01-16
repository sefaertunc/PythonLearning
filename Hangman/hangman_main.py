import hangman


hang_man = hangman.Hangman()
chosen_word = hang_man.word
word_length = hang_man.length
list_display = []
end_of_game = False

print(hang_man.get_logo())

for num in range(word_length):
    list_display += "_"

while not end_of_game:

    guessed_letter = hang_man.guess_letter(list_display)

    hang_man.replace_letter(guessed_letter, list_display)
    end_of_game = hang_man.check_letter(guessed_letter)

    print(hang_man.display_word(list_display))

    end_of_game = hang_man.check_winner(list_display)

    print(hang_man.get_stages(hang_man.lives))
