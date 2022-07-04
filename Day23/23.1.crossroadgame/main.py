import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Cross road game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for car_in_list in car.list_of_cars:
        if car_in_list.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.at_the_finish_line():
        player.go_to_start_pos()
        car.level_up()
        scoreboard.increse_level()

screen.exitonclick()
