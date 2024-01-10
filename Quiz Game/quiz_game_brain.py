class QuizGameBrain:
    def __init__(self, questions):
        self.questions = questions
        self.question_id = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_id < len(self.questions)

    def next_question(self):
        current_question = self.questions[self.question_id]
        self.question_id += 1
        answer = input(f"Q.{self.question_id}: {current_question.text} (true/false): ")
        self.check_answer(answer,current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("Your answer is correct")
            self.score += 1
        else:
            print("Your answer is incorrect")
        print(f"Your score is {self.score}/{self.question_id}\n")
