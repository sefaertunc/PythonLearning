from HigherLowerData import data
import random as rand


class HigherLower:
	def __init__(self):
		self.score = 0
		self.guess = ''
		self.personA = {}
		self.personB = {}
		self.game_end = False
		self.personA = rand.choice(data)

	def chose_competitor(self):
		self.personB = rand.choice(data)
		while self.personB == self.personA:
			self.personB = rand.choice(data)

	def show_competitors(self, person):
		if person == 'a':
			print(f"Compare A: {self.personA['name']}, {self.personA['description']}, {self.personA['country']}")
		elif person == 'b':
			print(f"Compare B: {self.personB['name']}, {self.personB['description']}, {self.personB['country']}")

	def make_guess(self):
		self.guess = input("Which one does have more followers? A or B: ").lower()

	def compare_guesses(self):
		number_A = self.personA['follower_count']
		number_B = self.personB['follower_count']
		if number_A > number_B:
			return self.guess == 'a'
		else:
			return self.guess == 'b'

	def show_result(self):
		result = self.compare_guesses()
		if result:
			self.score += 1
			print(f"Correct Answer! Your score is {self.score}")
			if self.guess == 'b':
				self.personA = self.personB
		else:
			print(f"Wrong Answer! Your final score is {self.score}")
			self.play_again()

	def play_again(self):
		ans = input("Would you like to play again? Y or N: ").lower()
		if ans == 'y':
			self.clean_game()
			return False
		elif ans == 'n':
			self.game_end = True

	def clean_game(self):
		self.score = 0
		self.guess = ''
		self.personA = {}
		self.personB = {}
		self.game_end = False
		self.personA = rand.choice(data)
