import random
import turtle as t
from turtle import Screen

s = Screen()

s.colormode(255)


def randomcolor():
    ranred = random.randint(0, 255)
    rangreen = random.randint(0, 255)
    ranblue = random.randint(0, 255)
    color = (ranred, rangreen, ranblue)
    return color


t.speed(0)

def drawCircle(gapSize):

    for i in range(int(360/gapSize)):
        t.pencolor(randomcolor())
        t.circle(50)
        heading = t.heading()
        t.setheading(heading + gapSize)

drawCircle(2)
s.exitonclick()
