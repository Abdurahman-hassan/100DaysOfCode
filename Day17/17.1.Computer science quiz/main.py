from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question = i['question']
    answer = i['correct_answer']
    newQuestion = Question(question, answer)
    # add objects to the list
    question_bank.append(newQuestion)

questionbrain = QuizBrain(question_bank)

while questionbrain.stillHasQuestions():

    questionbrain.next_question()

print(f"your have complete the test")
print(f"your current score is {questionbrain.score}/{questionbrain.questionNmuber}")
