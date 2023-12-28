from turtle import Turtle
FONT = ("Arial", 10, "bold")


class StateNames(Turtle):

    def __init__(self, answer_state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.answer_state = answer_state

    def write_state(self):
        self.write(f"{self.answer_state}", font=FONT)
