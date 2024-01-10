from quiz_game_brain import QuizGameBrain
from quiz_game_data import question_data
from quiz_gam_question_model import Question

question_bank = []
for q in question_data:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

game_brain = QuizGameBrain(question_bank)

while game_brain.still_has_questions():
    game_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score is {game_brain.score}/{len(game_brain.questions)}")
