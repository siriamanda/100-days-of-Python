from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_coordinates = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.turtlesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            new_car.goto(x=320, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def y_coordinates(self):
        for car in self.all_cars:
            y_cor = car.ycor()
            self.car_coordinates.append(y_cor)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        global MOVE_INCREMENT

        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

