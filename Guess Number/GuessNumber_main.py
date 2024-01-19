from GuessNumberBack import GuessNumber

print("Welcome to the Number Guessing Game!")
print("You have to choose a number between 1 and 100.")

is_game_over = False
the_game = GuessNumber()
the_game.create_number()
the_game.identify_difficulty()

while not the_game.isOver:
    the_game.guess_number()
    the_game.check_number()
    the_game.check_lives()
