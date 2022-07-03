from turtle import Screen

from BallShape import BallShape
from ScoreBoard import ScoreBoard
from paddleShape import PaddleShape
import time as time_of_speed

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong Pong")
s.tracer(0)

paddleShapeObjectRight = PaddleShape((350, 0))
paddleShapeObjectLeft = PaddleShape((-350, 0))
ball = BallShape()
score = ScoreBoard()

s.listen()

s.onkey(key="Up", fun=paddleShapeObjectRight.upMove)
s.onkey(key="Down", fun=paddleShapeObjectRight.downMove)
s.onkey(key="w", fun=paddleShapeObjectLeft.upMove)
s.onkey(key="s", fun=paddleShapeObjectLeft.downMove)

game_is_on = True

while game_is_on:
    time_of_speed.sleep(ball.move_speed)
    s.update()
    ball.move_to_corner()

    # ball in corner in the first of the game
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.y_bounce()

    # ball in paddle
    if ball.distance(paddleShapeObjectRight) < 50 and ball.xcor() > 320 or ball.distance(
            paddleShapeObjectLeft) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l_score()

    # miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r_score()

s.exitonclick()
