from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.back(10)


def move_left():
    # t.left(10)
    # or
    head = t.heading() + 10
    t.setheading(head)


def move_right():
    t.right(10)


def reset():
    #t.reset()

    # or
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=move_left)
s.onkey(key="d", fun=move_right)
s.onkey(key="c", fun=reset)
s.exitonclick()



