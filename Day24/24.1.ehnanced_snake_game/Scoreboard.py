from turtle import Turtle

AlIGNMENT = "center"
FONT = ('Arial', 22, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_file()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score_board()

    def read_file(self):
        # /Users/abdelrahman/Desktop/high_score_data.txt
        # or
        # ../../ Desktop / high_score_data.txt

        with open("high_score_data.txt") as file:
            high_score = int(file.read())
        return high_score

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High score :{self.high_score} ", False, align=AlIGNMENT, font=FONT)

    def increce_the_score(self):
        self.score += 1
        # self.clear()
        self.update_score_board()

    # def statue_of_game(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, align=AlIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score_data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()
