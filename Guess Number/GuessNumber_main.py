from GuessNumberBack import GuessNumber

print("Welcome to the Number Guessing Game!")
print("You have to choose a number between 1 and 100.")

the_game = GuessNumber()

while not the_game.isOver:
    if not the_game.isGameStart:
        the_game.create_number()
        the_game.identify_difficulty()
    the_game.guess_number()
    the_game.check_number()
    the_game.check_lives()
