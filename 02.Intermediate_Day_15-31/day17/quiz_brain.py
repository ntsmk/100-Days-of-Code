class QuizBrain:
    # when initializing, set question number is 0 and score is 0
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # check if there is questions left
    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    # fetching the question list from the question bank, adding +1 and then check if answer is correct
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(choice, current_question.answer)

    # called by next_question method so you don't need to call this method in main.py
    def check_answer(self, choice, correct_answer):
        if choice.lower() == correct_answer.lower():
            print("you are right!")
            self.score += 1
        else:
            print("you are wrong")
        print(f"correct answer was {correct_answer}")
        print(f"current score: {self.score}/{self.question_number}")
        print("\n")
