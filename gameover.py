from turtle import Turtle

class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,0)

    def r_won(self):
        self.write("Right won", align="center", font = ("Courier", 80, "normal"))

    def l_won(self):
        self.write("Left won", align="center", font = ("Courier", 80, "normal"))


