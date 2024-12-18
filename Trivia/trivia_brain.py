import question_database as qdb
import trivia_ui as tui
from Utilities import general_supplier

supplier = general_supplier.GeneralSupplier()

class TriviaBrain:
	def __init__(self):
		self.__database = qdb.QuestionDatabase()
		self.__gameUI = tui.TriviaUI()
		self.__current_question = None
		self.__score = 0
		self.__high_score = 0
		self.__initial_settings()
		self.update_question()

	def update_question(self):
		print("Updating question...")
		self.__current_question = self.__database.get_random_question()
		self.__gameUI.question_canvas.itemconfig(self.__gameUI.question_canvas_text, text=self.__current_question[0])

	def check_the_answer(self, answer):
		if answer == self.__current_question[1]:
			self.__score += 1
			self.__gameUI.current_score["text"] = f"Score: {self.__score}"
			self.__save_score()
			self.__change_background("green")
		else:
			print("Wrong answer!")
			self.__change_background("red")

	def __change_background(self, color):
		print("Changing background...")
		self.__gameUI.question_canvas.config(background=color)
		self.__gameUI.question_canvas.after(1000, lambda: self.__reset_background())

	def __reset_background(self):
		self.__gameUI.question_canvas.config(background="white")
		self.update_question()

	def __save_score(self):
		if self.__score >= self.__high_score:
			self.__high_score = self.__score
			self.__gameUI.high_score["text"] = f"High Score: {self.__high_score}"
			with open("score.txt", "w") as high_score_file:
				high_score_file.write(str(self.__score))

	def __initial_settings(self):
		self.__gameUI.true_button.config(command=lambda: self.check_the_answer("True"))
		self.__gameUI.false_button.config(command=lambda: self.check_the_answer("False"))
		try:
			with open("score.txt", "r") as high_score_file:
				score = high_score_file.read()
				self.__high_score = int(score)
		except FileNotFoundError:
			print("Score file not found!")
			with open("score.txt", "w") as high_score_file:
				high_score_file.write(str(self.__high_score))
		finally:
			self.__gameUI.high_score["text"] = f"High Score: {self.__high_score}"
			self.__gameUI.current_score["text"] = f"Score: {self.__score}"

	def get_main_loop(self):
		self.__gameUI.window.mainloop()
