from turtle import Turtle


class Score_ball(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()


    def update_scoreboard(self):
        self.write(self.score, align=" center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
