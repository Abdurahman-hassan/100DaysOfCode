from turtle import Turtle


class PaddleShape(Turtle):

    def __init__(self, POS):
        super().__init__()
        self.pos_with_tuble = POS
        self.createPaddleBody()

    def createPaddleBody(self):
        self.shape("square")
        self.color("White")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.pos_with_tuble)

    def upMove(self):
        yPostion = self.ycor() + 20
        self.goto(self.xcor(), yPostion)

    def downMove(self):
        yPostion = self.ycor() - 20
        self.goto(self.xcor(), yPostion)
