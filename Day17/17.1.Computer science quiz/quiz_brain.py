class QuizBrain:

    def __init__(self, questionList):
        self.score = 0
        self.questionNmuber = 0
        self.question_List = questionList

    def next_question(self):
        # question list -> list of attributes
        # new quizbrain("q","a")

        # for i in range(len(self.question_List)):
        #     self.questionNmuber += 1
        #     text = input(f"Q.{self.questionNmuber}: {self.question_List[i].text} (True/False)?:")

        current_answer = self.question_List[self.questionNmuber]
        self.questionNmuber += 1
        user_answer = input(f"Q.{self.questionNmuber}: {current_answer.text} (True/False)?:")

        self.check_answer(user_answer, current_answer)

    def stillHasQuestions(self):
        return self.questionNmuber < len(self.question_List)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.answer.lower():
            self.score += 1
            print("you got it right")

        else:
            print("you are wrong!")
            print(f"The correct answer was {current_answer.answer}.")

        print(f"your current score is {self.score}/{self.questionNmuber}")
        print("\n")

