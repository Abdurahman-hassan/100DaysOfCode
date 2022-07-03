import random
import turtle as t
from turtle import Screen

colorlist = [(182, 65, 34), (213, 149, 97), (14, 24, 42), (230, 237, 233), (239, 208, 94), (241, 234, 238),
              (237, 62, 33), (157, 26, 19), (72, 29, 32), (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37),
              (183, 85, 94), (135, 152, 164), (49, 52, 127), (229, 175, 161), (165, 64, 70), (167, 141, 150),
              (98, 113, 112), (160, 168, 165), (189, 190, 196), (217, 174, 180), (15, 25, 24), (79, 70, 43),
              (183, 196, 189), (119, 121, 147), (248, 196, 4)]

tu = t.Turtle()
tu.hideturtle()
t.colormode(255)
tu.speed(0)

s = Screen()

tu.penup()
# set angel as 225
tu.setheading(225)
# move 300
tu.forward(300)
# start from the base
tu.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    # size of dot is 20 and the color will be chosen randomly
    tu.dot(20, random.choice(colorlist))
    tu.forward(50)

    # dot_count = 10 , 20 ,30 ,40 ,50 ,60 ..etc
    if dot_count % 10 == 0:
        # head up
        tu.setheading(90)
        tu.forward(50)
        # head left
        tu.setheading(180)
        # move 50 step * 10 spaces between steps
        tu.forward(500)
        # start from the base
        tu.setheading(0)
