from turtle import Turtle


class BallShape(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball_shape()
        self.y_move = 10
        self.x_move = 10
        self. move_speed = 0.1

    def create_ball_shape(self):
        self.shape("circle")
        self.color("white")
        self.setpos(0, 0)
        self.penup()

    def move_to_corner(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def y_bounce(self):
        # y -> up and down
        # 290 -> 280 -> 270 -> ....
        self.y_move *= -1

    def x_bounce(self):
        # x -> left and right
        # 290 ->280 -> 270 -> ....
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()
