from Utilities import general_supplier as supplier
import random as rand

player_count = 5
player_bids = {}
winner = ""
highest_bid = 0

print("Welcome to the Auction!")

while True:
	player_name = input("What is your name? ").capitalize()
	print(f"The item for auction is {rand.choice(supplier.objects)}.")
	player_bid = int(input("What is your bid: "))
	player_bids[player_name] = player_bid

	for num in range(player_count):
		player_bids[rand.choice(supplier.names)] = rand.randint(10, 100)

	for person in player_bids:
		print(f"{person}'s bid is {player_bids[person]}.")

	for person in player_bids:

		if player_bids[person] > highest_bid:
			winner = person
			highest_bid = player_bids[person]

	print(f"The winner is {winner} with {highest_bid}$ bid.")

	winner = ""
	highest_bid = 0
	player_bids.clear()

