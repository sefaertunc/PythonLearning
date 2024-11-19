from Utilities import general_supplier
import random as rand

supplier = general_supplier.GeneralSupplier()


class auction_base(object):
	def __init__(self):
		self.player_bids = {}
		self.player_count = 0
		self.winner = ""
		self.highest_bid = 0
		self.end_game = False
		self.item = ""
		self.player = auction_main_player()
		print("Welcome to the Auction!")

	def create_bids(self):
		self.player_count = rand.randint(1, 10)
		for num in range(self.player_count):
			self.player_bids[supplier.get_random_name()] = rand.randint(10, 100)

	def choose_item(self):
		self.item = supplier.get_random_object()
		print(f"The item for auction is {self.item}.")

	def show_bids(self):
		for person in self.player_bids:
			print(f"{person}'s bid is ${self.player_bids[person]}.")

	def check_winner(self):
		for person in self.player_bids:
			if self.player_bids[person] > self.highest_bid:
				self.winner = person
				self.highest_bid = self.player_bids[person]
		if self.winner == self.player.player_name:
			self.player.player_money -= self.player.player_bid
			self.player.items.append(self.item)

	def show_winner(self):
		print(f"The winner is {self.winner} with ${self.highest_bid} bid.")

	@staticmethod
	def another_game(rest_money):
		print(f"You have {rest_money} dollar left.")
		while True:
			answer = input("Would you like to bid another? (y/n) ").lower()
			if answer == 'y' or answer == 'n':
				if answer == "y":
					return False
				elif answer == "n":
					return True
				break
			print("Invalid Input")


	def clean_bids(self):
		self.player_bids.clear()
		self.player_count = 0
		self.winner = ""
		self.highest_bid = 0
		self.item = ""

	def check_end_game(self):
		if self.player.player_money <= 0:
			self.end_game = True
		self.end_game = self.another_game(self.player.player_money)
		if self.end_game:
			print(f"You left the auction with {', '.join(self.player.items)} and {self.player.player_money} dollars left!")


class auction_main_player(object):
	def __init__(self):
		self.player_name = input("What is your name? ").capitalize()
		print("How many dollars do you have?")
		self.player_money = self.integer_check()
		self.items = []
		self.player_bid = 0

	def add_bid(self, var_bids_dic):
		print("What is your bid: ")
		self.player_bid = self.integer_check()
		while self.player_bid > self.player_money:
			print("You don't have enough money. Try again!")
			self.player_bid = self.integer_check()
		var_bids_dic[self.player_name] = self.player_bid

	def clean_bids(self):
		self.player_bid = 0

	@staticmethod
	def integer_check():
		while True:
			try:
				var_integer = int(input())
				break
			except ValueError:
				print("Invalid Input")
		return var_integer
