from turtle import Turtle
ALIGNMENT = 'left'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=FONT)

