import random
from turtle import Screen, Turtle

# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
from player import Player

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen = Screen()
screen.colormode(255)


class CarManager:

    def __init__(self):
        self.list_of_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        random_of_crossing_car = random.randint(1, 6)
        if random_of_crossing_car == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(self.random_color())
            new_car.shapesize(stretch_wid=1, stretch_len=2)

            # generate a random number to be up and down
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.list_of_cars.append(new_car)

    def random_color(self):
        ran_red = random.randint(0, 255)
        ran_green = random.randint(0, 255)
        ran_blue = random.randint(0, 255)
        color = (ran_red, ran_green, ran_blue)
        return color

    def move_cars(self):
        for car in self.list_of_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 10
