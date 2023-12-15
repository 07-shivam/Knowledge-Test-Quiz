# quiz.py
from random import shuffle

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.shuffle_questions()

    def shuffle_questions(self):
        shuffle(self.questions)

    def run_quiz(self):
        score = 0
        for question in self.questions:
            print(question.text)
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")

            user_answer = int(input("Your answer (enter the option number): "))
            
            if question.is_correct(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}.\n")

        print(f"You scored {score}/{len(self.questions)} in this quiz.")
