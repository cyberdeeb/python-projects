class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("Correct!")
        else:
            print(f"Oh no, that was wrong! The right answer was: {correct_answer}")

        print(f"Your current score is {self.score}/{self.question_number}")
        print()

    def next_question(self):
        question = self.question_list[self.question_number].q_text
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {question} (True/False)? ').strip().title()
        self.check_answer(user_answer, answer)

    def more_questions(self):
        return self.question_number < len(self.question_list)

