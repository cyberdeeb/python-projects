from art import logo
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
print(logo)


for item in question_data:
    new_question = Question(item["text"], item["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.more_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"You're score was {quiz.score}/{quiz.question_number}")