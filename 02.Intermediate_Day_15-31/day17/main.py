from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create object by using Question class. Fetching question and answer from the data set.
# adding them to the list called question bank
question_bank = []
for question in question_data:
    new_question = Question(question['question'], question['correct_answer'])
    question_bank.append(new_question)

# create object by using QuizBrain class. Judge if it has still questions in the question bank.
# if still questions, keep going
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

# after confirming no questions left, printing out the results
print(f"You've completed the quiz")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")