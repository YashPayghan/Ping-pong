from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.pace=0.1

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    #collision detection
    def bounce (self):
        self.y_move *= -1
    def bounce2(self):
        self.x_move *= -1
        self.pace *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.pace=0.1
        self.bounce2()