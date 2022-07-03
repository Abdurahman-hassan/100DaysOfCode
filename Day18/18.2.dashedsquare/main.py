import random
import turtle as t
from turtle import Screen

t = t.Turtle()
s = Screen()
t.shape("arrow")
color_list = ["firebrick", "magenta", "dark orchid", "dark orange", "lime green", "olive drab"]

t.speed(0)
def dashedLine():
    t.pensize(3)
    t.color(random.choice(color_list))
    t.forward(4)
    t.penup()
    t.color(random.choice(color_list))
    t.forward(4)
    t.pendown()


for i in range(4):
    t.left(90)
    for j in range(40):
        dashedLine()

s.onscreenclick()
