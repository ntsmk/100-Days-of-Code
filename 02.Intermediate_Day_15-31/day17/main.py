from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

# print(question_bank[0].answer)
# print(len(question_bank))
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    #quiz.check_answer() you don't have to put this