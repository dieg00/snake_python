from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = -1
        self.setpos(0, 260)
        self.color("white")
        self.add_point()

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=("arial", 25, "normal"))

    def game_over(self):
        self.setpos(0, 0)
        self.write(arg="GAME OVER", align="center", font=("arial", 25, "normal"))
