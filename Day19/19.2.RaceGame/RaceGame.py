import random as r
from turtle import Turtle, Screen

s = Screen()
s.setup(width=500, height=400)
colorOfWinnerTurtle = s.textinput(title="create your turtle", prompt="Enter the color of your turtle")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
listOfTurtles = []

# creating the lists of objects
yRange = -125
lenOfTurtleShape = 40

for i in range(6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.color(colors[i])
    newTurtle.goto(x=-230, y=yRange)
    listOfTurtles.append(newTurtle)
    yRange += 50

if colorOfWinnerTurtle:
    isRaceOn = True

while isRaceOn:
    for turtle in listOfTurtles:
        if turtle.xcor() > (250 - (lenOfTurtleShape / 2)):
            isRaceOn = False
            winner = turtle.pencolor()

            if winner == colorOfWinnerTurtle:
                print(f"You are right the {winner} turtle is won ")
            else:
                print(f"You are lose the {winner} turtle is won ")

        random_number = r.randint(0, 10)
        turtle.forward(random_number)


s.exitonclick()
