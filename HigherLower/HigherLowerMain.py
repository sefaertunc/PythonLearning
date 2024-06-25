from HigherLowerBase import HigherLower
import HigherLowerArt as Art


the_game = HigherLower()
print(Art.logo)

while not the_game.game_end:
	the_game.chose_competitor()
	the_game.show_competitors('a')
	print(Art.vs)
	the_game.show_competitors('b')
	the_game.make_guess()
	the_game.show_result()
