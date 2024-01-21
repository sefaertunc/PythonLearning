from Blackjack_Base import Blackjack

the_game = Blackjack()


def play_game():
    is_game_over = False

    for _ in range(2):
        the_game.user_hand.append(the_game.deal_card())
        the_game.comp_hand.append(the_game.deal_card())

    while not is_game_over:
        the_game.user_score = the_game.calculate_score(the_game.user_hand)
        the_game.comp_score = the_game.calculate_score(the_game.comp_hand)
        print(f"Your cards: {the_game.user_hand}, Current score: {the_game.user_score}")
        print(f"Computer's first cards: {the_game.comp_hand[0]}")

        is_game_over = the_game.run_round()

    while the_game.comp_score != 0 and the_game.comp_score < 17:
        the_game.comp_hand.append(the_game.deal_card())
        the_game.comp_score = the_game.calculate_score(the_game.comp_hand)

    the_game.display_result()
    the_game.clear_game()


play_game()
while input("Another Game: Y/N") == "y":
    play_game()
