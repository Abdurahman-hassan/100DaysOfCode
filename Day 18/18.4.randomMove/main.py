import random
import turtle as t
from turtle import Screen
import random as r

s = Screen()
t = t.Turtle()
directions = [0, 90, 180, 270]
t.pensize(4)
t.hideturtle()

s.colormode(255)

def randomColor():
    ranRed = r.randint(0, 255)
    ranGreen = r.randint(0, 255)
    ranblue = r.randint(0, 255)
    rancolorTuble = (ranRed, ranGreen, ranblue)
    return rancolorTuble

for i in range(300):
    t.pencolor(randomColor())
    t.forward(15)
    t.setheading(r.choice(directions))
    t.speed(0)

print(t.position())

s.exitonclick()
