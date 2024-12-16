import requests as rq
import random as rd


class QuestionDatabase:
	def __init__(self):
		self.__questions_data_list = self.__assign_database()

	@staticmethod
	def __assign_database():
		questions_api = rq.get("https://opentdb.com/api.php?amount=30&category=9&difficulty=medium&type=boolean")
		questions_api.raise_for_status()
		return questions_api.json()["results"]

	def get_random_question(self):
		"""Return a tuple which comprises the question and its answer in a tuple."""
		num = rd.randint(0, len(self.__questions_data_list) - 1)
		data = self.__questions_data_list[num]
		question = data["question"]
		answer = data["correct_answer"]
		question_tuple = (question, answer)
		return question_tuple
