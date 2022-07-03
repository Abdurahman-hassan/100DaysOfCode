import random
import turtle as t
from turtle import Screen

t = t.Turtle()
s = Screen()
t.shape("arrow")
color_list = ["firebrick", "magenta", "dark orchid", "dark orange", "lime green", "olive drab"]



def drawSquare():
t.pensize(15)
    for i in range(4):
        t.forward(150)
        t.color(random.choice(color_list))
        t.right(90)


drawSquare()

s.onscreenclick()
