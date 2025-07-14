from cgitb import reset
from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from score import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

paddle_1 = Paddle((350,0))
paddle_2 = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update()


game_is_on=True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.pace)
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce()
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce2()
    if ball.xcor() > 350:
        ball.reset_ball()
        scoreboard.l_point()
    elif ball.xcor() < -350:
        ball.reset_ball()
        scoreboard.r_point()
    screen.listen()
    screen.onkeypress(paddle_1.move_up, "Up")
    screen.onkeypress(paddle_1.move_down, "Down")
    screen.onkeypress(paddle_2.move_up, "w")
    screen.onkeypress(paddle_2.move_down, "s")
screen.exitonclick()