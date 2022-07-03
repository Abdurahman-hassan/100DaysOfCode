import random
import turtle as t
from turtle import Screen

t = t.Turtle()
s = Screen()
t.shape("arrow")
color_list = ["firebrick", "magenta", "dark orchid", "dark orange", "lime green", "olive drab"]


def drawallShapsOldTecniqe():
    angel = 360
    for i in range(3 + 4 + 5 + 6 + 7 + 8 + 9):
        t.forward(100)

        if 0 <= i < 3:
            t.right(angel / 3)
        elif 3 <= i < 7:
            t.right(angel / 4)
        elif 7 <= i < 12:
            t.right(angel / 5)
        elif 12 <= i < 18:
            t.right(angel / 6)
        elif 18 <= i < 25:
            t.right(angel / 7)
        elif 25 <= i < 33:
            t.right(angel / 8)
        elif 33 <= i < 42:
            t.right(angel / 9)

#drawallShapsOldTecniqe()

def drawallShapsDynamicly(numberSides):
    t.pensize(8)
    angel = 360 / numberSides

    for i in range(numberSides):
        t.forward(100)
        t.right(angel)


for i in range(3, 10):
    t.color(random.choice(color_list))
    drawallShapsDynamicly(i)

s.onscreenclick()
