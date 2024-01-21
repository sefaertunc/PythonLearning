import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
bid_list = [5, 10, 20, 50, 100]


class Blackjack:
    def __init__(self):
        self.user_hand = []
        self.comp_hand = []
        self.user_score = 0
        self.comp_score = 0

    def compare_scores(self):
        """The method provides to compare hands of players and returns result with announcement"""
        if self.user_score == self.comp_score:
            return "Draw 🙃"
        elif self.comp_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif self.user_score == 0:
            return "Win with a Blackjack 😎"
        elif self.user_score > 21:
            return "You went over. You lose 😭"
        elif self.comp_score > 21:
            return "Opponent went over. You win 😁"
        elif self.user_score > self.comp_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    def run_round(self):
        if self.user_score == 0 or self.comp_score == 0 or self.user_score > 21:
            return True
        else:
            user_should_deal = input("Another card? Y/N").lower()
            if user_should_deal == "y":
                self.user_hand.append(self.deal_card())
                return False
            else:
                return True

    def display_result(self):
        print(f"   Your final hand: {self.user_hand}, final score: {self.user_score}")
        print(f"   Computer's final hand: {self.comp_hand}, final score: {self.comp_score}")
        print(self.compare_scores())

    def clear_game(self):
        self.user_hand.clear()
        self.comp_hand.clear()
        self.user_score = 0
        self.comp_score = 0

    @staticmethod
    def deal_card():
        card = random.choice(deck)
        return card

    @staticmethod
    def calculate_score(hand):
        if sum(hand) == 21 and len(hand) == 2:
            return 0

        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
        return sum(hand)
