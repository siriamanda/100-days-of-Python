from turtle import Turtle

UP = 90
DOWN = 270

class Racket(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.new_y = self.ycor()

    def go_right(self):
        self.goto(350, 0)

    def go_left(self):
        self.goto(-350, 0)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
