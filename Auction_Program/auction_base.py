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
		print("Welcome to the Auction!")

	def create_bids(self):
		self.player_count = rand.randint(1, 10)
		for num in range(self.player_count):
			self.player_bids[rand.choice(supplier.names)] = rand.randint(10, 100)

	@staticmethod
	def choose_item():
		print(f"The item for auction is {rand.choice(supplier.objects)}.")

	def show_bids(self):
		for person in self.player_bids:
			print(f"{person}'s bid is ${self.player_bids[person]}.")

	def check_winner(self):
		for person in self.player_bids:
			if self.player_bids[person] > self.highest_bid:
				self.winner = person
				self.highest_bid = self.player_bids[person]

	def show_winner(self):
		print(f"The winner is {self.winner} with ${self.highest_bid} bid.")

	@staticmethod
	def another_game():
		answer = input("Would you like to bid another? (y/n) ").lower()
		if answer == "y":
			return False
		elif answer == "n":
			return True

	def clean_bids(self):
		self.player_bids.clear()
		self.player_count = 0
		self.winner = ""
		self.highest_bid = 0


class auction_main_player(object):
	def __init__(self):
		self.player_name = input("What is your name? ").capitalize()
		self.player_bid = 0

	def add_bid(self, var_bids_dic):
		self.player_bid = int(input("What is your bid: "))
		var_bids_dic[self.player_name] = self.player_bid

	def clean_bids(self):
		self.player_bid = 0
