from turtle import Turtle

AlIGNMENT = "center"
FONT = ('Arial', 22, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score} ", False, align=AlIGNMENT, font=FONT)

    def increce_the_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def statue_of_game(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=AlIGNMENT, font=FONT)


