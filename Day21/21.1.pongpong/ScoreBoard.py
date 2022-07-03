from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_player_one = 0
        self.score_player_two = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_player_two, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_player_one, align="center", font=("Arial", 80, "normal"))

    def increase_l_score(self):
        self.score_player_two += 1
        self.update_score()

    def increase_r_score(self):
        self.score_player_one += 1
        self.update_score()
