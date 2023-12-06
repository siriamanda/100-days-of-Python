from turtle import Screen
from racket import Racket

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

racket_1 = Racket()
racket_1.go_right()

racket_2 = Racket()
racket_2.go_left()

screen.listen()
screen.listen()
screen.onkey(racket_1.go_up, "Up")
screen.onkey(racket_1.go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()