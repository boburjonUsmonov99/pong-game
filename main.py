from paddle import Paddle
from ball import Ball
from turtle import Screen
from scoreboard import Scoreboard
from gameover import Gameover
import time




screen = Screen()
screen.setup(width=800, height=600)
screen.title("pong")
screen.bgcolor("black")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
gameover = Gameover()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True

while game_is_on == True:
    time.sleep(0.07)
    screen.update()
    ball.move_ball()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 40 and ball.xcor() > 340:
        ball.bounce_x()
        ball.ball_accelerate()

    if ball.distance(paddle_l) < 40 and ball.xcor() < -340:
        ball.bounce_x()
        ball.ball_accelerate()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
    if scoreboard.r_score > 3:
        game_is_on = False
        gameover.r_won()

    if scoreboard.l_score > 3:
        game_is_on = False
        gameover.l_won()



screen.exitonclick()
