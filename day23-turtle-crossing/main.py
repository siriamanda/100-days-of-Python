import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
score_board = Scoreboard()

random_cars = []

screen.listen()
screen.onkey(turtle.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_forward()

    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            score_board.game_over()
            game_is_on = False

    if turtle.ycor() == 280:
        turtle.go_to_start()
        car_manager.increase_speed()
        score_board.increase_score()

screen.exitonclick()