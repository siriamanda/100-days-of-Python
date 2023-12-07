from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 60, "bold")


class Scoreboard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.current_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

