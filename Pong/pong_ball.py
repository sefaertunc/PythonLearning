import time
from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(10)
        self.main_speed = 2
        self.speed = self.main_speed
        self.acceleration = 0.015
        self.random_rate = 20
        self.goto(0, 0)

    def move_ball(self):
        self.forward(self.speed)

    def detect_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(360 - self.heading())

    def detect_paddle(self, paddle):
        randomize = random.randint(-self.random_rate, self.random_rate)
        if paddle.index == "r":
            if self.distance(paddle) < 50 and self.xcor() > 340:
                self.setheading(180 - self.heading() + randomize)
                self.speed += self.acceleration
        elif paddle.index == "l":
            if self.distance(paddle) < 50 and self.xcor() < -340:
                self.setheading(180 - self.heading() + randomize)
                self.speed += self.acceleration

    def check_missing(self, scoreboard, r_paddle, l_paddle):
        if self.xcor() > 380:
            scoreboard.increase_score("l")
            self.set_game_again(r_paddle, l_paddle)
        if self.xcor() < -380:
            scoreboard.increase_score("r")
            self.set_game_again(r_paddle, r_paddle)

    def set_game_again(self, r_paddle, l_paddle):
        self.goto(0, 0)
        self.setheading(10)
        self.speed = self.main_speed
        r_paddle.move_zero()
        l_paddle.move_zero()
        time.sleep(2)
