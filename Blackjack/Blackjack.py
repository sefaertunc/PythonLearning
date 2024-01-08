import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


bid_list = [5, 10, 20, 50, 100]
bid = 0


def select_bid():
    bid = input(f"Select the bid: {bid_list}")


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    user_cards = []
    comp_cards = []
    is_game_over = False

    def deal_cards():
        """Return a random card from deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    for _ in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, Current score: {user_score}")
        print(f"Computer's first cards: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Another card? Y/N").lower()
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_cards())
        comp_score = calculate_score(comp_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))


play_game()
while input("Another Game: Y/N") == "y":
    play_game()
