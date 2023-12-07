from turtle import Screen
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

racket_1 = Racket(350, 0)
racket_2 = Racket(-350, 0)
ball = Ball()
racket_1_score = Scoreboard(80, 220)
racket_2_score = Scoreboard(-80, 220)


screen.listen()
screen.onkey(racket_1.go_up, "Up")
screen.onkey(racket_1.go_down, "Down")
screen.onkey(racket_2.go_up, "w")
screen.onkey(racket_2.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    screen.update()

    # Detect collision with racket_1

    if ball.distance(racket_1) < 50 and ball.xcor() > 320 or ball.distance(racket_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when racket missed the ball

    if ball.xcor() > 380:
        ball.reset_position()
        racket_2_score.increase_score()
    elif ball.xcor() < -380:
        racket_1_score.increase_score()
        ball.reset_position()


screen.exitonclick()