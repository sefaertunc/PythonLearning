import question_database as qdb


class TriviaBrain:
	def __init__(self):
		self.question = ()
		self.__database = qdb.QuestionDatabase()

	def get_question(self):
		self.question = self.__database.get_random_question()
		return self.question
