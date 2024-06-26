import random


class GeneralSupplier:
	def __init__(self):
		self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
						 't', 'u', 'v', 'w', 'x', 'y', 'z']
		self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		self.symbols = ['+', '-', '*', '/', '?', '%', '&', ')', '(', '#', '!', '=', '$', '@', ]
		self.names = ["Javier", "Anna", "Cherokee", "Betsy", "Tatyana", "Zack", "Amanda", "Miracle", "Devyn", "Cielo"]
		self.objects = ["flashlight", "shoe lace", "squirt gun", "packet of seeds", "pants", "lighter",
						"box of baking soda",
						"mobile phone", "bottle cap", "chocolates", "whip", "plastic fork", "comb", "spool of ribbon",
						"wine glass", "house", "desk", "glass", "ice cube", "apple", "can of whipped cream",
						"rusty nail", "mp3 player", "balloon",
						"CD", "coffee mug", "extension cord", "rat", "banana"]
		self.color = ["red", "green", "yellow", "blue", "magenta", "cyan", "black"]

		self.PI = 3.14159

	def get_random_color(self):
		return random.choice(self.color)

	def get_color_by_index(self, number):
		return self.color[number]
