from turtle import Turtle, Screen

siri = Turtle()
screen = Screen()


def move_forwards():
    siri.forward(10)


def move_backwards():
    siri.backward(10)


def move_clockwise():
    siri.right(10)


def move_counter_clockwise():
    siri.left(10)


def clear_screen():
    siri.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
