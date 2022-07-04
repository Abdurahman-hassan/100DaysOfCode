STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start_pos()
        self.y_pos = MOVE_DISTANCE

    def move_up(self):
        y_pos = self.ycor() + self.y_pos
        self.goto(self.xcor(), y_pos)
        # or
        # self.forward(MOVE_DISTANCE)

    def move_down(self):
        y_pos = self.ycor() - self.y_pos
        self.goto(self.xcor(), y_pos)

    def at_the_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start_pos(self):
        self.goto(STARTING_POSITION)
