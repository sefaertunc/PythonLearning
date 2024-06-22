import auction_base

the_game = auction_base.auction_base()
the_player = auction_base.auction_main_player()

while not the_game.end_game:
	the_game.choose_item()
	the_game.end_game = the_player.add_bid(the_game.player_bids)
	the_game.create_bids()
	the_game.show_bids()
	the_game.check_winner()
	the_game.show_winner()

	the_game.end_game = the_game.another_game()

	the_game.clean_bids()
	the_player.clean_bids()
