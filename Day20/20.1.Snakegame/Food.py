import random
from turtle import Turtle, Screen

s = Screen()

s.colormode(255)


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.stretch_len = 0.8
        self.stretch_wid = 0.8
        self.color("blue")
        self.speed("fastest")
        # the default size is 20 so this fum will divide the default divide by args
        self.shapesize(self.stretch_len, self.stretch_wid)
        self.refresh_the_food()

    def randomcolor(self):
        ranred = random.randint(0, 255)
        rangreen = random.randint(0, 255)
        ranblue = random.randint(0, 255)
        color = (ranred, rangreen, ranblue)
        return color

    def refresh_the_food(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.color(self.randomcolor())
        self.goto(random_x, random_y)


