from turtle import Screen
import time
from Food import Food
from Scoreboard import ScoreBoard
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

# create a list of objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up_position, "Up")
screen.onkey(snake.down_position, "Down")
screen.onkey(snake.left_position, "Left")
screen.onkey(snake.right_position, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # infinite loop until the snake makes an action just like touch his tail or the edges of screen
    snake.move()

    # detect collision with a food
    if snake.head.distance(food) < 15:
        scoreboard.increce_the_score()
        food.refresh_the_food()
        snake.extend_a_snake_body()

    # detect collision with a wall and tail
    if snake.head.xcor() > 290 or snake.head.xcor() < - 290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290 or snake.isTailCollisioned():
        # game_is_on = False
        scoreboard.reset()
        snake.reset()


screen.exitonclick()
