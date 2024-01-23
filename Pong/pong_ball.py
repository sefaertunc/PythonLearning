from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(10)
        self.goto(0, 0)

    def move_ball(self):
        self.forward(0.1)

    def detect_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.setheading(360 - self.heading())

    def detect_ball(self, paddle):
        randomize = random.randint(-10, 10)
        if paddle.index == "r":
            if self.distance(paddle) < 50 and self.xcor() > 340:
                self.setheading(180 - self.heading() + randomize)
        elif paddle.index == "l":
            if self.distance(paddle) < 50 and self.xcor() < -340:
                self.setheading(180 - self.heading() + randomize)
